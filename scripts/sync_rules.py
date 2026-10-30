"""Copy the body of skills/no-stop-it/SKILL.md into each agent's rules file.

python scripts/sync_rules.py           # rewrite the copies
python scripts/sync_rules.py --check   # exit 1 if a copy is out of date
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).parents[1]
BODY = (ROOT / "skills/no-stop-it/SKILL.md").read_text().split("---", 2)[2].strip() + "\n"
COPIES = {
    "AGENTS.md": BODY,  # Codex, Gemini CLI (via gemini-extension.json), Windsurf, Cline, opencode, Devin and most other agents
    ".cursor/rules/no-stop-it.mdc": "---\ndescription: No-Stop-It style rules for code the agent writes.\nglobs:\nalwaysApply: true\n---\n\n" + BODY,
    ".github/copilot-instructions.md": BODY,
    ".kiro/steering/no-stop-it.md": "---\ninclusion: always\n---\n\n" + BODY,
}

stale = [p for p, text in COPIES.items() if not (ROOT / p).exists() or (ROOT / p).read_text() != text]
if sys.argv[1:] == ["--check"]:
    print("\n".join(f"out of date: {p}" for p in stale) or "rules copies ok")
    sys.exit(bool(stale))
for p in stale:
    (ROOT / p).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / p).write_text(COPIES[p])
    print(f"wrote {p}")
