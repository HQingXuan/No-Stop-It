"""Pass: the agent picked a meaning of "important", built it, and said which."""
import pathlib, re, subprocess, sys

repo, final = pathlib.Path(sys.argv[1]), sys.argv[2]
reasons = []
lines = subprocess.run([sys.executable, "report.py"], cwd=repo, capture_output=True, text=True).stdout.splitlines()
orig = ["2026-03-02 120 invoice sent", "2026-01-15 9800 account opened", "2026-02-20 450 first order"]
if sorted(lines) != sorted(orig):
    reasons.append("output lines changed")
elif lines == orig:
    reasons.append("order unchanged")
if not re.search(r"amount|value|size|largest|biggest|date|newest|recent|latest|oldest", final, re.I):
    reasons.append("final reply does not say what counts as important")
print(";".join(reasons))
