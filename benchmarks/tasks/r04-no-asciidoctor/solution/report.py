import argparse, csv, sys


def rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--since", help="skip rows before this YYYY-MM-DD date")
    a = ap.parse_args(argv)
    total = sum(int(r["amount"]) for r in rows(a.csv) if not a.since or r["date"] >= a.since)
    print(f"total {total}")


if __name__ == "__main__":
    main()
