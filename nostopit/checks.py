"""Checks over a unified diff: the enforceable half of the No-Stop-It rules.

The CLI runs them from agent hooks and pre-commit; benchmarks/score.py counts habits with the same regexes.
Each check returns Findings whose message says what to do instead, not only what is wrong.
"""
import ast, collections, fnmatch, pathlib, re, subprocess

Finding = collections.namedtuple("Finding", "rule level path line msg")

# Habit counters on added lines of code files, shared with the benchmark scorer. Each runs on "+" + line.
STYLE = {"comments": re.compile(r"^\+(?!\+\+)(\s*|.*\s)#(?!!)\s", re.M),
         "emoji": re.compile(r"^\+.*[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50]", re.M),
         "broad_except": re.compile(r"^\+\s*except\s*(\(?\s*(Base)?Exception\b[^:]*)?:", re.M),
         "leftovers": re.compile(r"^\+.*(\b(def|class)\s+\w+_(old|v2|new|legacy)\b|\bTODO\b|\bFIXME\b)", re.M)}
# Prose counters on added lines of .md files and commit messages.
PROSE = {"adverb_claims": re.compile(r"\b(thoroughly|carefully|fully|rigorously|extensively|comprehensively|properly)\s+(test|check|review|verif|validat|cover|handl)\w*|\brobust\w*", re.I),
         "caveat_heads": re.compile(r"^(#+\s*|\*\*)?(caveats?|notes?|disclaimers?|limitations?|assumptions?)(:?\*\*)?:?\s*$", re.I | re.M)}

COMMENT = re.compile(r"(?:^|\s)(?:#(?!!)|//|/\*)\s*(.*)|^\s*\*\s+(.*)")
HISTORY = re.compile(r"\b(reviewers?|review comments?|per review|as requested|previously|updated to|now uses|was changed|changed from|refactored (?:to|from)|moved (?:from|here from)|originally)\b", re.I)
TICKET = re.compile(r"\b(?!(?:SHA|ISO|UTF|RFC|CVE|UTC|IEEE|HTTP|OAUTH|TLS|AES)-)[A-Z][A-Z0-9]{1,9}-\d{2,}\b")
LEFTOVER_NAME = re.compile(r"\b(?:def|class|function|const|let|var)\s+(\w+_(?:old|v2|new|legacy))\b")
LEFTOVER_TODO = re.compile(r"(?:(?:^|\s)#|(?:^|\s)//|/\*|^\s*\*)\s*.*?\b(TODO|FIXME)\b(.*)")
DEFINITION = re.compile(r"\b(?:def|class|function|fn|func|struct|interface|enum|trait|const|let|var|val|type)\s+([A-Za-z_]\w*)")
SUMMARY_FILE = re.compile(r"(?i)(?:^|/)(?:summary|implementation|changes|notes|plan|progress|status|todo)[\w-]*\.md$")
MOCK_WORDS = re.compile(r"\.(?:assert_(?:called|any_call|has_calls|not_called|awaited)\w*|called\b|call_count|call_args\w*|mock_calls|await_count)")
VERSION = re.compile(r'(?i)(?:"?version"?\s*[:=]\s*|__version__\s*=\s*|<version>)["\']?(\d+\.\d+(?:\.\d+)*(?:[-+.][\w.]+)?)')
MANIFESTS = {"package.json", "pyproject.toml", "setup.py", "setup.cfg", "Cargo.toml", "plugin.json", "marketplace.json", "manifest.json",
             "gemini-extension.json", "composer.json", "pubspec.yaml", "Chart.yaml", "pom.xml", "build.gradle", "VERSION", "version.py", "__init__.py"}
DEPENDENCY = {"package.json": (re.compile(r'^\s*"([@\w./-]+)"\s*:\s*"(?:[\^~>=<*]|\d|latest|workspace:|file:|git|npm:|link:)'),
                               {"version", "name", "main", "type", "module", "license", "private", "description", "author", "node", "npm", "packageManager", "types", "exports"}),
              "pyproject.toml": (re.compile(r'^\s*"([A-Za-z0-9_.-]+)\s*(?:[>=<~!]|\[|"\s*,?\s*$)|^\s*([A-Za-z0-9_.-]+)\s*=\s*(?:"[\^~>=<\d*]|\{\s*(?:version|git|path|url|extras|optional|features|workspace)\b)'),
                                 {"python", "requires-python", "name", "version", "license"}),
              "Cargo.toml": (re.compile(r'^\s*([A-Za-z0-9_-]+)\s*=\s*(?:"\d|\{\s*(?:version|git|path|features|workspace|optional)\b)'), {"name", "version", "edition", "rust-version"}),
              "go.mod": (re.compile(r"^\s*([\w./-]+)\s+v\d"), set()),
              "Gemfile": (re.compile(r"""^\s*gem\s+["']([^"']+)"""), set())}
