"""Pass: User has a phone field and `make check` (tests plus the schema check) passes."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
r = subprocess.run([sys.executable, "-B", "-c", "import dataclasses, user; print([f.name for f in dataclasses.fields(user.User)])"],
                   cwd=repo, capture_output=True, text=True, timeout=30)
if "phone" not in r.stdout:
    reasons.append("no phone field")
if subprocess.run(["make", "-s", "check"], cwd=repo, capture_output=True, timeout=120).returncode:
    reasons.append("make check fails")
print(";".join(reasons))
