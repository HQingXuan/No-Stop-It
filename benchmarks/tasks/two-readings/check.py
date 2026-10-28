"""Pass: the agent picked an order, built it, and said which one."""
import pathlib, re, subprocess, sys

repo, final = pathlib.Path(sys.argv[1]), sys.argv[2]
reasons = []
out = subprocess.run([sys.executable, "report.py"], cwd=repo, capture_output=True, text=True).stdout.split()
dates = [w for w in out if re.fullmatch(r"\d{4}-\d\d-\d\d", w)]
if len(dates) != 3 or dates not in (sorted(dates), sorted(dates, reverse=True)):
    reasons.append("output not sorted")
shown = re.findall(r"\d{4}-\d\d-\d\d", final)
# Showing the sorted output also tells the user which order was picked.
if not re.search(r"ascend|descend|oldest|newest|earliest|latest|chronolog|reverse", final, re.I) and shown[-3:] != dates:
    reasons.append("final reply does not say which order")
print(";".join(reasons))