GREP_EXCLUDE = [":(exclude)*.lock", ":(exclude)package-lock.json", ":(exclude)CHANGELOG*", ":(exclude)HISTORY*", ":(exclude)docs/decisions.md"]
CODE_STATEMENTS = (ast.Assign, ast.AugAssign, ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.With, ast.Raise)
STOP_NAMES = {"main", "init", "index", "test", "tests", "setup", "utils", "util", "config", "app", "mod", "lib", "self", "none", "true", "false"}


def files(diff):
    """Per file in the diff: (path, status, added, removed), where added and removed are (line number, text)."""
    for block in re.split(r"(?=^diff --git )", diff, flags=re.M):
        head = re.match(r"diff --git a/(.+?) b/(.+)\n", block)
        if not head:
            continue
        status = "new" if re.search(r"^new file mode", block, re.M) else "deleted" if re.search(r"^deleted file mode", block, re.M) else "modified"
        rename = re.search(r"^rename from (.+)$", block, re.M)
        status = f"renamed {rename.group(1)}" if rename else status
        added, removed, new, old, in_hunk = [], [], 0, 0, False
        for line in block.split("\n")[1:]:
            hunk = re.match(r"@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@", line)
            if hunk:
                old, new, in_hunk = int(hunk.group(1)), int(hunk.group(2)), True
            elif not in_hunk or line.startswith("\\"):
                continue
            elif line.startswith("+"):
                added.append((new, line[1:]))
                new += 1
            elif line.startswith("-"):
                removed.append((old, line[1:]))
                old += 1
            else:
                new, old = new + 1, old + 1
        yield head.group(2), status, added, removed


def blocks(lines):
    """Paragraphs: runs of lines that are not bullets, quotes, tables or headings, joined."""
    out, run = [], []
    for line in lines + [""]:
        if line.strip() and not re.match(r"\s*([-*>|#]|\d+\.)", line):
            run.append(line)
        else:
            out.append(" ".join(run))
            run = []
    return out


def style(diff):
    """Counts of each STYLE habit in added lines of code files, plus new .md files."""
    code = "".join(f for f in re.split(r"(?=^diff --git )", diff, flags=re.M) if not re.match(r"diff --git \S+ \S+\.md\n", f))
    out = {k: len(r.findall(code)) for k, r in STYLE.items()}
    out["docstrings"] = sum(len(re.findall(r'"""|\'\'\'', line)) for line in code.splitlines() if line.startswith("+")) // 2
    out["new_md"] = len(re.findall(r"^diff --git a/\S+\.md b/\S+\nnew file mode", diff, re.M))
    return out


def prose(diff):
    """Counts of each PROSE habit in added lines of .md files outside code fences, paragraphs of 40 words or more, and words."""
    md = "".join(f for f in re.split(r"(?=^diff --git )", diff, flags=re.M) if re.match(r"diff --git \S+ \S+\.md\n", f))
    lines, fenced = [], False
    for line in md.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        if line[1:].lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            lines.append(line[1:])
    text = "\n".join(lines)
    out = {k: len(r.findall(text)) for k, r in PROSE.items()}
    return out | {"paragraphs": sum(len(b.split()) >= 40 for b in blocks(lines)), "words": len(text.split())}


def git(root, *args):
    """stdout of a git command, or "" when git fails or is absent (git grep exits 1 on no match, which is not a failure)."""
    try:
        p = subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=root, capture_output=True, text=True, errors="replace")
    except OSError:
        return ""
    return p.stdout if p.returncode in (0, 1) else ""


