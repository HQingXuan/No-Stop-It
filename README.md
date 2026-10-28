# No-Stop-It

*"No. Stop it."*

[Ponytail](https://github.com/DietrichGebert/ponytail) tells your agent what to do: the smallest change that works. No-Stop-It tells it what **not** to do: the moves that burn time and tokens without moving the task. Retrying the same failing command. Re-reading a file it just wrote. Rewriting a parser that already exists on GitHub. Bending a test until it goes green. Asking permission for an edit you already asked for.

Each rule is written as **a sign you can observe → stop → do this instead**, so the agent knows exactly when it applies and what replaces the forbidden move.

## Skills

| Skill | What it does |
|-------|--------------|
| `no-stop-it` | The stop list: 14 rules in four groups (scope, loops, fake progress, asking and waiting), a rationalization table, and a "never stop" list. |
| `no-stop-it-check` | Checks a diff for what the stop list forbids: silenced checks, skipped or weakened tests, stubs, new dependencies, unrelated edits. Lists findings, changes no code. |

## Install

Claude Code:

```
/plugin marketplace add HQingXuan/No-Stop-It
/plugin install no-stop-it@no-stop-it
```

Any other agent (Codex, Cursor, Gemini, ...): paste the body of [`skills/no-stop-it/SKILL.md`](skills/no-stop-it/SKILL.md) into your `AGENTS.md`, `CLAUDE.md` or rules file.

## Benchmark

`benchmarks/` runs six trap tasks in fresh repos, each as a headless `claude -p` session, with and without the `no-stop-it` rules (appended to the system prompt), and scores what the agent leaves behind. Each trap targets one rule group: a missing secret under "make it green" pressure, a test that cannot pass offline, a tempting FIXME next to the bug, a vague ask, a background job that died long ago, and a cleanup script that wipes the only copy of the user data.

```
python benchmarks/score.py --selftest      # check the scorers, free
python benchmarks/judge.py --selftest      # check the judge, a few cents
python benchmarks/run.py --runs 5          # 200 sessions, about $15
```

Four control tasks (`ctl-*`) have no trap: plain feature, fix and rename work. They show what the rules cost on normal tasks and whether they make the agent stop early. A blind judge (`benchmarks/judge.py`) scores how much of each control task was delivered, 0-3, and refuses to run unless it ranks every reference solution above a stub.

Results land in `benchmarks/results/<time>/summary.md`. Each task counts as one pair (pass rate, judged completeness, median cost, tokens, turns and seconds per arm). The summary reports, per task group, on how many tasks no-stop-it beat the baseline with a sign test, and the effect with a 95% bootstrap CI over tasks.

For cheating, `benchmarks/impossible.py` also pulls tasks from [ImpossibleBench](https://github.com/safety-research/impossiblebench): tests that contradict their spec, so passing one means the agent cheated.

## Why the rules look like this

Before writing, we compared how other projects shape agent behavior:

- **[Ponytail](https://github.com/DietrichGebert/ponytail):** a ranked ladder of positive choices ("take the first option that fully works") plus a short "never cut" list. Short, plain words, one file.
- **[andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills):** four principles, mostly "don't" bullets. Simple, but the bullets have no trigger, so the agent decides on its own when they apply.
- **[superpowers](https://github.com/obra/superpowers):** found in wording tests that prohibitions backfire on *output shape* ("don't narrate" produced more narration) but work on *discipline* (the agent knows the rule and skips it under pressure), especially with a rationalization table and red flags.
- **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) `constraint-driven-development`:** watches the diff for a lowered bar: new suppressions, skipped tests, stripped assertions.

So No-Stop-It:

1. Uses "don't" only for discipline failures, and says how replies should look as a positive recipe instead.
2. Puts an observable sign on every rule ("the same command failed twice with the same error"), not a judgment call ("don't loop too much").
3. Pairs every stop with the move that replaces it.
4. Has no "unless it matters" clauses. A real exception is its own rule (rule 14 for steps that cannot be undone).
5. Ends with what the list must never cut, so "don't waste effort" never turns into "skip the hard part".

## License

MIT
