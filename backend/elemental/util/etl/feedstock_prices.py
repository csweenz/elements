"""Feedstock price ETL pipeline implementations.

This module provides reusable building blocks for bringing external pricing
sources into the local ``feedstock_prices`` table.  The intent is to make the
Extract/Transform/Load steps explicit so that they can be orchestrated both from
unit tests and from ad-hoc management commands.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from io import StringIO
from typing import Callable, Iterable, Optional, Sequence
from urllib import request

from django.db import transaction
import datetime as dt

from elemental.models import Feedstock, FeedstockPrice, PriceSource

# Public ---------------------------------------------------------------------------------------

Fetcher = Callable[[str], str]

@dataclass(frozen=True)
class FeedstockPriceObservation:

    ts: dt.datetime
    price: Decimal
    currency: str
    unit: str


@dataclass
class LoadSummary:

    created: int = 0
    updated: int = 0
    skipped: int = 0

    def as_dict(self) -> dict[str, int]:
        return {"created": self.created, "updated": self.updated, "skipped": self.skipped}


@dataclass(frozen=True)
class PipelineRunResult:
    """Container returned by :meth:`FeedstockPriceETLPipeline.run`."""

    records: Sequence[FeedstockPriceObservation]
    load_summary: Optional[LoadSummary]


class FeedstockPriceETLPipeline:
    feedstock_key: str
    price_source_name: str
    price_source_url: Optional[str]

    def __init__(self, fetcher: Optional[Fetcher] = None) -> None:
        self.fetcher = fetcher or default_fetcher

    # --- Orchestration ---------------------------------------------------------------------
    def run(self, *, dry_run: bool = False, limit: Optional[int] = None) -> PipelineRunResult:
        raw_payload = self.extract()
        records = tuple(self.transform(raw_payload))
        if limit is not None:
            if limit <= 0:
                raise ValueError("limit must be positive when provided")
            records = records[-limit:]
        summary = None
        if not dry_run:
            summary = self.load(records)
        return PipelineRunResult(records=records, load_summary=summary)

    # --- Individual phases -----------------------------------------------------------------
    def extract(self) -> str:
        """Fetch raw text from the upstream provider."""

        if not self.price_source_url:
            raise ValueError("price_source_url must be configured on the pipeline")
        return self.fetcher(self.price_source_url)

    def transform(self, raw_payload: str) -> Iterable[FeedstockPriceObservation]:  # pragma: no cover
        """Turn the raw response into :class:`FeedstockPriceObservation` objects."""

        raise NotImplementedError

    def load(self, records: Sequence[FeedstockPriceObservation]) -> LoadSummary:
        """Persist the normalized observations into ``feedstock_prices``."""

        feedstock = Feedstock.objects.get(key=self.feedstock_key)
        price_source, _ = PriceSource.objects.get_or_create(
            name=self.price_source_name,
            defaults={"url": self.price_source_url},
        )
        summary = LoadSummary()
        with transaction.atomic():
            for record in records:
                obj, created = FeedstockPrice.objects.get_or_create(
                    feedstock=feedstock,
                    ts=record.ts,
                    defaults={
                        "price": record.price,
                        "currency": record.currency,
                        "unit": record.unit,
                        "source": price_source,
                    },
                )
                if created:
                    summary.created += 1
                    continue

                changed = False
                if obj.price != record.price:
                    obj.price = record.price
                    changed = True
                if obj.currency != record.currency:
                    obj.currency = record.currency
                    changed = True
                if obj.unit != record.unit:
                    obj.unit = record.unit
                    changed = True
                if obj.source_id != price_source.pk:
                    obj.source = price_source
                    changed = True
                if changed:
                    obj.save(update_fields=["price", "currency", "unit", "source"])
                    summary.updated += 1
                else:
                    summary.skipped += 1
        return summary


# Helpers ---------------------------------------------------------------------------------------

DEFAULT_USER_AGENT = "elements-etl/1.0 (+https://example.com)"


def default_fetcher(url: str) -> str:
    """Small utility wrapper so the pipeline can be exercised without requests."""

    req = request.Request(url, headers={"User-Agent": DEFAULT_USER_AGENT})
    with request.urlopen(req, timeout=30) as resp:
        payload = resp.read().decode("utf-8")
    if not payload.strip():
        raise ValueError(f"Received empty payload from {url}")
    return payload


def _is_aware(x: dt.datetime) -> bool:
    return x.tzinfo is not None and x.utcoffset() is not None

def parse_timestamp(value: str) -> dt.datetime:
    value = value.strip()
    parsed: Optional[dt.datetime] = None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%m/%d/%Y"):
        try:
            parsed = dt.datetime.strptime(value, fmt)
            break
        except ValueError:
            continue
    if parsed is None:
        raise ValueError(f"Unrecognized timestamp '{value}'")
    if len(value) == 7:  # YYYY-MM -> normalize to first day of month
        parsed = parsed.replace(day=1)
    # If naive, assume upstream data is UTC; otherwise normalize to UTC.
    if not _is_aware(parsed):
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    else:
        parsed = parsed.astimezone(dt.timezone.utc)
    return parsed


def coerce_decimal(value: str) -> Decimal:
    """Convert text to :class:`~decimal.Decimal`, handling empty markers."""

    text = value.strip()
    if not text:
        raise ValueError("Missing price value")
    try:
        return Decimal(text)
    except InvalidOperation as exc:  # pragma: no cover - defensive programming
        raise ValueError(f"Could not interpret '{value}' as a decimal") from exc


# Henry Hub --------------------------------------------------------------------------------------

class HenryHubNaturalGasETL(FeedstockPriceETLPipeline):
    """ETL implementation for Henry Hub natural gas (feedstock key ``naturalgas``)."""

    feedstock_key = "naturalgas"
    price_source_name = "Henry Hub Natural Gas (DataHub monthly)"
    price_source_url = "https://datahub.io/core/natural-gas/r/monthly.csv"
    currency = "USD"
    unit = "USD/MMBtu"

    PRICE_COLUMN_CANDIDATES = (
        "Henry Hub Natural Gas Spot Price Dollars per Million Btu",
        "United States",
        "Price",
        "Value",
    )

    def transform(self, raw_payload: str) -> Iterable[FeedstockPriceObservation]:
        csv_buffer = StringIO(raw_payload)
        reader = csv.DictReader(csv_buffer)
        if reader.fieldnames is None:
            raise ValueError("CSV payload does not contain headers")

        price_column = self._determine_price_column(reader.fieldnames)
        for row in reader:
            timestamp_raw = row.get("Month") or row.get("Date") or row.get("month")
            if not timestamp_raw:
                continue  # ignore malformed row
            try:
                ts = parse_timestamp(timestamp_raw)
            except ValueError:
                continue

            price_raw = row.get(price_column, "")
            if not price_raw or not price_raw.strip():
                continue
            try:
                price = coerce_decimal(price_raw)
            except ValueError:
                continue
            yield FeedstockPriceObservation(ts=ts, price=price, currency=self.currency, unit=self.unit)

    def _determine_price_column(self, headers: Sequence[str]) -> str:
        for candidate in self.PRICE_COLUMN_CANDIDATES:
            if candidate in headers:
                return candidate
        numeric_headers = [h for h in headers if h not in {"Month", "Date", "month"}]
        if not numeric_headers:
            raise ValueError("Could not determine which column holds the price")
        return numeric_headers[0]