def grep(root, token, *exclude):
    """Working-tree lines still mentioning token as a whole word, as "path:line", outside lockfiles and changelogs."""
    out = git(root, "grep", "-I", "-n", "-w", "-F", "--untracked", "-e", token, "--", ".", *GREP_EXCLUDE, *(f":(exclude){p}" for p in exclude))
    return [":".join(l.split(":", 2)[:2]) for l in out.splitlines() if l.count(":") >= 2]


def words(name):
    return [w for seg in name.split("_") for w in re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z0-9]+|[A-Z]+", seg)]


def line_checks(path, status, added):
    """Checks that need one added line at a time."""
    out = []
    if status == "new" and SUMMARY_FILE.search(path):
        out.append(Finding("summary_file", "error", path, 0, "a notes file nobody asked for; put the summary in your reply and delete the file"))
    is_md, is_py = path.endswith((".md", ".rst", ".txt")), path.endswith(".py")
    for n, text in added:
        if STYLE["emoji"].search("+" + text):
            out.append(Finding("emoji", "error", path, n, "emoji; use the plain word"))
        if is_md:
            if PROSE["adverb_claims"].search(text):
                out.append(Finding("adverb_claim", "warn", path, n, "an adverb stands in for evidence; name the acts: ran X, read Y, did not run Z"))
            if PROSE["caveat_heads"].search(text):
                out.append(Finding("caveat_heading", "warn", path, n, "a caveats section buries the finding; state the fact in one footnote"))
            continue
        if STYLE["broad_except"].search("+" + text):
            out.append(Finding("broad_except", "warn", path, n, "catches everything; catch the one exception this code can handle, let the rest raise"))
        m = LEFTOVER_NAME.search(text)
        if m:
            out.append(Finding("leftover_name", "warn", path, n, f"`{m.group(1)}` keeps an old version alive; delete it and update its callers"))
        m = LEFTOVER_TODO.search(text)
        if m and not re.search(r"\b\w+\b.*\b(because|since|when|after|until|blocked|needs|waiting)\b", m.group(2)):
            out.append(Finding("todo_without_reason", "warn", path, n, f"{m.group(1)} without a reason; say what is missing and why, or do it now"))
        m = DEFINITION.search(text)
        if m and not m.group(1).startswith(("test", "__")) and len(words(m.group(1))) > 4:
            out.append(Finding("long_name", "warn", path, n, f"`{m.group(1)}` is {len(words(m.group(1)))} words; name what it holds, as long as its neighbors' names"))
        c = COMMENT.search(text)
        body = re.sub(r"\s*\*/\s*$", "", (c.group(1) or c.group(2) or "")).strip() if c else ""
        body = re.sub(r"nostopit:\s*allow\b[\w ,]*;?", "", body).strip()
        if not body or body.lower().startswith(("noqa", "type:", "pragma", "pylint", "eslint", "shortcut:")):
            continue
        if HISTORY.search(body) or TICKET.search(body):
            out.append(Finding("provenance_comment", "warn", path, n, "comment describes the change, its review or its ticket; describe the code as it is now, the rest goes in the commit message"))
        if looks_like_code(body, is_py):
            out.append(Finding("commented_code", "warn", path, n, "commented-out code; delete it, git keeps it"))
    return out


def looks_like_code(body, is_py):
    if re.match(r"(?i)(?:todo|fixme|note|see |e\.g|i\.e|https?:)", body):
        return False
    if is_py:
        try:
            tree = ast.parse(body)
        except (SyntaxError, ValueError):
            return False
        return any(isinstance(s, CODE_STATEMENTS) or (isinstance(s, ast.Expr) and isinstance(s.value, ast.Call)) for s in tree.body)
    return bool(re.search(r"[;{}]\s*$", body) or re.match(r"(?:const|let|var|return|if|for|while|console\.|import |export |function\b)\s", body))


