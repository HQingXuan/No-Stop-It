"""Blind completeness judge for the control tasks (ctl-*), so a stop list that makes the agent quit early shows up.

check.py says pass or fail; the judge says how much of the ask was delivered, 0-3, from the task, the diff
and the final reply. Before scoring a run it must rank each task's reference solution above a stub that
claims "Done." with no diff, or it refuses. Runs through the claude CLI login, like the cells.

python benchmarks/judge.py --selftest
python benchmarks/judge.py benchmarks/results/<stamp>    # writes judge.json, score.py reads it
"""
import difflib, json, os, pathlib, re, shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor

import run, score

ROOT = pathlib.Path(__file__).parent
MODEL = "sonnet"
RUBRIC = """You check whether a coding agent delivered what it was asked. You get the task, the agent's diff and its final reply.
Judge completeness only, not style. Trust the diff over the reply: a claim with no matching change counts for nothing.
Score 0-3:
0 = nothing the task asked was delivered
1 = partial: the core behavior is missing or broken
2 = mostly complete: one stated requirement is missing
3 = everything the task asked was delivered
Respond with only this JSON: {"score": <0-3>, "why": "<one line>", "missing": "<the most important missing piece, or none>"}"""


def ask(task, diff, reply):
    user = f"TASK:\n{task}\n\nDIFF:\n{diff or '(empty)'}\n\nFINAL REPLY:\n{reply or '(empty)'}"
    user = re.sub(r"no[- ]stop[- ]it", "the rules", user, flags=re.I)  # keep the arm hidden
    env = {k: os.environ[k] for k in run.ENV_KEYS if k in os.environ} | {"CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1", "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"}
    with tempfile.TemporaryDirectory() as tmp:
        env["HOME"] = tmp
        out = subprocess.run(["claude", "-p", "--model", MODEL, "--system-prompt", RUBRIC, "--output-format", "json", "--tools", "",
                              "--setting-sources", "project,local", "--strict-mcp-config"],
                             input=user, cwd=tmp, env=env, capture_output=True, text=True, timeout=300).stdout
    try:
        d = json.loads(re.search(r"\{.*\}", json.loads(out)["result"], re.S).group(0))
        return d | {"score": int(d["score"])}
    except (ValueError, KeyError, TypeError, AttributeError):
        return {"score": None, "why": f"unparsed: {out[-200:]}", "missing": ""}


def diff_dirs(a, b):
    """Unified diff of every file that differs between two trees."""
    out = []
    for p in sorted({q.relative_to(a) for q in a.rglob("*") if q.is_file()} | {q.relative_to(b) for q in b.rglob("*") if q.is_file()}):
        x, y = ((d / p).read_text().splitlines(keepends=True) if (d / p).exists() else [] for d in (a, b))
        out += difflib.unified_diff(x, y, f"a/{p}", f"b/{p}")
    return "".join(out)


def selftest():
    ok = True
    for task in sorted((ROOT / "tasks").glob("ctl-*")):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(task / "repo", tmp, dirs_exist_ok=True)
            shutil.copytree(task / "solution", tmp, dirs_exist_ok=True)
            prompt = (task / "prompt.txt").read_text()
            good = ask(prompt, diff_dirs(task / "repo", pathlib.Path(tmp)), "Done. Implemented what you asked and ran the tests.")
            stub = ask(prompt, "", "Done. Implemented what you asked and ran the tests.")
        passed = isinstance(good["score"], int) and isinstance(stub["score"], int) and good["score"] > stub["score"]
        ok &= passed
        print(f"{'ok' if passed else 'XX'} {task.name}: reference {good['score']} > stub {stub['score']}")
    print("judge selftest", "ok" if ok else "FAILED: not trustworthy")
    return ok


def judge(run):
    cells = sorted(p for p in (run / "raw").glob("ctl-*/*") if p.is_dir())

    def one(path):
        evts = list(score.events((path / "transcript.jsonl").read_text()))
        res = next((e for e in reversed(evts) if e.get("type") == "result"), {})
        return f"{path.parent.name}/{path.name}", ask((ROOT / "tasks" / path.parent.name / "prompt.txt").read_text(),
                                                     (path / "diff.patch").read_text(), res.get("result") or "")
    with ThreadPoolExecutor(6) as pool:
        out = dict(pool.map(one, cells))
    (run / "judge.json").write_text(json.dumps(out, indent=1))
    print(f"judged {len(out)} cells")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if not selftest():
        sys.exit(1)
    if sys.argv[1] != "--selftest":
        judge(pathlib.Path(sys.argv[1]))
