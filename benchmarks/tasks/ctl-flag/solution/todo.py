import argparse, json, pathlib

DB = pathlib.Path(__file__).with_name("todos.json")


def load():
    return json.loads(DB.read_text())


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list")
    ls.add_argument("--done", action="store_true")
    ls.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "list":
        items = [t for t in load() if t["done"] or not a.done]
        if a.json:
            print(json.dumps(items))
        else:
            for t in items:
                print(f"[{'x' if t['done'] else ' '}] {t['title']}")


if __name__ == "__main__":
    main()
