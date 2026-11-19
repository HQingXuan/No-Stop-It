# Decisions

## D-001: A stdlib-only checker over a ruff or ESLint plugin
- **Status:** Active
- **Origin:** new
- **Where:** nostopit/checks.py, nostopit/cli.py, pyproject.toml
- **Context:** The checks must run from an agent hook in any repository, in any language, on a machine with Python and git and nothing else installed.
- **Options:**
  - ruff/ESLint plugins: precise ASTs, but one plugin per language and a toolchain the target repo may not have.
  - A model-judged check: catches judgment habits, but costs tokens per edit and is the thing we are trying not to rely on.
  - Stdlib Python over the unified diff, Python `ast` where a file is Python: runs anywhere, regex elsewhere.
- **Choice:** Stdlib Python over the diff.
- **Trade-off:** AST-level checks (tests, commented-out code) are Python-only; other languages get regexes. The README points at ruff/ESLint rules for what they already own.
- **Revisit when:** a second language needs the test checks, or the regexes produce a false positive a user hits more than once.

## D-002: Hooks talk through exit code 2 and stderr, not JSON hook output
- **Status:** Active
- **Origin:** new
- **Where:** nostopit/cli.py (`hook`), hooks/claude-code.json, hooks/kiro-agent.json
- **Context:** Claude Code and Kiro CLI both read exit 2 as "block, show stderr to the model". Claude Code also accepts JSON on stdout with `additionalContext` or `decision: block`; Kiro's JSON contract was not verifiable from here.
- **Options:**
  - JSON output: non-blocking context on PostToolUse, but one shape per runtime.
  - Exit 2 and stderr: one code path for both runtimes; on PostToolUse it reads as an error even though nothing is blocked.
- **Choice:** Exit 2 and stderr.
- **Trade-off:** PostToolUse findings arrive as a blocking error message. The Stop hook fails only on `error` findings and honors `stop_hook_active`, so warnings cannot loop the agent.
- **Revisit when:** Kiro documents its JSON hook output, or a user reports the agent treating warnings as blockers.

## D-003: The send gate can be overridden by `NOSTOPIT_ALLOW_SEND=1` in the command
- **Status:** Active
- **Origin:** new
- **Where:** nostopit/cli.py (`send_block`)
- **Context:** A hook cannot know whether the user asked for the push. Writing rule 17 says "when they asked, do it".
- **Options:**
  - Hard deny, user runs every send: safe, but breaks every "create a PR for me" request.
  - Allow-file written by the user: an agent with a shell can write it too, and it is invisible in the transcript.
  - Env var in the command itself: the agent can set it, but the override is in the transcript and in any audit log of commands.
- **Choice:** Env var in the command, with the message telling the agent to say so in its reply.
- **Trade-off:** Not a hard gate against an agent with a shell. It makes sending a deliberate, visible act.
- **Revisit when:** a runtime offers a user-only approval channel the hook can call.

## D-004: Stale mentions only for removed definitions, flags and files, not every removed token
- **Status:** Active
- **Origin:** new
- **Where:** nostopit/checks.py (`stale_mentions`, `identifier_shaped`)
- **Context:** Grepping every removed word floods the report: removed prose words appear everywhere. deslop 2's finding was about removed flags, files and env vars.
- **Options:**
  - Every removed token: catches removed usages too, at a false-positive rate that would make the agent ignore the rule.
  - Removed definitions (`def`, `class`, `const`, UPPER_CASE, module-level assignment), quoted `--flags` in argparse-like calls, deleted file stems, all identifier-shaped (underscore, camel hump or dash) and absent from the added lines.
- **Choice:** Definitions, flags and files, identifier-shaped only.
- **Trade-off:** A renamed single-word function (`parse` to `load`) is not caught. First dogfood run already removed one false positive (`--git` inside a regex string).
- **Revisit when:** the check has run on 50 real PRs and the false-positive rate is known.

## D-005: One implementation for the benchmark counters and the checker
- **Status:** Active
- **Origin:** follows benchmarks/score.py
- **Where:** nostopit/checks.py (`STYLE`, `PROSE`, `style`, `prose`), benchmarks/score.py
- **Context:** The scorer already had the regexes. A second copy in the checker would drift, as the earlier comment-regex bug showed.
- **Options:**
  - Copy the regexes into the checker: no import path games, two copies to keep equal.
  - Scorer imports from the checker: one copy; `score.py` puts the repo root on `sys.path`.
- **Choice:** Scorer imports from the checker.
- **Trade-off:** The benchmark measures exactly what the hook enforces, which is also what makes a `hooks` arm a fair experiment.
- **Revisit when:** the checker needs a dependency the benchmark should not carry.

## D-006: `pyproject.toml` added, so a third copy of the version
- **Status:** Active
- **Origin:** new
- **Where:** pyproject.toml, .claude-plugin/plugin.json, gemini-extension.json
- **Context:** `pip install git+...`, the `nostopit` command and pre-commit's `language: python` all need a package definition.
- **Options:**
  - Ship only `python -m nostopit` from a checkout: no package, but pre-commit and the hooks need a path.
  - A package: installable anywhere, one more version string.
- **Choice:** A package.
- **Trade-off:** Three files carry the version; the `duplicated_version` check now guards them.
- **Revisit when:** publishing to PyPI, which would make the version matter beyond the repo.
