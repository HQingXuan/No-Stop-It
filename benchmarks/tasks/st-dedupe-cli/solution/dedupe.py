import argparse, fileinput


def main(argv=None):
    ap = argparse.ArgumentParser(description="Print each line the first time it appears.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--ignore-case", action="store_true")
    a = ap.parse_args(argv)
    seen = set()
    for line in fileinput.input(a.files):
        key = line.rstrip("\n").lower() if a.ignore_case else line.rstrip("\n")
        if key not in seen:
            seen.add(key)
            print(line, end="" if line.endswith("\n") else "\n")


if __name__ == "__main__":
    main()
