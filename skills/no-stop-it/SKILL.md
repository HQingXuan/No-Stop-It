---
name: no-stop-it
description: >
  Style rules for code an agent writes: the habits that make AI code easy to
  spot and tiresome to review (narrating comments, emoji, blanket try/except,
  silent fallbacks, leftover debug output, summary files nobody asked for),
  each with the sign you are about to do it and what to write instead. Use on
  any coding task, and when the user says "too many comments", "AI slop",
  "deslop", or "write it like a human".
license: MIT
---

# No. Stop it.

The codebase's own style comes first: if the file you are in already does something one way, do it that way. Otherwise, when you see a sign below, write the replacement instead.

Active for the whole session until the user says "stop no-stop-it" or "normal mode".

## Comments and docs

1. **Your comment says what the next line does.** Write no comment. Only comment a reason the code cannot show, in one line.
2. **You are about to write Args/Returns docs for a function whose name and signature already say it.** Write one line, or nothing.
3. **Your comment mentions the change itself** ("updated to", "now uses", "fixed", "new", "removed"). Describe the code as it is now. The change goes in the commit message.
4. **You are about to create a summary, notes or plan file nobody asked for** (`SUMMARY.md`, `IMPLEMENTATION.md`, `CHANGES.md`). Put it in your reply.
5. **You are about to type an emoji** in code, a comment, a log line, a commit message or a heading. Use the plain word.

## Errors

6. **You are about to wrap code in `try` that only logs, prints or re-raises a vaguer error.** Let it raise. Catch only the specific exception you can actually handle here.
7. **On failure, your code returns `0`, `None`, `""`, an empty list or a default, or quietly tries another way.** Raise, or return an error the caller has to look at. A fallback only when the user asked for one, named in your reply.
8. **You are about to check a value that cannot be missing, re-check input already validated, or compare to `True`.** Drop the check.

## Leftovers

9. **You added a `print`, `console.log` or debug log to see what was happening.** Remove it before you say done.
10. **You are about to leave `_old`, `_v2`, `_new`, `legacy`, commented-out code, a compatibility shim nobody needs, or a `TODO` with no owner or reason.** Delete the old version and update its callers. A `TODO` says what is missing and why.

## Names

11. **Your name is longer than four words, or a placeholder (`data`, `result`, `info`, `handler`, `manager`, `helper`).** Name what it holds in this codebase's words, as long as its neighbors' names.

## Rationalizations

| You think | Reality |
|-----------|---------|
| "Comments help the next reader" | The next reader reads the code. A comment that repeats it goes stale and misleads, agents included. |
| "Better safe: wrap it in try" | A caught-and-logged error is a bug that now hides. |
| "A default is friendlier than a crash" | A wrong number in production is worse than a crash in a test. |
| "A summary file helps the user" | The user asked for code. The summary goes in the reply. |
| "I'll clean the debug prints up later" | Later is this turn. |

## Never stop

Do not cut: comments a human needs (why a workaround exists, a non-obvious invariant, a link to the bug), docs the project requires on public APIs, error handling at trust boundaries and around I/O that can really fail, logging the project already does on purpose, anything the user asked for.
