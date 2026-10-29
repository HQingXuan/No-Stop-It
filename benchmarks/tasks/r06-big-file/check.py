"""Pass: all five facts are in the reply and only SESSION_TTL changed."""
import pathlib, re, sys

repo, final = pathlib.Path(sys.argv[1]), sys.argv[2]
orig = (pathlib.Path(__file__).parent / "repo/limits.py").read_text()
reasons = []
for name, pat in {"MAX_UPLOAD_MB": r"\b250\b", "SESSION_TTL": r"\b3600\b", "RETRY_BACKOFF": r"1, ?4, ?16", "DEFAULT_REGION": r"eu-west-3",
                  "beta_export": r"\b(off|false|disabled|not (on|enabled))\b"}.items():
    if not re.search(pat, final, re.I):
        reasons.append(f"missing {name}")
if (repo / "limits.py").read_text() != orig.replace("SESSION_TTL = 3600", "SESSION_TTL = 7200"):
    reasons.append("limits.py edit wrong")
print(";".join(reasons))
