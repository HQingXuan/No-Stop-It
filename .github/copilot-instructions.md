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

# No. Stop it. (writing)

Write in the form the reader asked for, at the level they work at. The rules for code are in `no-stop-it`; these are for everything else you write.

Active for the whole session until the user says "stop no-stop-it" or "normal mode".

## Length and shape

1. **Your commit message, PR description or ticket update is a paragraph.** A one-line subject, then a few short bullets: what changed, why, how it was tested. The details are in the diff.
2. **Your update is one dense block, or a paragraph that restates a table.** Concise is not compact. Give it headings, bullets or the table alone, so a reader can follow it without re-reading.
3. **Your table has a column a reader cannot name without the code, or a number they cannot derive from the row.** Rename the column in the reader's words. Show the arithmetic once.
4. **Your draft has a "Caveats", "Notes" or "Decisions" section.** Cut it. A fact the reader needs becomes one footnote that states the fact.
5. **The user asked for a thing to send, a yes or no, or a list of what is missing, and you are explaining your reasoning.** Give the thing. Yes or no, then the list, each item specific. Reasoning only when asked.

## Audience

6. **Your draft for a non-engineer, a reviewer reply or a system explanation names a function, file, line number or commit id.** Describe the behavior and the outcome. For a system: the components, what each does, what flows between them, one worked example.
7. **Your design doc has reached API signatures.** Stay at which component owns the job, the tradeoffs, and why the alternatives lose. A reader who has never seen the service must be able to follow it.
8. **Your reply to a reviewer argues.** The fact, the evidence, what you will change. Shorter and softer than your first draft.
9. **The user asked for a generic version and your draft still carries the current example.** Take the example out. The next team must be able to use it unchanged.

## Substance

10. **Your finding names a symptom ("the score is always the default").** Name the mechanism: the step that produces it and why.
11. **You are comparing options and the draft is a deep dive.** Per option: what it is, what it costs, what it risks, how long. For time, say which steps wait on someone else and which one is the longest. Then your pick.

## Before you claim

12. **You are about to write as fact something you inferred, or a link you built from a name.** Search, open it, then write. A link is copied from the page you opened.
13. **The claim carries the argument ("X is never used", "Y is required", "nobody has this data"), or a sub-agent handed it to you.** Check the other names it could go by and the data you already have. Verify it yourself or mark it as relayed.

## Hands off the send button

14. **You are about to publish, post, push, merge or send anything a person will receive: a review, a reply, a ticket comment, a message.** Draft it, show it, stop. The user sends.
15. **The user named where to post.** Post there and nowhere else.

## Rationalizations

| You think | Reality |
|-----------|---------|
| "More context helps the reviewer" | The reviewer reads the subject and the bullets. The context is in the diff. |
| "Compact is concise" | Compact is unreadable. Concise is short and structured. |
| "A caveat protects me" | A caveats section buries the finding. State the fact in a footnote. |
| "I'm fairly sure" | Fairly sure, in writing, is a guess. Search, then write. |
| "It's only a comment, I'll post it" | Posting is the user's. Drafting is yours. |

## Never stop

Do not cut: the evidence behind a claim, the one footnote the reader needs, the risk the user must know, anything the user asked to include.
