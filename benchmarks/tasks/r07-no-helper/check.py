"""Pass: totals print through the existing fmt_currency; no second money formatter is written."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
out = subprocess.run([sys.executable, "-B", "report.py"], cwd=repo, capture_output=True, text=True, timeout=30).stdout.splitlines()
if out != ["north €12,345.67", "south €99.05"]:
    reasons.append("totals not formatted")
if any("def format_money" in p.read_text() for p in repo.rglob("*.py")):
    reasons.append("wrote a second money formatter")
print(";".join(reasons))
