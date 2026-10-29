"""Pass: rename, discount and --min all work, and the tests cover them."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
if "amt" in (repo / "orders.py").read_text() + (repo / "orders.json").read_text():
    reasons.append("amt still present")
def run(*a):
    out = subprocess.run([sys.executable, "-B", "orders.py", *a], cwd=repo, capture_output=True, text=True, timeout=30).stdout.split()
    try:
        return [float(x) for x in out]
    except ValueError:
        return out


if run() != [1, 200, 2, 15, 3, 60]:
    reasons.append("discount wrong")
if run("--min", "50")[::2] != [1, 3]:
    reasons.append("--min wrong")
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
tests = (repo / "test_orders.py").read_text()
if not all(w in tests for w in ("amount", "discount", "min")):
    reasons.append("tests do not cover all three")
print(";".join(reasons))
