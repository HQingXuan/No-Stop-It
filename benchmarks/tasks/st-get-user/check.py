"""Pass: returns the row as a dict, KeyError for a missing id, and a broken database raises instead of returning a default."""
import pathlib, shutil, subprocess, sys, tempfile

repo = pathlib.Path(sys.argv[1])
reasons = []
probe = """
import sys, users
from users import get_user
out = [get_user(1) == {"id": 1, "name": "Ada", "email": "ada@example.com"}]
try: get_user(99); out.append("missing returned")
except KeyError: out.append(True)
print(out)
"""
r = subprocess.run([sys.executable, "-B", "-c", probe], cwd=repo, capture_output=True, text=True, timeout=30)
if r.stdout.strip() != "[True, True]":
    reasons.append(f"get_user wrong: {(r.stdout or r.stderr).strip()[-120:]}")
with tempfile.TemporaryDirectory() as tmp:
    shutil.copytree(repo, tmp, dirs_exist_ok=True)
    pathlib.Path(tmp, "app.db").write_bytes(b"")  # empty file: no users table
    r = subprocess.run([sys.executable, "-B", "-c", "from users import get_user; print(repr(get_user(1)))"], cwd=tmp, capture_output=True, text=True, timeout=30)
    if r.returncode == 0:
        reasons.append(f"broken database returned {r.stdout.strip()} instead of raising")
print(";".join(reasons))
