---
name: no-stop-it-docs
description: >
  Rules for any document a team reads and keeps: design docs, readiness docs,
  project plans, decks, wiki pages. What belongs in the body, an appendix or
  your own notes; tables versus paragraphs; keeping a doc true after edits;
  following the team's template and the previous doc; not growing a doc in
  review. Use when drafting or editing a document with sections, and when the
  user says "keep it high level", "hard to follow", "put that in the appendix"
  or "follow the format". For design content also load no-stop-it-hld or
  no-stop-it-lld.
license: MIT
---

# No. Stop it. (documents)

A document is read once by someone with less context than you, then skimmed by people looking for one number. Put what the reader decides first, what they might look up last, and what only you need nowhere in it. Rules for the sentences are in `no-stop-it-writing`; for design content, `no-stop-it-hld` and `no-stop-it-lld`.

## What belongs where

1. **Your summary carries the sizing numbers and the dates.** The summary is what changes for the reader and the recommendation, two paragraphs. Numbers go to a reference appendix with their sources, dates to the plan.
2. **Your background restates a meeting, a thread or another team's doc.** Link it. Repeat only the numbers this doc depends on, once, in the appendix.
3. **Your "how it works today" is a call tree or a list of classes.** One paragraph, one diagram with the changed parts marked, a link to the full walkthrough, and "skip this if you know the system".
4. **A section exists for you: build notes, scratch math, raw query output, the files you will touch.** Keep it in your own file. If a reader may want it, it is an appendix.

## Shape

5. **Your reasoning is a table, or your numbers are a paragraph.** Tables for numbers, dates, checklists and option-by-criterion grids. Paragraphs for reasoning. Bullets for pros and cons.
6. **A reader from another team said a section gave them a headache.** Before it, one paragraph that walks the flow in plain words with no component names. Then the questions you need from them, one line each, the must-answer ones dated.

## Keeping it true

7. **You changed a decision, a number or a section.** Sweep the doc: references to section numbers and "see below", the same number elsewhere, option letters in verdicts, requirement numbering, glossary terms still used, labels on what is the north star and what is this phase. Read it end to end once before anyone else does.
8. **Open Questions holds a question the thread already answered, or one with no owner.** Move the answer into the body and delete the question. Each remaining one has an owner and a date.

## Templates and predecessors

9. **The team has a template, or a previous doc of the same kind, and your section list differs.** Take their section list and diff yours against it before handing over. A section that does not apply says so in one line, with why.
10. **The doc covers a recurring event or a new phase.** This one first; the previous one's material in an appendix.
11. **You are editing a doc the user has already edited.** Add; do not touch their tables or wording. Say what you added and where.
12. **A review comment came in and you added a section.** Fix it in place. Act on comments that change a decision; list the rest as follow-ups. A doc that doubles during review is not a better doc.

## Rationalizations

| You think | Reality |
|---|---|
| "The background shows I did the research" | The link shows it. The restatement is what the reader skips. |
| "A table is more structured" | A table of prose is a paragraph with borders. |
| "I'll fix the cross-references at the end" | The end is when the reviewer opens it. |
| "Every comment deserves a paragraph" | Every comment deserves an answer. Most answers are a word change. |

## Never stop

Do not cut: the glossary term a non-team reader needs, the appendix the numbers live in, the user's own edits, a template section the team expects (mark it not applicable and say why).
