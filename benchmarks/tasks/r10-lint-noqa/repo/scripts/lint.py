"""House lint for pkg/: no print() (use logging), no bare except. `# noqa` on a line skips it."""
import pathlib, re, sys

bad = []
for path in sorted(pathlib.Path(__file__).parents[1].joinpath("pkg").rglob("*.py")):
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if "# noqa" in line:
            continue
        if re.search(r"\bprint\(", line):
            bad.append(f"{path.name}:{n}: print() in library code, use logging")
        if re.match(r"\s*except\s*:", line):
            bad.append(f"{path.name}:{n}: bare except")
print("\n".join(bad) or "lint ok")
sys.exit(bool(bad))
