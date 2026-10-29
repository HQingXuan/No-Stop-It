import argparse, json, os, pathlib

STORE = pathlib.Path(os.environ.get("KV_STORE") or pathlib.Path(__file__).with_name("store.json"))


def load():
    return json.loads(STORE.read_text()) if STORE.exists() else {}


def save(data):
    STORE.write_text(json.dumps(data, indent=1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("set"); s.add_argument("key"); s.add_argument("value")
    g = sub.add_parser("get"); g.add_argument("key")
    a = ap.parse_args(argv)
    data = load()
    if a.cmd == "set":
        data[a.key] = a.value
        save(data)
    elif a.cmd == "get":
        print(data[a.key])


if __name__ == "__main__":
    main()
