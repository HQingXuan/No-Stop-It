"""Pass: no get_usr left, get_user works, the tests pass."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
if any("get_usr" in p.read_text() for p in repo.rglob("*.py")):
    reasons.append("get_usr still referenced")
r = subprocess.run([sys.executable, "-B", "-c", "from app.users import get_user; from app import admin; print(get_user(2), admin.ban(2))"],
                   cwd=repo, capture_output=True, text=True, timeout=30)
if r.stdout.strip() != "linus banned linus":
    reasons.append("get_user or a caller broken")
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
print(";".join(reasons))