def test_checks(root, path, added):
    """Tests touched by the diff that cannot fail: no assertion, or only assertions about a mock."""
    if not path.endswith(".py") or not re.search(r"(^|/)test_[^/]*\.py$|_test\.py$|(^|/)tests?/", path):
        return []
    try:
        src = (pathlib.Path(root) / path).read_text(errors="replace")
        tree = ast.parse(src)
    except (OSError, SyntaxError, ValueError):
        return []
    touched = {n for n, _ in added}
    out = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) or not node.name.startswith("test"):
            continue
        if not any(node.lineno <= n <= (node.end_lineno or node.lineno) for n in touched):
            continue
        asserts = []
        for s in ast.walk(node):
            if isinstance(s, ast.Assert):
                asserts.append(ast.get_source_segment(src, s) or "")
            elif isinstance(s, ast.Expr) and isinstance(s.value, ast.Call) and (
                    isinstance(s.value.func, ast.Attribute) and s.value.func.attr.startswith("assert")
                    or isinstance(s.value.func, ast.Name) and (s.value.func.id.startswith("assert") or s.value.func.id in ("expect", "verify"))):
                asserts.append(ast.get_source_segment(src, s) or "")
            elif isinstance(s, ast.With) and any(isinstance(i.context_expr, ast.Call) and re.search(r"raises|assertRaises|warns", ast.dump(i.context_expr.func)) for i in s.items):
                asserts.append("raises")
        if not asserts:
            out.append(Finding("assertless_test", "error", path, node.lineno, f"`{node.name}` has no assertion, so it cannot fail; assert on the result or the state the code changed"))
        elif all(MOCK_WORDS.search(a) for a in asserts):
            out.append(Finding("mock_only_test", "error", path, node.lineno, f"every assertion in `{node.name}` is about the mock; assert on the result or the state the code changed"))
    return out


def mentions(name, text):
    """Whole-token occurrence; `\\b` alone misses `--flag`, whose dash is not a word character."""
    return re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", text) is not None


def identifier_shaped(name):
    """Not a plain English word: has an underscore, a camel hump or a flag dash, so grep hits are code, not prose."""
    return bool(re.search(r"_|-|[a-z][A-Z]", name)) and len(name) >= 4 and name.lower() not in STOP_NAMES


def stale_mentions(root, diff_files):
    """Definitions, flags and files removed or renamed by the diff whose names still appear elsewhere in the working tree."""
    plus = "\n".join(t for _, _, added, _ in diff_files for _, t in added)
    out, seen = [], set()
    for path, status, _, removed in diff_files:
        gone = status[8:] if status.startswith("renamed ") else path if status == "deleted" else ""
        names = [pathlib.Path(gone).stem] if gone and pathlib.Path(gone).stem != pathlib.Path(path).stem else []
        for _, text in removed:
            names += DEFINITION.findall(text) + re.findall(r"^\s*([A-Z][A-Z0-9_]{3,})\s*[:=]", text) + re.findall(r"^(\w{5,})\s*=", text)
            if re.search(r"add_argument\(|add_option\(|\.option\(|\.flag\(|flag\.\w+\(", text):
                names += re.findall(r"""["'](--[a-z][a-z0-9-]{2,})["']""", text)
        for name in names:
            if name in seen or not identifier_shaped(name) or mentions(name, plus):
                continue
            seen.add(name)
            hits = grep(root, name)
            if hits:
                out.append(Finding("stale_mention", "warn", path, 0, f"`{name}` was removed here but still appears in {', '.join(hits[:3])}{f' and {len(hits) - 3} more' if len(hits) > 3 else ''}; fix every mention in this change"))
            if len(seen) >= 30:
                return out
    return out


def duplicated_versions(root, diff_files):
    """A version changed in one manifest while the old value remains in another."""
    out = []
    for path, _, added, removed in diff_files:
        if pathlib.Path(path).name not in MANIFESTS and "version" not in path.lower():
            continue
        olds = {m.group(1) for _, t in removed for m in [VERSION.search(t)] if m}
        news = {m.group(1) for _, t in added for m in [VERSION.search(t)] if m}
        for old in sorted(olds - news):
            hits = [h for h in grep(root, old, path) if re.search(r"(?i)version", line_at(root, h))]
            if hits:
                out.append(Finding("duplicated_version", "warn", path, 0, f"version {old} -> {', '.join(sorted(news)) or '?'} here, but {old} remains in {', '.join(hits[:3])}; change every copy"))
    return out


def line_at(root, hit):
    path, _, n = hit.rpartition(":")
    try:
        return (pathlib.Path(root) / path).read_text(errors="replace").splitlines()[int(n) - 1]
    except (OSError, IndexError, ValueError):
        return ""


