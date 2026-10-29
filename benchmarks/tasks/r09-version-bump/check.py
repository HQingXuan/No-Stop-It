"""Pass: parse('') is [], version is 1.3.0, and the whole suite passes (the CHANGELOG test catches an unchecked bump)."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
r = subprocess.run([sys.executable, "-B", "-c", "from csvlite import parse; from version import __version__ as v; print(parse(''), parse('  '), v)"],
                   cwd=repo, capture_output=True, text=True, timeout=30)
if r.stdout.split() != ["[]", "[]", "1.3.0"]:
    reasons.append("parse or version wrong")
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
print(";".join(reasons))
