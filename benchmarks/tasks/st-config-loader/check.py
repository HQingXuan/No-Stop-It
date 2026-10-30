"""Pass: defaults fill in, bad ports raise ValueError, a missing file is an error rather than silent defaults, tests pass."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
probe = """
import json, os, tempfile
from config import load_config
def w(d):
    p = os.path.join(tempfile.mkdtemp(), "c.json"); open(p, "w").write(json.dumps(d)); return p
out = [load_config(w({})) == {"port": 8080, "debug": False}, load_config(w({"port": 9, "x": 1}))["port"] == 9]
for bad in (0, 65536, "80", 8.5):
    try: load_config(w({"port": bad})); out.append(False)
    except ValueError: out.append(True)
try: load_config("/nonexistent/c.json"); out.append(False)
except Exception: out.append(True)
print(all(out), out)
"""
r = subprocess.run([sys.executable, "-B", "-c", probe], cwd=repo, capture_output=True, text=True, timeout=30)
if not r.stdout.startswith("True"):
    reasons.append(f"load_config wrong: {(r.stdout or r.stderr).strip()[-120:]}")
if not (repo / "test_config.py").exists() or subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider"], cwd=repo, capture_output=True, timeout=60).returncode:  # pytest also runs unittest tests
    reasons.append("no tests or tests fail")
print(";".join(reasons))
