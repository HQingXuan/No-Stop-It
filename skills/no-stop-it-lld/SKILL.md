---
name: no-stop-it-lld
description: >
  How to write a low-level design doc: the sections and what "done" looks
  like for each, how to show a schema, a sequence, a dependency call and a
  capacity number, and what to push back up to the high-level design. Use
  when drafting or reviewing a detailed design, implementation plan or tech
  spec that engineers will build from, and when the user asks whether
  something belongs in the HLD or the LLD.
license: MIT
---

# No. Stop it. (low-level design)

A low-level design tells the engineers who build it, and the teammates who review the code, how each component the HLD chose does its job. It passes when two engineers would write code that interoperates from it, and a code review can check the diff against it without re-deciding anything. Which components exist and who owns what was settled in the HLD (`no-stop-it-hld`, which also holds the boundary table).

## The boundary

Ask of every sentence: which pieces does it touch? The inside of one component: it belongs here. Several, or the choice between them: that is the HLD's decision; link it. The LLD stops at components, contracts, tables and sequences. The list of packages, classes and files you will edit is your build notes or the work breakdown, not the doc.

## Sections, in order

| Section | Done when |
|---|---|
| Scope | links the HLD and the decision this implements; says which work stream this LLD covers and where the others are |
| Sequence | one diagram per key flow; gates in the order the code checks them (kill switch, eligibility, experiment, lookup); a failure arrow on every external call |
| Data model | per table or entity: one annotated sample item; keys, indexes, TTL; item size from the measured distribution (p50, p99, max), not the mean alone; what is deliberately not stored and where it is recovered; migration and rollback |
| Interfaces | per operation: request, response, errors; for a changed contract, before and after and how clients move; a sketch of what the design depends on, never a pasted generated definition |
| Component behavior | per component: responsibility, inputs and outputs, the state it holds and the invariant that must hold, the one non-obvious step as ten lines of pseudocode or fewer with a worked example, each config flag and what it controls |
| Dependencies and failure | per call: timeout, retries, throttle behavior, what the caller returns on miss or error and the metric it emits, what the customer sees if it is down |
| Capacity and cost | the arithmetic shown once: count × item size = footprint, rate × price = $/month; measured p50 and p99 of the new call and where it was measured |
| Observability | per metric: unit, when it is emitted, what a reader does when it moves; per alarm: threshold and window; per log column: the key it joins on offline |
| Security and privacy | data classification, who reads it, retention and deletion, registrations the data needs |
| Test plan | one case per behavior; the seed data integration cases need; the latency check and the stage it runs in |
| Work breakdown | tasks of two weeks or less with dependencies and a confidence; tests and launch prep are tasks |
| Launch | per step: what turns on, how it turns off, how long that takes |

## Rules

1. **A paragraph argues which component should own the job, or reopens a storage or sync-versus-async choice.** That is the HLD's decision. Link it and describe how the chosen component does it. If the LLD proves the HLD wrong, change the HLD first, then this doc.
2. **Your schema is a column table or a pasted definition.** One annotated sample item, then two bullets: what is stored, and what is deliberately not stored and where it is recovered.
3. **A stored field has no reader on the serving path.** Drop it, or name the reader. If analysis needs it, recover it offline through a join on a key the log already carries.
4. **Your sequence diagram is the happy path, or the gates are in the wrong order.** Gates in the order the code checks them, a failure arrow on every external call, and what the response is on each failure.
5. **A dependency call has no timeout, retry or miss behavior.** Per call: timeout, retries, what the caller returns on miss and on error, the metric it emits, what the customer sees if it is down.
6. **A capacity or cost number appears without its arithmetic, or from the mean alone.** Show it once: count × size, rate × price. Use the measured distribution; the p99 and the max change the design, the mean does not.
7. **The metrics section is a list of names.** Per metric: unit, when emitted, what a reader does when it moves. Per alarm: threshold and window. Per log column: the join key.
8. **Your LLD lists the packages, classes and files to edit.** Move it to your build notes or the work breakdown. The doc names components, contracts, tables and sequences; code review checks the diff against those.
9. **There is pseudocode for a step a sentence describes, or none for the one step a sentence cannot.** Pseudocode only for the non-obvious step, ten lines or fewer, with one worked example from input to output.
10. **The test plan says "unit and integration tests".** One case per behavior, named; the seed rows the integration cases need; the latency comparison and the stage it runs in.
11. **The work breakdown is a total, or has a task over two weeks.** Tasks of two weeks or less, with dependencies and a confidence; tests and launch prep are tasks, not a buffer.
12. **The launch plan has no way back for a step.** Per step: what turns on, how it turns off (flag, dial, revert), how long that takes.

## Rationalizations

| You think | Reality |
|---|---|
| "The implementer will fill in the details" | Two implementers fill them in differently. The LLD is where they agree. |
| "The schema table is thorough" | A sample item is read in five seconds and shows the shape. The table hides the field nobody reads. |
| "Listing the files shows I understand the code" | A reviewer cannot judge a file list. They can judge a sequence and a contract. |
| "Mean item size is fine" | The p99 item decides the cache; the max decides the cap. |

## Never stop

Do not cut: the failure path of a call, the migration and rollback for a schema change, the one worked example, the join key in the logs, a security or privacy registration the data needs.
