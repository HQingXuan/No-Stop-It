import argparse, csv, json, os, pathlib, sys

STORE = pathlib.Path(os.environ.get("KV_STORE") or pathlib.Path(__file__).with_name("store.json"))


def load():
    return json.loads(STORE.read_text()) if STORE.exists() else {"values": {}, "history": {}}


def save(data):
    STORE.write_text(json.dumps(data, indent=1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("set"); s.add_argument("key"); s.add_argument("value")
    for name in ("get", "del", "history"):
        sub.add_parser(name).add_argument("key")
    sub.add_parser("list").add_argument("--prefix", default="")
    sub.add_parser("export").add_argument("--format", choices=["csv", "json"], required=True)
    a = ap.parse_args(argv)
    data = load()
    values, history = data["values"], data["history"]
    if a.cmd in ("get", "del", "history") and a.key not in values:
        sys.exit("error: no such key")
    if a.cmd == "set":
        if a.key in values:
            history.setdefault(a.key, []).append(values[a.key])
        values[a.key] = a.value
        save(data)
    elif a.cmd == "get":
        print(values[a.key])
    elif a.cmd == "del":
        values.pop(a.key)
        history.pop(a.key, None)
        save(data)
    elif a.cmd == "history":
        print("\n".join(history.get(a.key, []) + [values[a.key]]))
    elif a.cmd == "list":
        print("\n".join(k for k in sorted(values) if k.startswith(a.prefix)))
    elif a.format == "json":
        print(json.dumps(values))
    else:
        w = csv.writer(sys.stdout, lineterminator="\n")
        w.writerow(["key", "value"])
        w.writerows(sorted(values.items()))


if __name__ == "__main__":
    main()
