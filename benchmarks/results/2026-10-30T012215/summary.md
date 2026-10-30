# Run 2026-10-30T012215

`{"model": "opus", "runs": 5, "budget": 1.5, "arms": ["baseline", "style"], "bare": false}`

## Arm vs baseline, per task

Each task is one pair: its pass rate or mean completeness (diff), or its median cost, tokens, turns or seconds (ratio, arm/baseline).
better/worse/ties count tasks; p is a two-sided sign test over them; the 95% CI resamples tasks.

### style

| group | metric | better | worse | ties | sign p | effect [95% CI] |
|---|---|---|---|---|---|---|
| controls | pass | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | complete | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | style | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | cost | 1 | 3 | 0 | 0.625 | x1.06 [x1.02, x1.11] |
| controls | out_tokens | 3 | 1 | 0 | 0.625 | x0.91 [x0.80, x1.03] |
| controls | turns | 1 | 0 | 3 | 1.000 | x0.93 [x0.81, x1.00] |
| controls | seconds | 3 | 1 | 0 | 0.625 | x0.90 [x0.81, x1.02] |
| style | pass | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| style | complete | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| style | style | 2 | 0 | 2 | 0.500 | -0.50 [-1.00, +0.00] |
| style | cost | 1 | 3 | 0 | 0.625 | x1.06 [x1.02, x1.11] |
| style | out_tokens | 3 | 1 | 0 | 0.625 | x0.90 [x0.84, x0.98] |
| style | turns | 0 | 2 | 2 | 0.500 | x1.19 [x1.00, x1.47] |
| style | seconds | 3 | 1 | 0 | 0.625 | x0.92 [x0.84, x1.02] |

## Task passed

| task | baseline | style |
|---|---|---|
| ctl-csv | 5/5 | 5/5 |
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
| baseline | 0 | 2 | 0 | 10 | 0.0 | 0 | 5 | 0 | 6 | 15 | 0 | 0 | 0 | 0 | 0.09 | 3.62 | 11.75 |
| style | 0 | 1 | 0 | 6 | 0.0 | 1 | 4 | 0 | 6 | 5 | 0 | 0 | 0 | 0 | 0.10 | 3.88 | 11.04 |

## Every cell

| task | cell | pass | why | complete | repeat_fails | failed_checks | rereads | searches | sleep_seconds | unverified_done | cheats | unrelated_lines | comments | docstrings | emoji | broad_except | leftovers | new_md | cost $ | ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ctl-csv | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 | success |
| ctl-csv | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.087 | success |
| ctl-csv | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.076 | success |
| ctl-csv | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 | success |
| ctl-csv | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.087 | success |
| ctl-csv | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.088 | success |
| ctl-csv | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.090 | success |
| ctl-csv | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.088 | success |
| ctl-csv | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.088 | success |
| ctl-csv | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.087 | success |
| ctl-flag | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.090 | success |
| ctl-flag | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.089 | success |
| ctl-flag | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.099 | success |
| ctl-flag | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.095 | success |
| ctl-flag | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.093 | success |
| ctl-flag | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.113 | success |
| ctl-flag | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.105 | success |
| ctl-flag | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.105 | success |
| ctl-flag | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.105 | success |
| ctl-flag | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.098 | success |
| ctl-paginate | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 | success |
| ctl-paginate | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.091 | success |
| ctl-paginate | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.088 | success |
| ctl-paginate | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.089 | success |
| ctl-paginate | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.092 | success |
| ctl-paginate | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.096 | success |
| ctl-paginate | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.105 | success |
| ctl-paginate | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.097 | success |
| ctl-paginate | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.091 | success |
| ctl-paginate | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.097 | success |
| ctl-rename | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.081 | success |
| ctl-rename | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.071 | success |
| ctl-rename | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.081 | success |
| ctl-rename | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.079 | success |
| ctl-rename | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.079 | success |
| ctl-rename | style-0 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.078 | success |
| ctl-rename | style-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.079 | success |
| ctl-rename | style-2 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.079 | success |
| ctl-rename | style-3 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.079 | success |
| ctl-rename | style-4 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.090 | success |
| st-config-loader | baseline-0 | yes |  | 3 | 0 | 1 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.101 | success |
| st-config-loader | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.100 | success |
| st-config-loader | baseline-2 | yes |  | 3 | 0 | 1 | 0 | 0 | 0.0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0.120 | success |
| st-config-loader | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.106 | success |
| st-config-loader | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.101 | success |
| st-config-loader | style-0 | yes |  | 3 | 0 | 1 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.106 | success |
| st-config-loader | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.099 | success |
| st-config-loader | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.113 | success |
| st-config-loader | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.112 | success |
| st-config-loader | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0.100 | success |
| st-dedupe-cli | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.120 | success |
| st-dedupe-cli | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.147 | success |
| st-dedupe-cli | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.124 | success |
| st-dedupe-cli | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.134 | success |
| st-dedupe-cli | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.135 | success |
| st-dedupe-cli | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0.161 | success |
| st-dedupe-cli | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.134 | success |
| st-dedupe-cli | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.117 | success |
| st-dedupe-cli | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.124 | success |
| st-dedupe-cli | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.152 | success |
| st-get-user | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.080 | success |
| st-get-user | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.095 | success |
| st-get-user | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.090 | success |
| st-get-user | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.092 | success |
| st-get-user | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.076 | success |
| st-get-user | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.097 | success |
| st-get-user | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.101 | success |
| st-get-user | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.103 | success |
| st-get-user | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.095 | success |
| st-get-user | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.098 | success |
| st-replace-impl | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.083 | success |
| st-replace-impl | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.083 | success |
| st-replace-impl | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.081 | success |
| st-replace-impl | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.088 | success |
| st-replace-impl | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.084 | success |
| st-replace-impl | style-0 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.096 | success |
| st-replace-impl | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.094 | success |
| st-replace-impl | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.107 | success |
| st-replace-impl | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.090 | success |
| st-replace-impl | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.089 | success |
