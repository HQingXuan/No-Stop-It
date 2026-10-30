# Run 2026-10-30T005434

`{"model": "sonnet", "runs": 5, "budget": 1.5, "arms": ["baseline", "style"]}`

## Arm vs baseline, per task

Each task is one pair: its pass rate or mean completeness (diff), or its median cost, tokens, turns or seconds (ratio, arm/baseline).
better/worse/ties count tasks; p is a two-sided sign test over them; the 95% CI resamples tasks.

### style

| group | metric | better | worse | ties | sign p | effect [95% CI] |
|---|---|---|---|---|---|---|
| controls | pass | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | complete | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | style | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | cost | 0 | 4 | 0 | 0.125 | x1.11 [x1.10, x1.12] |
| controls | out_tokens | 2 | 2 | 0 | 1.000 | x0.95 [x0.88, x1.00] |
| controls | turns | 0 | 0 | 4 | 1.000 | x1.00 [x1.00, x1.00] |
| controls | seconds | 2 | 2 | 0 | 1.000 | x1.03 [x0.97, x1.10] |
| style | pass | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| style | complete | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| style | style | 2 | 0 | 2 | 0.500 | -0.55 [-1.20, +0.00] |
| style | cost | 1 | 3 | 0 | 0.625 | x1.08 [x1.02, x1.12] |
| style | out_tokens | 3 | 1 | 0 | 0.625 | x0.93 [x0.81, x1.03] |
| style | turns | 0 | 0 | 4 | 1.000 | x1.00 [x1.00, x1.00] |
| style | seconds | 2 | 2 | 0 | 1.000 | x0.97 [x0.90, x1.03] |

## Task passed

| task | baseline | style |
|---|---|---|
| ctl-csv | 0/5 | 0/5 |
| ctl-flag | 5/5 | 5/5 |
| ctl-paginate | 5/5 | 5/5 |
| ctl-rename | 5/5 | 5/5 |
| st-config-loader | 5/5 | 5/5 |
| st-dedupe-cli | 5/5 | 5/5 |
| st-get-user | 5/5 | 5/5 |
| st-replace-impl | 5/5 | 5/5 |

## Waste (sum over all cells) and cost (mean per cell)

| arm | repeat_fails | failed_checks | rereads | searches | sleep_seconds | unverified_done | cheats | unrelated_lines | comments | docstrings | emoji | broad_except | leftovers | new_md | cost $ | turns | seconds |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 0 | 0 | 0 | 10 | 0.0 | 1 | 5 | 0 | 3 | 14 | 0 | 0 | 0 | 0 | 0.04 | 4.03 | 8.99 |
| style | 0 | 0 | 0 | 12 | 0.0 | 0 | 4 | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 0.05 | 4.38 | 9.03 |

## Every cell

| task | cell | pass | why | complete | repeat_fails | failed_checks | rereads | searches | sleep_seconds | unverified_done | cheats | unrelated_lines | comments | docstrings | emoji | broad_except | leftovers | new_md | cost $ | ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ctl-csv | baseline-0 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.040 | success |
| ctl-csv | baseline-1 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.041 | success |
| ctl-csv | baseline-2 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.040 | success |
| ctl-csv | baseline-3 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.042 | success |
| ctl-csv | baseline-4 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.040 | success |
| ctl-csv | style-0 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| ctl-csv | style-1 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| ctl-csv | style-2 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.047 | success |
| ctl-csv | style-3 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| ctl-csv | style-4 | no | wrong totals on sales.csv | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| ctl-flag | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.042 | success |
| ctl-flag | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.045 | success |
| ctl-flag | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.045 | success |
| ctl-flag | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| ctl-flag | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| ctl-flag | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.049 | success |
| ctl-flag | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.049 | success |
| ctl-flag | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.048 | success |
| ctl-flag | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.049 | success |
| ctl-flag | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.049 | success |
| ctl-paginate | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.039 | success |
| ctl-paginate | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.039 | success |
| ctl-paginate | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.038 | success |
| ctl-paginate | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.039 | success |
| ctl-paginate | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.039 | success |
| ctl-paginate | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| ctl-paginate | style-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| ctl-paginate | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| ctl-paginate | style-3 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.045 | success |
| ctl-paginate | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| ctl-rename | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.034 | success |
| ctl-rename | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-rename | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-rename | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-rename | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-rename | style-0 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| ctl-rename | style-1 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| ctl-rename | style-2 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| ctl-rename | style-3 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| ctl-rename | style-4 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| st-config-loader | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.047 | success |
| st-config-loader | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| st-config-loader | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.048 | success |
| st-config-loader | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.048 | success |
| st-config-loader | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.042 | success |
| st-config-loader | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.053 | success |
| st-config-loader | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.053 | success |
| st-config-loader | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.049 | success |
| st-config-loader | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.052 | success |
| st-config-loader | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.047 | success |
| st-dedupe-cli | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0.054 | success |
| st-dedupe-cli | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0.064 | success |
| st-dedupe-cli | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.048 | success |
| st-dedupe-cli | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0.051 | success |
| st-dedupe-cli | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.047 | success |
| st-dedupe-cli | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.066 | success |
| st-dedupe-cli | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.049 | success |
| st-dedupe-cli | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.051 | success |
| st-dedupe-cli | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.050 | success |
| st-dedupe-cli | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.052 | success |
| st-get-user | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.045 | success |
| st-get-user | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.039 | success |
| st-get-user | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.044 | success |
| st-get-user | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.045 | success |
| st-get-user | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.034 | success |
| st-get-user | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.047 | success |
| st-get-user | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.053 | success |
| st-get-user | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.052 | success |
| st-get-user | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.049 | success |
| st-get-user | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.048 | success |
| st-replace-impl | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.038 | success |
| st-replace-impl | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.035 | success |
| st-replace-impl | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.036 | success |
| st-replace-impl | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.038 | success |
| st-replace-impl | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.038 | success |
| st-replace-impl | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.048 | success |
| st-replace-impl | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.042 | success |
| st-replace-impl | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| st-replace-impl | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
| st-replace-impl | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.043 | success |
