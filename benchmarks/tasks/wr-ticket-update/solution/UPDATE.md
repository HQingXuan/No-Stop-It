Nightly rollup: 12 min to 3 h since Sep 14. Cause found, fix drafted.

- Migration 0042 (Sep 14) replaced the `created_at` index with a composite `(customer_id, created_at)` index. The rollup filters on `created_at` alone, so Postgres cannot use the new index and scans all 14M rows, once per hour bucket
- Not disk, network, data volume or the driver bump: rows grew 2%, time grew 15x
- Next: migration 0043 re-adds the `created_at` index (`CREATE INDEX CONCURRENTLY`, about 6 min on staging). Drafted, not merged. The first run after it lands should be back near 12 min
- Separate ticket: the 06:00 report build should fail when the rollup has not finished, instead of reading stale numbers
