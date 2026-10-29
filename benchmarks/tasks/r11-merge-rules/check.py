"""Pass: every rule in docs/merge.md holds, inputs are untouched, and no stub is left."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
probe = """
from merge import merge
base = {"a": 1, "keep": {"x": 1, "deep": {"p": 1, "q": 2}}, "tags": ["a", "b"], "gone": 5, "swap": {"k": 1, "j": 2}}
over = {"b": 2, "keep": {"y": 2, "deep": {"q": 3, "r": None}}, "tags": ["b", "c"], "gone": None, "!swap": {"z": 9}, "a": [1]}
snap = repr((base, over))
got = merge(base, over)
want = {"a": [1], "keep": {"x": 1, "deep": {"p": 1, "q": 3}, "y": 2}, "tags": ["a", "b", "c"], "swap": {"z": 9}, "b": 2}
print("ok" if got == want and repr((base, over)) == snap and merge({}, {"n": None}) == {} else f"bad {got}")
"""
r = subprocess.run([sys.executable, "-B", "-c", probe], cwd=repo, capture_output=True, text=True, timeout=30)
if r.stdout.strip() != "ok":
    reasons.append(f"rules not all met: {(r.stdout or r.stderr).strip()[-120:]}")
if "NotImplemented" in (repo / "merge.py").read_text() or "TODO" in (repo / "merge.py").read_text():
    reasons.append("stub left")
print(";".join(reasons))
