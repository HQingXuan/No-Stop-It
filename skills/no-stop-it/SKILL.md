---
name: no-stop-it
description: >
  Style rules for code an agent writes: the habits that make AI code easy to
  spot and tiresome to review (narrating comments, boilerplate docstrings,
  blanket try/except, silent fallbacks, placeholder names, tests that cannot
  fail), each with the sign you are about to do it and what to write instead.
  The mechanical half (emoji, leftovers, notes files, stale mentions, version
  copies, mock-only tests) is enforced by the `nostopit` checker, not by this
  file. Use on any coding task, and when the user says "too many comments",
  "AI slop", "deslop", or "write it like a human".
license: MIT
---

# No. Stop it.

The codebase's own style comes first: if the file you are in already does something one way, do it that way. Otherwise, when you see a sign below, write the replacement instead.

Active for the whole session until the user says "stop no-stop-it" or "normal mode".

## Comments and docs

1. **Your comment says what the next line does.** Write no comment. Only comment a reason the code cannot show, in one line.
2. **You are about to write Args/Returns docs for a function whose name and signature already say it.** Write one line, or nothing.
3. **Your comment mentions the change itself** ("updated to", "now uses", "fixed", "new", "removed"), **or cites the ticket, requirement or review round that asked for it.** Describe the code as it is now. The change and its ticket go in the commit message.

## Errors

4. **You are about to wrap code in `try` that only logs, prints or re-raises a vaguer error.** Let it raise. Catch only the specific exception you can actually handle here.
5. **On failure, your code returns `0`, `None`, `""`, an empty list or a default, or quietly tries another way.** Raise, or return an error the caller has to look at. A fallback only when the user asked for one, named in your reply.
6. **You are about to check a value that cannot be missing, re-check input already validated, or compare to `True`.** Drop the check.

## Leftovers and names

7. **You added a `print`, `console.log` or debug log to see what was happening.** Remove it before you say done.
8. **Your name is a placeholder (`data`, `result`, `info`, `handler`, `manager`, `helper`).** Name what it holds in this codebase's words.

## Tests

9. **Your test computes its expected value with the code under test, or only checks that a call happened.** Write the expected value by hand and assert the result. If flipping a condition in the source would not fail the test, it is not a test.

## The diff

10. **Your diff mixes a rename or refactor with the behavior change.** Put the refactor and the behavior change in separate commits.

## Checked by the tool, not by you

The `nostopit` checker runs from the agent hook, pre-commit and CI and reports these with the fix in the message: emoji, notes files nobody asked for, comments that cite a review or a ticket, commented-out code, `_old`/`_v2` names, TODOs with no reason, names over four words, tests with no assertion or only mock assertions, names removed but still mentioned elsewhere, a version changed in one file and not its copies, new dependencies, diffs past 400 lines. When it fires, fix the cause. `# nostopit: allow <rule>` exists for the real exception and is counted in the report; a reviewer reads that count.

## Rationalizations

| You think | Reality |
|-----------|---------|
| "Comments help the next reader" | The next reader reads the code. A comment that repeats it goes stale and misleads, agents included. |
| "Better safe: wrap it in try" | A caught-and-logged error is a bug that now hides. |
| "A default is friendlier than a crash" | A wrong number in production is worse than a crash in a test. |
| "I'll clean the debug prints up later" | Later is this turn. |
| "The test proves the call happened" | It proves the mock works. Flip the condition; nothing fails. |
| "The checker is wrong here, I'll allow it" | Sometimes. The allow count is on the report the reviewer reads. |

## Never stop

Do not cut: comments a human needs (why a workaround exists, a non-obvious invariant, a link to the bug), docs the project requires on public APIs, error handling at trust boundaries and around I/O that can really fail, logging the project already does on purpose, anything the user asked for.
