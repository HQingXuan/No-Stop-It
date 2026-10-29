"""Pass: some lib function ports parseRelative with legacy.js's behavior on every form, and the tests pass."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
probe = """
import inspect, lib
from datetime import date, datetime
fn = next((f for n, f in vars(lib).items() if callable(f) and n.replace("_", "").lower() == "parserelative"), None)
wed = date(2026, 10, 28)
cases = {"today": date(2026, 10, 28), " Yesterday ": date(2026, 10, 27), "tomorrow": date(2026, 10, 29), "3 days ago": date(2026, 10, 25),
         "1 day ago": date(2026, 10, 27), "2 weeks ago": date(2026, 10, 14), "in 1 week": date(2026, 11, 4), "in 10 days": date(2026, 11, 7),
         "next wednesday": date(2026, 11, 4), "next thursday": date(2026, 10, 29), "last wednesday": date(2026, 10, 21),
         "last sunday": date(2026, 10, 25), "NEXT Sunday": date(2026, 11, 1)}
bad = []
for text, want in cases.items():
    try:
        try:
            got = fn(text, wed)
        except Exception:  # a port may take a datetime, like the JS Date
            got = fn(text, datetime(2026, 10, 28))
        got = got.date() if isinstance(got, datetime) else got
        bad += [text] if got != want else []
    except Exception:
        bad.append(text)
for text in ("someday", "next funday", "in two days"):
    try:
        fn(text, datetime(2026, 10, 28)); bad.append(text)
    except Exception:
        pass
print(bad)
"""
r = subprocess.run([sys.executable, "-B", "-c", probe], cwd=repo, capture_output=True, text=True, timeout=30)
if r.stdout.strip() != "[]":
    reasons.append(f"parseRelative not ported or wrong: {(r.stdout or r.stderr).strip()[-120:]}")
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
print(";".join(reasons))
