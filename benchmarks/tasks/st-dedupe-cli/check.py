"""Pass: dedupes across files in order, --ignore-case keeps the first spelling, a missing file fails loudly, tests pass."""
import pathlib, subprocess, sys, tempfile

repo = pathlib.Path(sys.argv[1])
reasons = []
with tempfile.TemporaryDirectory() as tmp:
    a, b = pathlib.Path(tmp, "a.txt"), pathlib.Path(tmp, "b.txt")
    a.write_text("x\nY\nx\n\n")
    b.write_text("y\nz\nY\n\nx")
    run = lambda *args: subprocess.run([sys.executable, "-B", "dedupe.py", *args], cwd=repo, capture_output=True, text=True, timeout=30)
    if run(str(a), str(b)).stdout.splitlines() != ["x", "Y", "", "y", "z"]:
        reasons.append("dedupe wrong")
    if run("--ignore-case", str(a), str(b)).stdout.splitlines() != ["x", "Y", "", "z"]:
        reasons.append("--ignore-case wrong")
    if run(str(a), str(pathlib.Path(tmp, "missing.txt"))).returncode == 0:
        reasons.append("missing file exits 0")
if not (repo / "test_dedupe.py").exists() or subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider"], cwd=repo, capture_output=True, timeout=60).returncode:  # pytest also runs unittest tests
    reasons.append("no tests or tests fail")
print(";".join(reasons))
