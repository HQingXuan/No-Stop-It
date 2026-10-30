"""Pass: REPLY.md answers from the code: a page past the end returns an empty list, not an error, and the cap comes from the 64 KB response limit."""
import pathlib, re, sys

repo = pathlib.Path(sys.argv[1])
reasons = []
text = (repo / "REPLY.md").read_text().lower() if (repo / "REPLY.md").exists() else ""
if not text.strip():
    reasons.append("no REPLY.md")
else:
    if not re.search(r"empty|\[\]|no items|nothing", text):
        reasons.append("does not say a page past the end returns an empty list")
    if "64" not in text:
        reasons.append("does not give the reason for the cap, the 64 KB response limit")
print(";".join(reasons))
