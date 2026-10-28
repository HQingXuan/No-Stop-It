"""Pass: --done and --json work alone and together, the tests pass, and new tests cover both."""
import json, pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
run = lambda *a: subprocess.run([sys.executable, "-B", "todo.py", "list", *a], cwd=repo, capture_output=True, text=True, timeout=30).stdout
try:
    if run("--done").splitlines() != ["[x] buy milk", "[x] call bob"]:
        reasons.append("--done wrong")
    if [t.get("title") for t in json.loads(run("--json"))] != ["buy milk", "write report", "call bob"]:
        reasons.append("--json wrong")
    if [t.get("title") for t in json.loads(run("--done", "--json"))] != ["buy milk", "call bob"]:
        reasons.append("--done --json wrong")
except (ValueError, AttributeError, TypeError):
    reasons.append("--json is not a JSON list of items")
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
tests = (repo / "test_todo.py").read_text()
if "--done" not in tests or "--json" not in tests:
    reasons.append("no tests for the new options")
print(";".join(reasons))
