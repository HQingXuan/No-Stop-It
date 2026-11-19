"""nostopit: run the checks on a diff, a file, a commit message, or from an agent hook.

nostopit diff [--base REF | --staged]      the working tree against REF (default HEAD), plus untracked files
nostopit file PATH...                      one or more files, as a diff against HEAD
nostopit commit-msg FILE                   git commit-msg hook
nostopit hook                              reads the hook event JSON on stdin (Claude Code or Kiro), picks the check
nostopit --selftest
"""
import argparse, json, os, pathlib, re, subprocess, sys, tempfile

from . import checks

LEVELS = {"error": 0, "warn": 1}
SEND = re.compile(r"\bgit\s+push\b|\bgh\s+(?:pr|issue|release)\s+(?:create|merge|comment|review|edit|close|ready)\b|\bgit\s+send-email\b"
                  r"|\bnpm\s+publish\b|\btwine\s+upload\b|\bcargo\s+publish\b|\bgem\s+push\b|--publish\b|\bpublish\s*=\s*true\b|\bautoPublish\b")


def build_diff(root, base="HEAD", staged=False, untracked=True, paths=()):
    """Unified diff of the working tree against base (or the index), with untracked files shown as new files."""
    tail = ["--", *paths] if paths else []
    out = checks.git(root, "diff", "--no-color", "--no-ext-diff", *(["--cached"] if staged else [base]), *tail)
    if untracked and not staged:
        for p in checks.git(root, "ls-files", "--others", "--exclude-standard", *tail).splitlines()[:100]:
            out += new_file_diff(root, p)
    return out


def new_file_diff(root, path):
    out = checks.git(root, "diff", "--no-color", "--no-index", "--", os.devnull, path)
    if out:
        return re.sub(r"^diff --git a/\S+ b/", f"diff --git a/{path} b/", out, count=1, flags=re.M)
    try:
        lines = (pathlib.Path(root) / path).read_text(errors="replace").splitlines()
    except OSError:
        return ""
    return f"diff --git a/{path} b/{path}\nnew file mode 100644\n@@ -0,0 +1,{len(lines)} @@\n" + "".join(f"+{l}\n" for l in lines)


def file_diff(root, paths):
    out = ""
    for p in paths:
        rel = os.path.relpath(os.path.abspath(p), root)
        tracked = checks.git(root, "ls-files", "--error-unmatch", "--", rel).strip() != ""
        out += build_diff(root, paths=[rel], untracked=False) if tracked else new_file_diff(root, rel)
    return out


def toplevel(cwd):
    """The repository root for a directory, or the directory itself outside git, so diff paths resolve from the right place."""
    return checks.git(cwd, "rev-parse", "--show-toplevel").strip() or cwd


def send_block(command):
    """The reason a publishing command is blocked, or "" when it may run."""
    extra = os.environ.get("NOSTOPIT_SEND_EXTRA")
    hit = SEND.search(command) or (extra and re.search(extra, command))
    if not hit or os.environ.get("NOSTOPIT_ALLOW_SEND") == "1" or "NOSTOPIT_ALLOW_SEND=1" in command:
        return ""
    return (f"No-Stop-It: `{hit.group(0).strip()}` publishes or sends something a person will receive. Drafting is yours, sending is the user's: "
            "show the command and ask them to run it. If the user already asked for this, run it with NOSTOPIT_ALLOW_SEND=1 in front and say so in your reply.")


def hook_plan(event):
    """From a hook's stdin JSON: ("send", command), ("file", path), ("diff", None) or (None, None)."""
    name = (event.get("hook_event_name") or event.get("event") or "").lower()
    tool_input = event.get("tool_input") or event.get("toolInput") or {}
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    path = next((tool_input.get(k) for k in ("file_path", "path", "targetFile", "notebook_path") if isinstance(tool_input, dict) and tool_input.get(k)), None)
    if name.startswith("pretooluse"):
        return ("send", command) if command else (None, None)
    if name.startswith("posttooluse"):
        return ("file", path) if path else ("diff", None) if not command else (None, None)
    if name == "stop":
        return (None, None) if event.get("stop_hook_active") else ("diff", None)
    return (None, None)


