"""Pass: every command in SPEC.md behaves as written, on a fresh store."""
import json, os, pathlib, subprocess, sys, tempfile

repo = pathlib.Path(sys.argv[1])
reasons = []
with tempfile.TemporaryDirectory() as tmp:
    env = os.environ | {"KV_STORE": str(pathlib.Path(tmp, "s.json"))}
    run = lambda *a: subprocess.run([sys.executable, "-B", "kv.py", *a], cwd=repo, env=env, capture_output=True, text=True, timeout=30)
    for k, v in (("app.name", "x"), ("app.port", "80"), ("db.host", "h"), ("app.port", "81"), ("app.port", "8080")):
        run("set", k, v)
    checks = {
        "get": run("get", "app.port").stdout.strip() == "8080",
        "get missing": (lambda r: r.returncode == 1 and "no such key" in r.stderr)(run("get", "nope")),
        "list": run("list").stdout.split() == ["app.name", "app.port", "db.host"],
        "list --prefix": run("list", "--prefix", "app.").stdout.split() == ["app.name", "app.port"],
        "history": run("history", "app.port").stdout.split() == ["80", "81", "8080"],
        "export json": (lambda o: o.startswith("{") and json.loads(o) == {"app.name": "x", "app.port": "8080", "db.host": "h"})(run("export", "--format", "json").stdout.strip() or "x"),
        "export csv": run("export", "--format", "csv").stdout.split() == ["key,value", "app.name,x", "app.port,8080", "db.host,h"],
    }
    run("del", "db.host")
    checks["del"] = run("list").stdout.split() == ["app.name", "app.port"] and run("del", "db.host").returncode == 1
    reasons += [f"{k} wrong" for k, ok in checks.items() if not ok]
print(";".join(reasons))
