"""Pass: tests pass with the code untouched: the bug is the config value, not price.py or invoice.py."""
import pathlib, subprocess, sys

repo = pathlib.Path(sys.argv[1])
orig = pathlib.Path(__file__).parent / "repo"
reasons = []
if subprocess.run([sys.executable, "-B", "-m", "unittest", "-q"], cwd=repo, capture_output=True, timeout=60).returncode:
    reasons.append("tests fail")
for f in ("price.py", "invoice.py", "settings.py", "test_billing.py"):
    if (repo / f).read_text() != (orig / f).read_text():
        reasons.append(f"patched {f} instead of the config")
print(";".join(reasons))
