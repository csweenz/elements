from __future__ import annotations

from django.core.management.base import BaseCommand, CommandError

from elemental.util.etl import HenryHubNaturalGasETL
from elemental.models import Feedstock


class Command(BaseCommand):
    help = (
        "Ingest Henry Hub natural gas prices from the DataHub monthly dataset into "
        "the feedstock_prices table."
    )

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Fetch and parse the upstream data without writing to the database.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            help="Only process the most recent N observations from the upstream dataset.",
        )

    def handle(self, *args, **options) -> None:
        pipeline = HenryHubNaturalGasETL()
        dry_run: bool = options["dry_run"]
        limit = options.get("limit")
        try:
            result = pipeline.run(dry_run=dry_run, limit=limit)
        except Feedstock.DoesNotExist:
            raise CommandError(
                "Feedstock with key 'naturalgas' is missing. Run the seed migrations first."
            )
        except Exception as exc:  # pragma: no cover
            raise CommandError(str(exc)) from exc

        records = list(result.records)
        if dry_run:
            self.stdout.write(
                f"Fetched {len(records)} transformed observations (dry-run, nothing persisted)."
            )
            for record in records[-5:]:
                self.stdout.write(
                    f"  · {record.ts.date()}: {record.price} {record.currency} per {record.unit}"
                )
            return

        summary = result.load_summary
        if summary is None:
            raise CommandError("Pipeline returned no load summary; this should not happen.")

        self.stdout.write(
            self.style.SUCCESS(
                "Feedstock pricing import complete: "
                f"created={summary.created}, updated={summary.updated}, skipped={summary.skipped}"
            )
        )