def render(found, allowed, fmt):
    if fmt == "json":
        return json.dumps([f._asdict() for f in found])
    lines = [f"{f.path or '-'}:{f.line or '-'}: [{f.level}] {f.rule}: {f.msg}" for f in found]
    n = {lvl: sum(f.level == lvl for f in found) for lvl in LEVELS}
    lines.append(f"{n['error']} errors, {n['warn']} warnings" + (f", {allowed} allowed by `nostopit: allow`" if allowed else ""))
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="nostopit", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", default=None, help="repository root (default: git toplevel of the cwd)")
    ap.add_argument("--off", action="append", default=[], metavar="RULE", help="switch a rule off (repeatable)")
    ap.add_argument("--exclude", action="append", default=[], metavar="GLOB", help="skip files matching the glob (repeatable)")
    ap.add_argument("--fail-on", choices=LEVELS, default="error", help="exit non-zero at this level (default error)")
    ap.add_argument("--format", choices=("text", "json"), default="text")
    ap.add_argument("--hook", action="store_true", help="hook mode: findings on stderr, exit 2 when failing")
    sub = ap.add_subparsers(dest="cmd")
    d = sub.add_parser("diff")
    d.add_argument("--base", default="HEAD")
    d.add_argument("--staged", action="store_true")
    d.add_argument("--no-untracked", action="store_true")
    sub.add_parser("file").add_argument("paths", nargs="+")
    sub.add_parser("commit-msg").add_argument("file")
    sub.add_parser("hook")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    root = a.root or toplevel(os.getcwd())
    out = sys.stderr if a.hook else sys.stdout
    fail_on, allowed = a.fail_on, 0

    if a.cmd == "hook":
        try:
            event = json.loads(sys.stdin.read() or "{}")
        except ValueError:
            return 0
        root = toplevel(event.get("cwd") or root)
        kind, arg = hook_plan(event)
        if kind == "send":
            reason = send_block(arg)
            if reason:
                print(reason, file=sys.stderr)
                return 2
            return 0
        if kind == "file":
            found, allowed = checks.collect(file_diff(root, [arg]), root, a.off, a.exclude)
            fail_on = "warn"
        elif kind == "diff":
            found, allowed = checks.collect(build_diff(root), root, a.off, a.exclude)
        else:
            return 0
        out = sys.stderr
    elif a.cmd == "diff":
        found, allowed = checks.collect(build_diff(root, a.base, a.staged, not a.no_untracked), root, a.off, a.exclude)
    elif a.cmd == "file":
        found, allowed = checks.collect(file_diff(root, a.paths), root, a.off, a.exclude)
    elif a.cmd == "commit-msg":
        found = [f for f in checks.commit_message(pathlib.Path(a.file).read_text(errors="replace")) if f.rule not in a.off]
    else:
        ap.print_help()
        return 0

    failing = [f for f in found if LEVELS[f.level] <= LEVELS[fail_on]]
    if found or not a.hook:
        print(render(found, allowed, a.format), file=out)
    if not failing:
        return 0
    return 2 if a.cmd == "hook" or a.hook else 1


