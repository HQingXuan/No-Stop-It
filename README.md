<h1 align="center">No-Stop-It</h1>

<p align="center"><em>"No. Stop it." Rules that keep your coding agent from writing code that reads like AI code.</em></p>

<p align="center">
  <img src="https://img.shields.io/github/stars/HQingXuan/No-Stop-It?style=flat-square&color=111111&label=stars" alt="Stars">
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex%20%C2%B7%20Copilot%20%C2%B7%20Gemini-111111?style=flat-square" alt="Works with Claude Code, Cursor, Codex, Copilot, Gemini">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license">
</p>

<p align="center"><img src="assets/before-after.png" alt="The same dedupe CLI written by Opus without and with No-Stop-It: 57 lines with a six-line docstring, versus 34 lines that pass the same checks" width="900"></p>

<p align="center"><sub>Inspired by <a href="https://github.com/DietrichGebert/ponytail">Ponytail</a>.</sub></p>

<br>

## What it stops

AI code is easy to spot, and tiresome to review, because of a handful of habits:

- Comments that read the code aloud.
- Args/Returns blocks on a two-line function.
- Emoji in log lines and headings.
- A `try` that only logs.
- A fallback that returns `0` and hides the bug.
- `parse_old` left next to `parse`.
- A `SUMMARY.md` nobody asked for.

No-Stop-It gives your agent one rule for each. Every rule is **a sign you can observe → what to write instead**, so the agent knows exactly when it applies and has a replacement, not only a ban.

<br>

## The rules

One skill, `no-stop-it`, with 11 rules in four groups:

| Group | Stops |
|-------|-------|
| **Comments and docs** | narrating comments, boilerplate docstrings, comments about the edit itself, summary files, emoji |
| **Errors** | `try` that only logs, silent fallbacks, checks on values that cannot be missing |
| **Leftovers** | debug prints, `_old` / `_v2` copies, commented-out code, TODOs with no reason |
| **Names** | names longer than four words, or placeholders like `data` and `helper` |

The codebase's own style always comes first. A closing "never stop" list keeps the comments, docs and error handling that matter: why a workaround exists, public API docs the project requires, handling at trust boundaries.

Read the full list: [`skills/no-stop-it/SKILL.md`](skills/no-stop-it/SKILL.md).

<br>

## Install

### Claude Code

Send these as two separate prompts:

```
/plugin marketplace add HQingXuan/No-Stop-It
```

```
/plugin install no-stop-it@no-stop-it
```

### Cursor

```
mkdir -p .cursor/rules && curl -fsSL https://raw.githubusercontent.com/HQingXuan/No-Stop-It/main/.cursor/rules/no-stop-it.mdc -o .cursor/rules/no-stop-it.mdc
```

### Codex, and any agent that reads `AGENTS.md`

```
curl -fsSL https://raw.githubusercontent.com/HQingXuan/No-Stop-It/main/AGENTS.md >> AGENTS.md
```

### GitHub Copilot

```
mkdir -p .github && curl -fsSL https://raw.githubusercontent.com/HQingXuan/No-Stop-It/main/.github/copilot-instructions.md >> .github/copilot-instructions.md
```

### Gemini CLI

```
gemini extensions install https://github.com/HQingXuan/No-Stop-It
```

All of these are copies of the same skill, kept in sync by `python scripts/sync_rules.py`.

<br>

## Benchmark

### Results

8 coding tasks, 5 runs each, with and without the rules:

| Setup | Docstrings | Narrating comments | Added lines | Cost |
|---|---|---|---|---|
| Sonnet | 14 → 5 | 3 → 1 | 822 → 707 | +11% |
| Sonnet, one-line system prompt | 13 → 3 | 0 → 0 | 807 → 706 | +3% |
| Opus | 15 → 5 | 0 → 0 | 1055 → 864 | +8% |

- Pass rate and judged completeness were the same in every setup.
- Opus wrote 6 comments in both arms, all of them "why" comments, which the rules keep.
- Emoji, broad `except`, leftovers and new `.md` files were 0 in both arms on these tasks.

### What it measures

Each task runs in a fresh repo as a headless `claude -p` session. For every run, the benchmark:

1. Counts the style habits in the diff: narrating comments, docstrings, emoji, broad `except`, leftovers, new `.md` files.
2. Checks that the task works, including a probe that a missing file or a broken database raises instead of falling back silently.
3. Asks a blind judge how much of the task was delivered, 0 to 3, so rules that make the agent do less would show up.

The summary reports, per task group, on how many tasks the rules beat the baseline (sign test) and by how much (95% bootstrap CI).

### Run it

```
python benchmarks/score.py --selftest                    # check the scorers, free
python benchmarks/judge.py --selftest                    # check the judge, a few cents
python benchmarks/run.py --runs 5                        # every task, both arms
python benchmarks/run.py --runs 5 --model opus --bare    # another model, a one-line system prompt
```

Results land in `benchmarks/results/<time>/summary.md`.

<br>

## Why the rules look like this

- **Every rule names its replacement.** [superpowers](https://github.com/obra/superpowers) found that bare prohibitions backfire on output shape: "don't narrate" produced more narration.
- **Every rule has an observable sign.** "Your comment says what the next line does", not "don't over-comment".
- **The codebase's style wins.** Said once at the top, instead of "unless" clauses on every rule.
- **A "never stop" list.** So "fewer comments" never turns into "no why".

The habits come from [deslop](https://github.com/dabit3/deslop), [beagle](https://skills.cat/skills/existential-birds/beagle/llm-artifacts-detection), and user complaints about [emoji in headings](https://claudeissues.com/issue/3567-markdown-header-emoji-removal-prevent-emoji-in-documentation-sections), [unrequested .md files](https://forum.cursor.com/t/claude-models-with-cursor-constantly-wastefully-generate-md-docs-files-violating-rules/147673) and [silent fallbacks](https://hyperdev.matsuoka.com/p/bad-habit-of-agentic-coders-part).

An earlier version of No-Stop-It was an engineering stop list (retry loops, polling, bending tests). Its benchmark showed current models already avoid most of those moves, so this one replaced it. It is still in the git history.

<br>

## License

MIT
