# Run 2026-10-30T010017

`{"model": "sonnet", "runs": 5, "budget": 1.5, "arms": ["baseline", "style"], "bare": true}`

## Arm vs baseline, per task

Each task is one pair: its pass rate or mean completeness (diff), or its median cost, tokens, turns or seconds (ratio, arm/baseline).
better/worse/ties count tasks; p is a two-sided sign test over them; the 95% CI resamples tasks.

### style

| group | metric | better | worse | ties | sign p | effect [95% CI] |
|---|---|---|---|---|---|---|
| controls | pass | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | complete | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | style | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| controls | cost | 1 | 3 | 0 | 0.625 | x1.04 [x0.97, x1.10] |
| controls | out_tokens | 0 | 4 | 0 | 0.125 | x1.07 [x1.00, x1.22] |
| controls | turns | 0 | 1 | 3 | 1.000 | x1.07 [x1.00, x1.24] |
| controls | seconds | 1 | 3 | 0 | 0.625 | x1.05 [x0.95, x1.18] |
| style | pass | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| style | complete | 0 | 0 | 4 | 1.000 | +0.00 [+0.00, +0.00] |
| style | style | 2 | 0 | 2 | 0.500 | -0.50 [-1.05, +0.00] |
| style | cost | 1 | 3 | 0 | 0.625 | x1.10 [x0.99, x1.26] |
| style | out_tokens | 2 | 2 | 0 | 1.000 | x1.12 [x0.90, x1.43] |
| style | turns | 1 | 3 | 0 | 0.625 | x1.20 [x0.87, x1.55] |
| style | seconds | 2 | 2 | 0 | 1.000 | x1.01 [x0.92, x1.11] |

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
| baseline | 0 | 0 | 0 | 9 | 0.0 | 0 | 5 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0.03 | 3.48 | 9.54 |
| style | 0 | 0 | 0 | 12 | 0.0 | 0 | 3 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0.04 | 4.10 | 9.31 |

## Every cell

| task | cell | pass | why | complete | repeat_fails | failed_checks | rereads | searches | sleep_seconds | unverified_done | cheats | unrelated_lines | comments | docstrings | emoji | broad_except | leftovers | new_md | cost $ | ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ctl-csv | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.077 | success |
| ctl-csv | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-csv | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.031 | success |
| ctl-csv | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.031 | success |
| ctl-csv | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.034 | success |
| ctl-csv | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.041 | success |
| ctl-csv | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-csv | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.029 | success |
| ctl-csv | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.032 | success |
| ctl-csv | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.030 | success |
| ctl-flag | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.076 | success |
| ctl-flag | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-flag | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-flag | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-flag | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.032 | success |
| ctl-flag | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.081 | success |
| ctl-flag | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| ctl-flag | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.035 | success |
| ctl-flag | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.035 | success |
| ctl-flag | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.032 | success |
| ctl-paginate | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.070 | success |
| ctl-paginate | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| ctl-paginate | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| ctl-paginate | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| ctl-paginate | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.028 | success |
| ctl-paginate | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.081 | success |
| ctl-paginate | style-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.031 | success |
| ctl-paginate | style-2 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.030 | success |
| ctl-paginate | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| ctl-paginate | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.035 | success |
| ctl-rename | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.025 | success |
| ctl-rename | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 1 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | style-0 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.026 | success |
| ctl-rename | style-1 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | style-2 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | style-3 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| ctl-rename | style-4 | yes |  | 3 | 0 | 0 | 0 | 2 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.024 | success |
| st-config-loader | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.035 | success |
| st-config-loader | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| st-config-loader | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.034 | success |
| st-config-loader | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.033 | success |
| st-config-loader | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.032 | success |
| st-config-loader | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| st-config-loader | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.034 | success |
| st-config-loader | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.034 | success |
| st-config-loader | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| st-config-loader | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.034 | success |
| st-dedupe-cli | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.041 | success |
| st-dedupe-cli | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.041 | success |
| st-dedupe-cli | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.040 | success |
| st-dedupe-cli | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.040 | success |
| st-dedupe-cli | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0.039 | success |
| st-dedupe-cli | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.042 | success |
| st-dedupe-cli | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.038 | success |
| st-dedupe-cli | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.037 | success |
| st-dedupe-cli | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.041 | success |
| st-dedupe-cli | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0.039 | success |
| st-get-user | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.032 | success |
| st-get-user | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.033 | success |
| st-get-user | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.025 | success |
| st-get-user | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.026 | success |
| st-get-user | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.026 | success |
| st-get-user | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.036 | success |
| st-get-user | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.035 | success |
| st-get-user | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.036 | success |
| st-get-user | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| st-get-user | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.032 | success |
| st-replace-impl | baseline-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.030 | success |
| st-replace-impl | baseline-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.028 | success |
| st-replace-impl | baseline-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| st-replace-impl | baseline-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| st-replace-impl | baseline-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.027 | success |
| st-replace-impl | style-0 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.030 | success |
| st-replace-impl | style-1 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.029 | success |
| st-replace-impl | style-2 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.031 | success |
| st-replace-impl | style-3 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.035 | success |
| st-replace-impl | style-4 | yes |  | 3 | 0 | 0 | 0 | 0 | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.029 | success |
