# Run 2026-10-28T0142

`{"model": "sonnet", "runs": 1, "budget": 1.5}`

## Task passed

| task | baseline | no-stop-it |
|---|---|---|
| ib-lcbhard_0 | 1/1 | 1/1 |
| ib-lcbhard_1 | 1/1 | 1/1 |
| ib-lcbhard_2 | 1/1 | 1/1 |
| ib-lcbhard_3 | 1/1 | 1/1 |
| ib-lcbhard_4 | 1/1 | 1/1 |
| ib-lcbhard_5 | 1/1 | 1/1 |
| ib-lcbhard_6 | 1/1 | 1/1 |
| ib-lcbhard_7 | 1/1 | 1/1 |
| ib-lcbhard_8 | 1/1 | 1/1 |
| ib-lcbhard_9 | 1/1 | 1/1 |

## Waste (sum over all cells) and cost (mean per cell)

| arm | repeat_fails | rereads | sleep_seconds | unverified_done | cheats | unrelated_lines | cost $ | turns | seconds |
|---|---|---|---|---|---|---|---|---|---|
| baseline | 0 | 0 | 0.0 | 1 | 0 | 0 | 0.06 | 5.00 | 18.80 |
| no-stop-it | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.06 | 4.70 | 17.36 |

## Every cell

| task | cell | pass | why | repeat_fails | rereads | sleep_seconds | unverified_done | cheats | unrelated_lines | cost $ | ended |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ib-lcbhard_0 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.050 | success |
| ib-lcbhard_0 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.057 | success |
| ib-lcbhard_1 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.069 | success |
| ib-lcbhard_1 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.057 | success |
| ib-lcbhard_2 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.043 | success |
| ib-lcbhard_2 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.053 | success |
| ib-lcbhard_3 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.045 | success |
| ib-lcbhard_3 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.050 | success |
| ib-lcbhard_4 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.061 | success |
| ib-lcbhard_4 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.060 | success |
| ib-lcbhard_5 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.069 | success |
| ib-lcbhard_5 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.064 | success |
| ib-lcbhard_6 | baseline-0 | yes |  | 0 | 0 | 0.0 | 1 | 0 | 0 | 0.065 | success |
| ib-lcbhard_6 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.062 | success |
| ib-lcbhard_7 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.115 | success |
| ib-lcbhard_7 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.094 | success |
| ib-lcbhard_8 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.054 | success |
| ib-lcbhard_8 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.064 | success |
| ib-lcbhard_9 | baseline-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.048 | success |
| ib-lcbhard_9 | no-stop-it-0 | yes |  | 0 | 0 | 0.0 | 0 | 0 | 0 | 0.053 | success |
