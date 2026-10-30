---
name: no-stop-it-writing
description: >
  Rules for what an agent writes to people: chat replies, commit messages,
  PR descriptions, review replies, ticket comments, design docs and slides.
  Each rule is the sign you are about to write something the reader will skim
  past or push back on, and what to write instead. Use whenever another person
  will read the output, and when the user says "too long", "too compact",
  "hard to follow", "just tell me", "keep it high level" or "be concise".
license: MIT
---

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
12. **Your description claims a change the diff does not contain, or skips one it does.** Describe the diff: every change in it, and only those. A commit subject or a plan is not the diff.
13. **The request can be read two ways and you picked one without saying.** Say which reading you took, in one line at the top. If the wrong reading would be expensive to redo, ask instead.

## Before you claim

14. **You are describing your own checking with an adverb or a grade: "thoroughly tested", "carefully reviewed", "fully verified".** Name the acts: ran X, read Y, did not run Z.
15. **You are about to write as fact something you inferred, or a link you built from a name.** Search, open it, then write. A link is copied from the page you opened.
16. **The claim carries the argument ("X is never used", "Y is required", "nobody has this data"), or a sub-agent handed it to you.** Check the other names it could go by and the data you already have. Verify it yourself or mark it as relayed.

## Hands off the send button

17. **You are about to publish, post, push, merge or send anything a person will receive: a review, a reply, a ticket comment, a message.** Draft it, show it, stop. The user sends.
18. **The user named where to post.** Post there and nowhere else.

## Rationalizations

| You think | Reality |
|-----------|---------|
| "More context helps the reviewer" | The reviewer reads the subject and the bullets. The context is in the diff. |
| "Compact is concise" | Compact is unreadable. Concise is short and structured. |
| "A caveat protects me" | A caveats section buries the finding. State the fact in a footnote. |
| "I'm fairly sure" | Fairly sure, in writing, is a guess. Search, then write. |
| "'Thoroughly tested' covers it" | It covers nothing. Which tests ran, which did not, is the evidence. |
| "It's only a comment, I'll post it" | Posting is the user's. Drafting is yours. |

## Never stop

Do not cut: the evidence behind a claim, the one footnote the reader needs, the risk the user must know, anything the user asked to include.
