---
name: no-stop-it-check
description: >
  Checks a finished change for the no-stop-it violations a diff can show:
  silenced checks, weakened or skipped tests, stubs passed off as done, new
  dependencies, and edits outside the task. Use before a commit or PR, after
  an autonomous run, or for "check the agent's work", "did it cheat",
  /no-stop-it-check.
---

Check a change for wasted or faked work. Lists findings, changes no code.

## 1. Get the change

What the user names: a branch, a PR, a commit, files. Nothing named: the uncommitted changes, or the last commit if there are none. Read the task it was meant to do (the prompt, the issue, the PR text).

## 2. Scan the added lines

```sh
git diff <base> -U0 | grep -E '^\+.*(@ts-(ignore|nocheck|expect-error)|eslint-disable|# *type: *ignore|# *noqa|\|\| *true|\.skip\(|\.only\(|xit\(|xdescribe\(|@pytest\.mark\.skip|t\.Skip\(|TODO|FIXME|NotImplemented|catch *(\([^)]*\))? *\{ *\})'
```

Then read the diff for what grep cannot see:

- an assertion made weaker (exact value turned into `toBeTruthy`, a range widened, a check deleted)
- a test file deleted or a test case removed
- the code under test mocked out by its own test
- a new entry in the dependency manifest
- a file or line the task does not need

## 3. Confirm each one

A suppression with a comment that names a real cause (a known upstream bug, a generated file) is a decision, not a finding. No concrete case, no finding.

## 4. Output

Number the findings so the user can say "fix 2". Each one: **what** (`file:line`), **why it is a problem**, **the fix** in one line.

End with `Verdict: clean.` or `Verdict: fix 1 and 3 first.` and one line on what you did not check.
