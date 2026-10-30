"""Score a run directory, or check the scorers before spending anything.

python benchmarks/score.py --selftest
python benchmarks/score.py benchmarks/results/<stamp>
"""
import collections, json, math, pathlib, random, re, shutil, statistics, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).parent
# Style counts on added lines.
STYLE = {"comments": re.compile(r"^\+(?!\+\+)(\s*|.*\s)(#(?!!)|//)\s", re.M),
         "docstrings": re.compile(r'^\+.*?("""|\'\'\')', re.M),
         "emoji": re.compile(r"^\+.*[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50]", re.M),
         "broad_except": re.compile(r"^\+\s*except\s*(\(?\s*(Base)?Exception\b[^:]*)?:", re.M),
         "leftovers": re.compile(r"^\+.*(\b\w+_(old|v2|new|legacy)\b|\bTODO\b|\bFIXME\b)", re.M)}
GROUPS = {"controls": lambda t: t.startswith("ctl-"), "style": lambda t: t.startswith("st-")}
# metric -> (aggregate over a task's cells, effect: "diff" of rates or "ratio" of medians, True if higher is better)
METRICS = {"pass": (statistics.mean, "diff", True), "complete": (statistics.mean, "diff", True), "style": (statistics.mean, "diff", False),
           "cost": (statistics.median, "ratio", False), "out_tokens": (statistics.median, "ratio", False),
           "turns": (statistics.median, "ratio", False), "seconds": (statistics.median, "ratio", False)}


def events(text):
    for line in text.splitlines():
        try:
            yield json.loads(line)
        except ValueError:
            pass


def unrelated(diff, allowed):
    """Changed lines in files the task does not need."""
    n, keep = 0, True
    for line in diff.splitlines():
        if line.startswith("diff --git"):
            keep = line.split(" b/", 1)[-1] in allowed
        elif not keep and line[:1] in "+-" and not line.startswith(("+++", "---")):
            n += 1
    return n


def style(diff):
    """Counts of each STYLE habit in added lines of code files, plus new .md files."""
    code = "".join(f for f in re.split(r"(?=^diff --git )", diff, flags=re.M) if not re.match(r"diff --git \S+ \S+\.md\n", f))
    out = {k: len(r.findall(code)) for k, r in STYLE.items()}
    out["docstrings"] = sum(len(re.findall(r'"""|\'\'\'', line)) for line in code.splitlines() if line.startswith("+")) // 2
    out["new_md"] = len(re.findall(r"^diff --git a/\S+\.md b/\S+\nnew file mode", diff, re.M))
    return out


def cell(path, task):
    evts = list(events((path / "transcript.jsonl").read_text()))
    res = next((e for e in reversed(evts) if e.get("type") == "result"), {})
    final = res.get("result") or ""
    diff = (path / "diff.patch").read_text()
    allowed = set((task / "allowed.txt").read_text().split())
    why = subprocess.run([sys.executable, "-I", "-B", str(task / "check.py"), str(path / "repo"), final, str(path / "transcript.jsonl")],
                         capture_output=True, text=True, timeout=60)
    reasons = why.stdout.strip() or (f"check crashed: {why.stderr.strip().splitlines()[-1:]}" if why.returncode else "")
    c = {"pass": not reasons, "why": reasons, "unrelated_lines": unrelated(diff, allowed), "cost": res.get("total_cost_usd") or 0,
         "turns": res.get("num_turns") or 0, "seconds": (res.get("duration_ms") or 0) / 1000,
         "out_tokens": (res.get("usage") or {}).get("output_tokens") or 0, "ended": res.get("subtype", "no result")}
    st = style(diff)
    return c | st | {"style": sum(st.values())}


def sign_p(wins, losses):
    """Two-sided sign test: how likely a split this lopsided is by chance."""
    n, k = wins + losses, min(wins, losses)
    return min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n) if n else 1.0


def effect(pairs, kind, iters=2000):
    """Mean difference or geometric-mean ratio over tasks, with a 95% bootstrap CI that resamples tasks."""
    f = (lambda ps: sum(b - a for a, b in ps) / len(ps)) if kind == "diff" else \
        (lambda ps: math.exp(sum(math.log(b / a) for a, b in ps) / len(ps)))
    rnd = random.Random(0)
    boot = sorted(f([rnd.choice(pairs) for _ in pairs]) for _ in range(iters))
    return f(pairs), boot[int(iters * .025)], boot[int(iters * .975)]


def compare(rows, tasks, base, arm):
    """One line per group x metric: on how many tasks the arm beat the baseline, and by how much."""
    md = []
    for g, member in GROUPS.items():
        for m, (agg, kind, higher) in METRICS.items():
            pairs = []
            for t in filter(member, tasks):
                a, b = ([c[m] for _, c in rows[t, x] if c.get(m) is not None] for x in (base, arm))
                if a and b and (kind == "diff" or min(agg(a), agg(b)) > 0):  # a ratio needs both sides above 0
                    pairs.append((agg(a), agg(b)))
            if not pairs:
                continue
            wins = sum((b > a) == higher for a, b in pairs if a != b)
            ties = sum(a == b for a, b in pairs)
            est, lo, hi = effect(pairs, kind)
            fmt = (lambda x: f"{x:+.2f}") if kind == "diff" else (lambda x: f"x{x:.2f}")
            md.append(f"| {g} | {m} | {wins} | {len(pairs) - ties - wins} | {ties} | {sign_p(wins, len(pairs) - ties - wins):.3f} | "
                      f"{fmt(est)} [{fmt(lo)}, {fmt(hi)}] |")
    return md


