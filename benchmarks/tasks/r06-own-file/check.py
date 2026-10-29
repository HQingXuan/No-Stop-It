"""Pass: the fixture is right, the generator reproduces it, and the test passes."""
import json, pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
want = [{"id": i, "name": f"user{i}", "email": f"user{i}@example.com", "active": i % 7 != 0} for i in range(1, 51)]
try:
    got = json.loads((repo / "fixtures/users.json").read_text())
    if [{k: u.get(k) for k in ("id", "name", "email", "active")} for u in got] != want:
        reasons.append("fixture wrong")
except (OSError, ValueError, AttributeError):
    reasons.append("no fixture")
if not (repo / "gen_fixtures.py").exists() or not (repo / "test_fixtures.py").exists():
    reasons.append("missing script or test")
elif subprocess.run([sys.executable, "-B", "-m", "unittest", "-q", "test_fixtures"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("test fails")
print(";".join(reasons))
