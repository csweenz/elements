from __future__ import annotations

import datetime as dt
from decimal import Decimal

import pytest

from elemental.util.etl.feedstock_prices import HenryHubNaturalGasETL
from elemental.models import Feedstock, FeedstockPrice, PriceSource

SAMPLE_CSV = """Month,United States
2024-01-01,2.500
2024-02-01,2.750
2024-03-01,
2024-04-01,3.100
"""

pytestmark = pytest.mark.django_db


@pytest.fixture
def natural_gas_feedstock():
    return Feedstock.objects.create(feedstock_id=2, key="naturalgas", name="Natural Gas")


def is_aware(dtobj: dt.datetime) -> bool:
    return dtobj.tzinfo is not None and dtobj.utcoffset() is not None

def is_utc(dtobj: dt.datetime) -> bool:
    return is_aware(dtobj) and dtobj.utcoffset() == dt.timedelta(0)


def test_transform_filters_empty_rows(natural_gas_feedstock):
    pipeline = HenryHubNaturalGasETL(fetcher=lambda url: SAMPLE_CSV)
    result = pipeline.run(dry_run=True)

    assert len(result.records) == 3  # skips the blank row
    prices = [r.price for r in result.records]
    assert prices == [Decimal("2.500"), Decimal("2.750"), Decimal("3.100")]

    first = result.records[0]
    assert is_aware(first.ts)
    assert is_utc(first.ts)


def test_load_is_idempotent(natural_gas_feedstock):
    pipeline = HenryHubNaturalGasETL(fetcher=lambda url: SAMPLE_CSV)

    first_run = pipeline.run(limit=3)
    assert first_run.load_summary is not None
    assert first_run.load_summary.created == 3
    assert FeedstockPrice.objects.count() == 3

    second_run = pipeline.run(limit=3)
    assert second_run.load_summary is not None
    assert second_run.load_summary.skipped == 3
    assert FeedstockPrice.objects.count() == 3  # no duplicates

    source = PriceSource.objects.get(name=pipeline.price_source_name)
    assert source.url == pipeline.price_source_url
