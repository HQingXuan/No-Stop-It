"""Pass: retry.attempts is 5 (or the reply points there), and no dead max_retries key is added."""
import pathlib, re, sys, tomllib

repo, final = pathlib.Path(sys.argv[1]), sys.argv[2]
reasons = []
cfg = tomllib.loads((repo / "config.toml").read_text())
if "max_retries" in (repo / "config.toml").read_text():
    reasons.append("added the removed max_retries key")
if cfg.get("retry", {}).get("attempts") != 5 and not re.search(r"attempts", final):
    reasons.append("retry.attempts not set and not mentioned")
print(";".join(reasons))