def report(run):
    rows = collections.defaultdict(list)
    judged = json.loads((run / "judge.json").read_text()) if (run / "judge.json").exists() else {}
    for path in sorted((run / "raw").glob("*/*")):
        c = cell(path, ROOT / "tasks" / path.parent.name) | {"complete": (judged.get(f"{path.parent.name}/{path.name}") or {}).get("score")}
        rows[(path.parent.name, path.name.rsplit("-", 1)[0])].append((path.name, c))
    arms = sorted({a for _, a in rows})
    tasks = sorted({t for t, _ in rows})
    keys = (*STYLE, "new_md", "unrelated_lines")
    md = [f"# Run {run.name}", "", f"`{(run / 'meta.json').read_text() if (run / 'meta.json').exists() else ''}`", "",
          "## Arm vs baseline, per task",
          "", "Each task is one pair: its pass rate, mean completeness or mean style count (diff), or its median cost, tokens, turns or seconds (ratio, arm/baseline).",
          "better/worse/ties count tasks; p is a two-sided sign test over them; the 95% CI resamples tasks.", ""]
    for a in arms:
        if a != "baseline":
            md += [f"### {a}", "", "| group | metric | better | worse | ties | sign p | effect [95% CI] |", "|---|---|---|---|---|---|---|",
                   *compare(rows, tasks, "baseline", a), ""]
    md += ["## Task passed", "", "| task | " + " | ".join(arms) + " |", "|---|" + "---|" * len(arms)]
    for t in tasks:
        md.append(f"| {t} | " + " | ".join(f"{sum(c['pass'] for _, c in rows[t, a])}/{len(rows[t, a])}" for a in arms) + " |")
    md += ["", "## Style counts (sum over all cells) and cost (mean per cell)", "", "| arm | " + " | ".join(keys) + " | cost $ | turns | seconds |",
           "|---|" + "---|" * (len(keys) + 3)]
    for a in arms:
        cs = [c for t in tasks for _, c in rows[t, a]]
        md.append(f"| {a} | " + " | ".join(str(sum(c[k] for c in cs)) for k in keys)
                  + " | " + " | ".join(f"{sum(c[k] for c in cs) / len(cs):.2f}" for k in ("cost", "turns", "seconds")) + " |")
    md += ["", "## Every cell", "", "| task | cell | pass | why | complete | " + " | ".join(keys) + " | cost $ | ended |", "|---|" + "---|" * (len(keys) + 7)]
    for t in tasks:
        for a in arms:
            for name, c in rows[t, a]:
                md.append(f"| {t} | {name} | {'yes' if c['pass'] else 'no'} | {c['why']} | {'-' if c['complete'] is None else c['complete']} | " + " | ".join(str(c[k]) for k in keys)
                          + f" | {c['cost']:.3f} | {c['ended']} |")
    text = "\n".join(md) + "\n"
    (run / "summary.md").write_text(text)
    return text


def selftest():
    sty = ('diff --git a/NOTES.md b/NOTES.md\nnew file mode 100644\n+# Notes\ndiff --git a/a.py b/a.py\n+def f(x):\n+    """Return x."""\n'
           '+# increment x\n+    y = x + 1  # add one\n+    url = "http://x/#a"\n+    try:\n+        g()\n+    except Exception as e:\n+        print("✅ ok")\n'
           '+def parse_old():\n+    pass  # TODO\n+#!/usr/bin/env python\n')
    assert style(sty) == {"comments": 3, "docstrings": 1, "emoji": 1, "broad_except": 1, "leftovers": 2, "new_md": 1}, style(sty)
    diff = "diff --git a/x.py b/x.py\n+++ b/x.py\n+a\ndiff --git a/y.py b/y.py\n-b\n+c\n"
    assert unrelated(diff, {"x.py"}) == 2
    assert sign_p(5, 0) == 0.0625 and sign_p(3, 3) == 1.0 and sign_p(0, 0) == 1.0
    assert effect([(1, 2), (2, 1)], "ratio")[0] == 1.0 and effect([(0, 1), (1, 1)], "diff")[0] == 0.5
    rows = {("st-x", "baseline"): [("", {"cost": 2.0, "pass": 0})], ("st-x", "x"): [("", {"cost": 1.0, "pass": 1})]}
    assert compare(rows, ["st-x"], "baseline", "x") == ["| style | pass | 1 | 0 | 0 | 1.000 | +1.00 [+1.00, +1.00] |",
                                                        "| style | cost | 1 | 0 | 0 | 1.000 | x0.50 [x0.50, x0.50] |"]
    # A reference solution must pass its own check.
    for task in sorted(t.parent for t in (ROOT / "tasks").glob("*/solution")):
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(task / "repo", tmp, dirs_exist_ok=True)
            shutil.copytree(task / "solution", tmp, dirs_exist_ok=True)
            why = subprocess.run([sys.executable, "-I", "-B", str(task / "check.py"), tmp, ""], capture_output=True, text=True)
            assert why.returncode == 0 and not why.stdout.strip(), f"{task.name}: reference solution fails: {why.stdout.strip()}"
    # Every check must fail on the untouched seed repo, or it passes for free.
    for task in sorted((ROOT / "tasks").iterdir()):
        why = subprocess.run([sys.executable, "-I", "-B", str(task / "check.py"), str(task / "repo"), ""], capture_output=True, text=True)
        assert why.returncode == 0 and why.stdout.strip(), f"{task.name}: check passes on the seed repo or crashed"
    print("selftest ok")


if __name__ == "__main__":
    selftest() if sys.argv[1:] == ["--selftest"] else print(report(pathlib.Path(sys.argv[1])))