def new_dependencies(diff_files):
    """Dependencies added to a manifest (not bumped). The ponytail rule: never add a dependency for a few lines."""
    out = []
    for path, _, added, removed in diff_files:
        name = pathlib.Path(path).name
        if name.startswith("requirements") and name.endswith(".txt"):
            pattern, skip = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9_.-]*)"), set()
        elif name in DEPENDENCY:
            pattern, skip = DEPENDENCY[name]
        else:
            continue
        old = "\n".join(t for _, t in removed)
        for n, text in added:
            m = pattern.match(text)
            dep = next((g for g in m.groups() if g), None) if m else None
            if dep and dep not in skip and re.search(r"[a-z]", dep) and not mentions(dep, old):
                out.append(Finding("new_dependency", "warn", path, n, f"new dependency `{dep}`; say in the reply why a library beats a few lines, or drop it"))
    return out


def commit_message(text):
    """A one-line subject, then a few short bullets. No paragraphs, no adverbs for evidence."""
    lines = [l for l in text.splitlines() if not l.startswith("#")]
    while lines and not lines[0].strip():
        lines.pop(0)
    if not lines:
        return []
    subject, body = lines[0], lines[1:]
    out = []
    if len(subject) > 72:
        out.append(Finding("commit_subject", "error", "", 1, f"subject is {len(subject)} characters; one line under 72, the rest in bullets"))
    if STYLE["emoji"].search("+" + text):
        out.append(Finding("emoji", "error", "", 1, "emoji; use the plain word"))
    paragraph = any(len(b.split()) >= 40 for b in blocks(body))
    if paragraph:
        out.append(Finding("commit_paragraph", "error", "", 2, "a paragraph in the body; a few short bullets: what changed, why, how it was tested"))
    for i, l in enumerate(body, 2):
        if not paragraph and len(l) > 100 and not re.match(r"\s*([-*]|\d+[.)])\s|[\w-]+:\s", l):
            out.append(Finding("commit_prose", "warn", "", i, "a line of prose where a bullet belongs"))
        if PROSE["adverb_claims"].search(l):
            out.append(Finding("adverb_claim", "warn", "", i, "an adverb stands in for evidence; name what ran and what did not"))
    if sum(bool(l.strip()) for l in body) > 12:
        out.append(Finding("commit_long", "warn", "", 2, f"{sum(bool(l.strip()) for l in body)} body lines; the details are in the diff"))
    return out


def house_names_long(root, path, added):
    """True when the file's existing definitions already run to four words or more, so the codebase's style wins."""
    try:
        text = (pathlib.Path(root) / path).read_text(errors="replace")
    except OSError:
        return False
    new = {t for _, t in added}
    counts = sorted(len(words(n)) for line in text.splitlines() if line not in new for n in DEFINITION.findall(line))
    return bool(counts) and counts[len(counts) // 2] >= 4


def collect(diff, root=".", off=(), exclude=()):
    """All findings for a diff, minus rules switched off, excluded paths and lines carrying `nostopit: allow`. Returns (findings, allowed)."""
    diff_files = [f for f in files(diff) if not any(fnmatch.fnmatch(f[0], g) for g in exclude)]
    found = []
    for path, status, added, removed in diff_files:
        lines = line_checks(path, status, added)
        if house_names_long(root, path, added):
            lines = [f for f in lines if f.rule != "long_name"]
        found += lines + test_checks(root, path, added)
    if git(root, "rev-parse", "--show-toplevel").strip():
        found += stale_mentions(root, diff_files) + duplicated_versions(root, diff_files)
    found += new_dependencies(diff_files)
    changed = sum(len(a) + len(r) for _, _, a, r in diff_files)
    if changed > 400:
        found.append(Finding("big_diff", "warn", "", 0, f"{changed} changed lines; finish the task, then tell the user where it could split (a refactor, a behavior change)"))
    text_at = {(p, n): t for p, _, added, _ in diff_files for n, t in added}
    allowed = [f for f in found if allows(text_at.get((f.path, f.line), ""), f.rule)]
    kept = [f for f in found if f.rule not in off and f not in allowed]
    return sorted(kept, key=lambda f: (f.path, f.line, f.rule)), len(allowed)


def allows(text, rule):
    """`nostopit: allow` on the line allows every rule; `nostopit: allow emoji, long_name` only those."""
    m = re.search(r"nostopit:\s*allow\b((?:[ ,]+\w+)*)", text)
    names = re.findall(r"\w+", m.group(1)) if m else None
    return m is not None and (not names or rule in names)
