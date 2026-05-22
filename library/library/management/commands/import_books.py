import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.db import OperationalError
from library.models import Book


class Command(BaseCommand):
    help = "Import books from a CSV file. Expected columns: title,author,genre,published_year,available"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all existing books before importing",
        )

    def handle(self, *args, **options):
        path = options["csv_file"]
        if not os.path.exists(path):
            raise CommandError(f"File not found: {path}")

        if options["clear"]:
            try:
                count, _ = Book.objects.all().delete()
                self.stdout.write(self.style.WARNING(f"Deleted {count} existing books."))
            except OperationalError:
                raise CommandError(
                    "Database table not found. Run 'python manage.py migrate' first."
                )

        created = 0
        skipped = 0

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=2):
                try:
                    available_raw = row.get("available", "true").strip().lower()
                    available = available_raw in ("true", "1", "yes")
                    Book.objects.create(
                        title=row["title"].strip(),
                        author=row["author"].strip(),
                        genre=row["genre"].strip(),
                        published_year=int(row["published_year"].strip()),
                        available=available,
                    )
                    created += 1
                except OperationalError:
                    raise CommandError(
                        "Database table not found. Run 'python manage.py migrate' first."
                    )
                except (KeyError, ValueError) as e:
                    self.stderr.write(f"Row {i} skipped — {e}")
                    skipped += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {created} books."))
        if skipped:
            self.stdout.write(self.style.WARNING(f"Skipped {skipped} rows due to errors."))
