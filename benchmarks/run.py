"""Run every task in a fresh repo, with and without no-stop-it, then score the run.

python benchmarks/run.py --runs 1
"""
import argparse, datetime, json, os, pathlib, shutil, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor

import score

ROOT = pathlib.Path(__file__).parent
SKILL = (ROOT.parent / "skills/no-stop-it/SKILL.md").read_text().split("---", 2)[2].strip()
ARMS = {"baseline": None, "no-stop-it": SKILL}
# Only what claude needs to sign in and reach the API, so no host settings, CLAUDE.md or plugins leak into a cell.
ENV_KEYS = ("PATH", "ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL", "CLAUDE_CODE_OAUTH_TOKEN", "CLAUDE_SESSION_INGRESS_TOKEN_FILE",
            "HTTPS_PROXY", "https_proxy", "NO_PROXY", "no_proxy", "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE")


def cell(task, arm, i, out, model, budget, bare):
    dest = out / task.name / f"{arm}-{i}"
    dest.mkdir(parents=True)
    with tempfile.TemporaryDirectory() as tmp:
        repo, home = pathlib.Path(tmp, "repo"), pathlib.Path(tmp, "home")
        shutil.copytree(task / "repo", repo, ignore=shutil.ignore_patterns("__pycache__"))
        home.mkdir()
        git = lambda *a: subprocess.run(["git", "-c", "user.name=bench", "-c", "user.email=bench@localhost", *a],
                                        cwd=repo, capture_output=True, text=True).stdout
        git("init", "-q"); git("add", "-A"); git("commit", "-qm", "seed")
        env = {k: os.environ[k] for k in ENV_KEYS if k in os.environ} | {"HOME": str(home), "IS_SANDBOX": "1", "PYTHONDONTWRITEBYTECODE": "1"}
        cmd = ["claude", "-p", (task / "prompt.txt").read_text(), "--model", model, "--output-format", "stream-json",
               "--verbose", "--permission-mode", "bypassPermissions", "--max-budget-usd", str(budget)]
        if bare:  # Claude Code's own prompt already asks for few comments; a plainer agent does not
            cmd += ["--system-prompt", "You are a coding agent working in this repository."]
        if ARMS[arm]:
            cmd += ["--append-system-prompt", ARMS[arm]]
        try:
            stdout = subprocess.run(cmd, cwd=repo, env=env, capture_output=True, text=True, timeout=900).stdout
        except subprocess.TimeoutExpired as e:
            stdout = e.stdout.decode() if isinstance(e.stdout, bytes) else e.stdout or ""
        (dest / "transcript.jsonl").write_text(stdout)
        git("add", "-A")
        (dest / "diff.patch").write_text(git("diff", "--cached", "HEAD"))
        shutil.copytree(repo, dest / "repo", ignore=shutil.ignore_patterns(".git"))
    print(f"done {task.name} {arm}-{i}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--budget", type=float, default=1.5, help="max USD per session")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--tasks", nargs="*", help="task names, default all")
    ap.add_argument("--arms", nargs="*", default=list(ARMS), choices=list(ARMS))
    ap.add_argument("--bare", action="store_true", help="a one-line system prompt instead of Claude Code's")
    a = ap.parse_args()
    tasks = [t for t in sorted((ROOT / "tasks").iterdir()) if not a.tasks or t.name in a.tasks]
    out = ROOT / "results" / datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H%M%S") / "raw"
    # Interleave arms so a slow or fast stretch of the API does not land on one arm.
    jobs = [(t, arm, i) for i in range(a.runs) for n, t in enumerate(tasks)
            for arm in (a.arms if (i + n) % 2 == 0 else a.arms[::-1])]
    with ThreadPoolExecutor(a.jobs) as pool:
        list(pool.map(lambda j: cell(*j, out, a.model, a.budget, a.bare), jobs))
    (out.parent / "meta.json").write_text(json.dumps({"model": a.model, "runs": a.runs, "budget": a.budget, "arms": a.arms, "bare": a.bare}))
    import judge  # judge imports this module, so not at the top
    if judge.selftest():
        judge.judge(out.parent)
    print(score.report(out.parent))


if __name__ == "__main__":
    main()
