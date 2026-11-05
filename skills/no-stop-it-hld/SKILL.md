---
name: no-stop-it-hld
description: >
  How to write a high-level design doc: who reads it, the sections and what
  "done" looks like for each, how to present decisions, and where it stops
  and the low-level design begins. Use when drafting or reviewing a design
  doc, architecture proposal, RFC or one-pager that other people must agree
  to, and when the user asks whether something belongs in the HLD or the LLD.
license: MIT
---

# No. Stop it. (high-level design)

A high-level design is a decision document. Its reader is anyone who must agree to the approach: product, science, other teams, senior reviewers who have never opened the code. It passes when such a reader can say what will be built, why this shape and not the others, what it costs, and what takes it down. It decides between components; the low-level design (`no-stop-it-lld`) decides inside one.

## The boundary

Ask of every sentence: which pieces does it touch? Several, or the choice between them: HLD. The inside of one: LLD. Deleting an HLD sentence would change which option a reviewer picks; deleting an LLD sentence would change what an engineer types.

| | High-level design | Low-level design |
|---|---|---|
| Decides | which component owns the job, store type, sync or async, what is out of scope | keys, fields, request and response shapes, call order, timeouts, retries, flags |
| Names | services, stores, teams, flows | tables, operations, classes, config keys, metric names |
| Numbers | order of magnitude with a source: TPS, data size, latency budget, $/month, engineer-weeks per work area | the arithmetic: item size × count, reads × price, measured p99 of the new call |
| Diagram | context or container: boxes are systems and stores, changed ones marked | sequence, entity, component: boxes are operations and classes, gates in code order |
| Reader | anyone who must agree to the approach | whoever builds it or reviews the code |
| Gate | should we build it, and this way? | will the code be right? |
| Changes when | requirements or tradeoffs change | the code changes |

The line moves with scale: splitting a "service" that is one class is LLD; splitting one that deploys on its own is HLD. One component and under about ten engineer-weeks: one doc, an HLD section then an LLD section. Several components, or a doc reviewers cannot read in one sitting: one HLD, one LLD per work stream.

## Sections, in order

| Section | Done when |
|---|---|
| Summary | opens with the problem in one sentence and what the reader decides after reading; then two paragraphs: what changes for the customer, the recommended shape; no numbers, no dates |
| Glossary | every term a reader from another team would stumble on, one line each |
| Requirements and scope | functional ones as user stories; each non-functional one has today's value, the limit and a source; out of scope says why; each assumption says how it is de-risked |
| Current state | one paragraph, one diagram with the changed parts marked, a link to the full walkthrough; what the current system does well and what it cannot do |
| North star | where the architecture is headed; how much of this design is a step toward it and how much is throwaway |
| Architecture | one diagram: components, who owns each, what flows between them, new or changed parts marked |
| Decisions | one question per choice point, in request order; two or three options each; the recommended one marked; the verdict names the fallback and when to take it; one-way doors flagged |
| Non-functional | scale now, at peak and in a year; latency budget; the dependency that can take it down and the known-good state to flip to; $/month; data classification |
| Rollout or experiment | how it turns on and off and how long that takes; for an experiment: arms, who is eligible and what triggers it, primary and guardrail metrics, the success bar, duration |
| Effort | per work area, low confidence, with how each estimate was made, which steps wait on another team, and the long pole |
| Open questions | each with an owner and a date |
| Appendix | reference numbers with sources; options discounted early, each with its one reason |

## Rules

1. **The doc opens with the solution and describes only it.** Open with the problem in one sentence and what the reader decides after reading. A reviewer chooses between options, not between your idea and nothing.
2. **Your alternatives are whole designs listed side by side.** Split them into decisions: one question per choice point, in the order a request meets them. Options lettered; each: how it works, pros, cons; one marked recommended; a one-line verdict with the fallback and when to take it. Same criteria for every option.
3. **An option's cons say "more complex", "not ideal" or "harder to maintain".** Name the thing that kills it: the job another team's loader rewrites, the kill switch it couples to, the row that does not exist. A pro is not another option's con. Every option has a con; if one has none, look harder.
4. **The option you did not pick has no cost.** Size it: days on your side, what the other team keeps doing, what is reused and what is thrown away. It is the fast-follow someone will ask about.
5. **You are replacing or improving a system without saying what is wrong with it or where the architecture is headed.** The current system is the bar: what it does well, what it cannot do, why improving it loses. Then the north star: the step this takes toward it, and what is throwaway.
6. **Pages on a new abstraction, or flexibility nobody asked for.** Back to the problem at hand. Flexibility earns a sentence when the second use case is named and dated.
7. **A paragraph has reached table keys, field names, request shapes or class names.** That is the LLD. Here: which component owns the job, what it reads and writes, the latency budget it gets. Link the LLD.
8. **The architecture diagram shows classes, flags or experiment arms.** Components and flows only, changed parts marked, in the team's diagram style. A reader from another team must read it unaided.
9. **A non-functional requirement is a word: "scalable", "low latency", "secure".** Today's value, the limit, and where the number came from: "p99 20 ms today, alarm at 85 ms, budget +2 ms on the new path", with the dashboard link.
10. **Nothing says what takes the system down.** One failure paragraph: the dependency whose outage reaches the customer, the switch that turns the feature off and how long that takes, the state you fall back to.
11. **The estimate is one total.** Per work area, with how you got it (a similar project, a heuristic, a quote from the owning team), which steps wait on approvals or another team, and the long pole. No project plan in the HLD.
12. **A decision came up in review and you settled it in chat.** Add it to the doc as the next decision, in the same shape, before the next reader opens it.

## Rationalizations

| You think | Reality |
|---|---|
| "The reviewers know the system" | The one who blocks you does not. |
| "The pros and cons are in my head" | Unwritten options read as "I only considered mine." |
| "Detail shows rigor" | Detail past the decision hides it. Rigor is the number with its source. |
| "The new system is obviously better" | The old one is the bar. Say where it falls short. |

## Never stop

Do not cut: the recommended option's biggest con, the north star paragraph, a one-way door, the source behind a number, the glossary term a non-team reader needs.
