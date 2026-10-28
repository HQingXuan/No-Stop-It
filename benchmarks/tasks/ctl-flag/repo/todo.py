import argparse, json, pathlib

DB = pathlib.Path(__file__).with_name("todos.json")


def load():
    return json.loads(DB.read_text())


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    a = ap.parse_args(argv)
    if a.cmd == "list":
        for t in load():
            print(f"[{'x' if t['done'] else ' '}] {t['title']}")


if __name__ == "__main__":
    main()
