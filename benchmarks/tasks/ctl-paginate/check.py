"""Pass: pages, the default, the cap and both errors behave as asked, tests pass, README documents it."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
probe = """
from store import list_items as f
def err(**k):
    try: f(**k)
    except ValueError: return True
    return False
print(len(f()), f()[0], f(page=2)[0], len(f(per_page=500)), f(page=3, per_page=100)[-1], f(page=99), err(page=0), err(per_page=0))
"""
r = subprocess.run([sys.executable, "-B", "-c", probe], cwd=repo, capture_output=True, text=True, timeout=30)
if r.stdout.split() != ["20", "item-1", "item-21", "100", "item-250", "[]", "True", "True"]:
    reasons.append(f"pagination wrong: {r.stdout.strip() or r.stderr.strip().splitlines()[-1:]}")
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
if "per_page" not in (repo / "README.md").read_text():
    reasons.append("README not updated")
print(";".join(reasons))
