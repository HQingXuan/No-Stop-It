# rollup slowness, raw notes

Nightly `rollup.py` (cron 02:00 UTC) used to finish in about 12 min. Since Sep 14 it takes about 3 h, and twice it overran into the 06:00 report build (Sep 20, Sep 27), which then read the previous day's numbers without complaint.

## timings (job log)

| night | wall time |
|---|---|
| Sep 12 | 11m40s |
| Sep 13 | 12m05s |
| Sep 14 | 2h51m |
| Sep 15 | 2h58m |
| Sep 27 | 3h12m |

## dead ends

- disk: iostat during the Sep 27 run, util under 20%, no queueing. not disk.
- network: the job talks to the db over the local socket. nothing there.
- data growth: orders grew 14.1M -> 14.4M rows over the period. 2% more rows, 15x more time. not volume.
- postgres version: unchanged, 15.4 since June.
- the Sep 14 deploy also bumped the psycopg driver. rolled that back on staging, no change. not the driver.

## what it is

The slow statement is the range query in rollup.py line 41, run once per hour bucket (24 times per run):

    SELECT customer_id, amount FROM orders WHERE created_at >= %s AND created_at < %s

EXPLAIN ANALYZE on Sep 27:

    Seq Scan on orders  (cost=0.00..412233.00 rows=48211 width=16) (actual time=0.031..9811.442 rows=47960 loops=1)
      Filter: ((created_at >= ...) AND (created_at < ...))
      Rows Removed by Filter: 14352040

Same query from the Sep 12 slow-query log, before:

    Index Scan using orders_created_at_idx on orders  (actual time=0.040..61.2 rows=48102)

Migration 0042 (merged Sep 14, "composite index for customer history") replaced `orders_created_at_idx` with `orders_customer_created_idx (customer_id, created_at)`. The planner cannot use the composite index for a range on created_at alone, because customer_id is the leading column. So every hour bucket is a full scan of 14M rows.

## plan

- migration 0043: re-add `orders_created_at_idx` on `created_at`. drafted, not merged, not run anywhere yet. CREATE INDEX CONCURRENTLY took about 6 min on the staging copy.
- after it lands: watch that night's run, expect about 12 min again.
- longer term: the 06:00 report build should fail when the rollup has not finished, instead of reading stale numbers. separate ticket.
- someday: pg 16 upgrade. unrelated, not now.
