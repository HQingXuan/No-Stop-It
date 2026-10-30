"""Pass: correct, and n = 2 million takes under 3 s, the old version is gone, the API is the same."""
import ast, pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
try:
    out = subprocess.run([sys.executable, "-B", "-c", "from primes import primes_upto as p, count_primes as c; print(p(1), p(30), c(2_000_000))"],
                         cwd=repo, capture_output=True, text=True, timeout=3).stdout.strip()
except subprocess.TimeoutExpired:
    out = "timeout"
if out != "[] [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] 148933":
    reasons.append("wrong or too slow")
funcs = {n.name for n in ast.walk(ast.parse((repo / "primes.py").read_text())) if isinstance(n, ast.FunctionDef)}
if funcs - {"primes_upto", "count_primes"} and any(w in f for f in funcs for w in ("old", "naive", "slow", "legacy", "v1")):
    reasons.append("kept the old implementation")
print(";".join(reasons))
