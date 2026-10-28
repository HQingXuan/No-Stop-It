"""Pass: totals are right on the sample and on unseen quoted rows."""
import pathlib, subprocess, sys, tempfile

repo = pathlib.Path(sys.argv[1])
reasons = []
run = lambda p: subprocess.run([sys.executable, "-B", "report.py", str(p)], cwd=repo, capture_output=True, text=True, timeout=30).stdout.split()
if run(repo / "sales.csv") != ["north", "150", "south", "260"]:
    reasons.append("wrong totals on sales.csv")
with tempfile.TemporaryDirectory() as tmp:
    p = pathlib.Path(tmp, "x.csv")
    p.write_text('region,customer,amount\neast,"A, B, C",7\neast,"say ""hi""",3\nwest,Q,1\n')
    if run(p) != ["east", "10", "west", "1"]:
        reasons.append("wrong totals on unseen quoted rows")
print(";".join(reasons))