def selftest():
    c = checks
    diff = ("diff --git a/NOTES.md b/NOTES.md\nnew file mode 100644\n@@ -0,0 +1 @@\n+# Summary\n"
            "diff --git a/a.py b/a.py\n@@ -1,0 +1,11 @@\n+def f(x):\n+    try:\n+        g()\n+    except Exception:\n"
            "+        print('\u2705 ok')  # reviewer asked for this, see IVE-2028\n+# x = compute(y)\n+# increment x by one\n+def parse_old():\n"  # nostopit: allow
            "+    pass  # TODO\n+class VeryLongNameWithManyWordsInside:\n+    pass  # TODO: drop after the migration, since callers still import it\n"  # nostopit: allow
            "diff --git a/PR.md b/PR.md\n@@ -1,0 +1,3 @@\n+thoroughly tested\n+## Caveats\n+fine\n")
    with tempfile.TemporaryDirectory() as tmp:
        found, allowed = c.collect(diff, tmp)
        rules = sorted(f.rule for f in found)
        assert rules == ["adverb_claim", "broad_except", "caveat_heading", "commented_code", "emoji", "leftover_name", "long_name",
                         "provenance_comment", "summary_file", "todo_without_reason"], rules
        assert allowed == 0 and {f.level for f in found if f.rule in ("emoji", "summary_file")} == {"error"}
        found, allowed = c.collect(diff.replace("except Exception:", "except Exception:  # nostopit: allow broad_except"), tmp)
        assert allowed == 1 and "broad_except" not in {f.rule for f in found}
        found, allowed = c.collect(diff.replace("# reviewer asked", "# nostopit: allow emoji; reviewer asked"), tmp)
        assert allowed == 1 and "emoji" not in {f.rule for f in found} and "provenance_comment" in {f.rule for f in found}
        found, _ = c.collect(diff, tmp, off=["emoji", "summary_file"])
        assert "emoji" not in {f.rule for f in found} and {f.level for f in found} == {"warn"}
        assert c.collect("diff --git a/a.py b/a.py\n@@ -1,0 +1,1 @@\n" + "+x = 1\n" * 401, tmp)[0][-1].rule == "big_diff"
    # Benchmark counters keep their old shapes.
    assert c.style("diff --git a/a.py b/a.py\n+def f():\n+    \"\"\"Doc.\"\"\"\n+# increment\n+    url = 'http://x/#a'\n+#!/usr/bin/env python\n") == \
        {"comments": 1, "docstrings": 1, "emoji": 0, "broad_except": 0, "leftovers": 0, "new_md": 0}
    assert c.prose("diff --git a/PR.md b/PR.md\n+" + " ".join(["w"] * 40) + "\n+\n+- carefully reviewed\n+**Notes:**\n") == \
        {"adverb_claims": 1, "caveat_heads": 1, "paragraphs": 1, "words": 44}
    # Checks that need a repository: stale mentions, duplicated versions, tests, dependencies.
    with tempfile.TemporaryDirectory() as tmp:
        g = lambda *a: subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", *a], cwd=tmp, check=True, capture_output=True)
        w = lambda p, s: (pathlib.Path(tmp, p).parent.mkdir(parents=True, exist_ok=True), pathlib.Path(tmp, p).write_text(s))
        g("init", "-q")
        w("app.py", "import argparse\ndef load_items(path):\n    return []\n\nMAX_ROWS = 10\nargparse.ArgumentParser().add_argument('--max-rows')\n")
        w("README.md", "Call load_items() then read MAX_ROWS or pass --max-rows.\n")
        w("plugin.json", '{"version": "1.0.0"}\n')
        w("other.json", '{"name": "x", "version": "1.0.0"}\n')
        w("tests/test_app.py", "from unittest import mock\n\ndef test_noop():\n    x = 1\n\ndef test_mock():\n    m = mock.Mock()\n    m(1)\n    m.assert_called_once_with(1)\n\n"
                              "def test_real():\n    m = mock.Mock(return_value=3)\n    assert m(1) == 3\n    assert m.call_count == 1\n")
        g("add", "."), g("commit", "-q", "-m", "seed")
        w("app.py", "import argparse\ndef read_items(path):\n    return []\n\nROW_LIMIT = 10\nargparse.ArgumentParser().add_argument('--row-limit')\n")
        w("plugin.json", '{"version": "1.1.0"}\n')
        w("pyproject.toml", '[project]\nname = "x"\nversion = "1.0"\nlicense = {text = "MIT"}\ndependencies = [\n    "httpx>=0.27",\n]\n')
        w("tests/test_app.py", pathlib.Path(tmp, "tests/test_app.py").read_text().replace("    x = 1\n", "    x = 2\n").replace("m(1)\n    m.assert", "m(1)\n    m(1)\n    m.assert")
          .replace("== 3\n", "== 3  # ok\n"))
        w("requirements.txt", "requests==2.32\n")
        w("PLAN.md", "# Plan\n")
        found, _ = c.collect(build_diff(tmp), tmp)
        by = {f.rule: f for f in found}
        assert {"stale_mention", "duplicated_version", "assertless_test", "mock_only_test", "new_dependency", "summary_file"} <= set(by), sorted(by)
        assert "README.md:1" in by["stale_mention"].msg and "other.json:1" in by["duplicated_version"].msg
        assert "test_real" not in str(found) and by["mock_only_test"].msg.startswith("every assertion in `test_mock`")
        names = sorted(f.msg.split("`")[1] for f in found if f.rule == "stale_mention")
        assert names == ["--max-rows", "MAX_ROWS", "load_items"], names
        assert "ROW_LIMIT" not in str(found)
        deps = sorted(f.msg.split("`")[1] for f in found if f.rule == "new_dependency")
        assert deps == ["httpx", "requests"], deps
        found, _ = c.collect(file_diff(tmp, [str(pathlib.Path(tmp, "requirements.txt"))]), tmp)
        assert [f.rule for f in found] == ["new_dependency"], found
    msg = c.commit_message("Add the thing and also do several other things that make this subject line far too long to read\n\n" + " ".join(["word"] * 45) + "\n\n- carefully tested\n")
    assert sorted(f.rule for f in msg) == ["adverb_claim", "commit_paragraph", "commit_subject"], msg
    assert c.commit_message("Add checks\n\n- what changed\n- why\n- how it was tested\n\nsim: https://example/T-1\n") == []
    assert send_block("git push -u origin x") and send_block("gh pr create --fill") and send_block("cr --publish")
    assert not send_block("git log --format=%cr") and not send_block("gh pr view 16") and not send_block("NOSTOPIT_ALLOW_SEND=1 git push")
    assert hook_plan({"hook_event_name": "PreToolUse", "tool_input": {"command": "ls"}}) == ("send", "ls")
    assert hook_plan({"hook_event_name": "PostToolUse", "tool_input": {"file_path": "a.py"}}) == ("file", "a.py")
    assert hook_plan({"hook_event_name": "postToolUse", "tool_name": "shell", "tool_response": {}}) == ("diff", None)
    assert hook_plan({"hook_event_name": "Stop", "stop_hook_active": True}) == (None, None) and hook_plan({"hook_event_name": "Stop"}) == ("diff", None)
    print("nostopit selftest ok")
    return 0
