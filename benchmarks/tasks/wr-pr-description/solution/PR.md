Fix region totals for quoted CSV fields

- `report.py` reads the file with `csv.DictReader` instead of splitting on commas, so a customer like `"Smith, Jones & Co"` no longer shifts the amount column and drops the row
- Removes `print_debug`, which nothing called
- Adds `test_report.py` with one test for quoted fields and escaped quotes; `pytest` passes
- The commit subject mentions a `--json` flag; the diff does not add one
