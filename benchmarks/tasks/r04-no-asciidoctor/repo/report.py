import argparse, csv, sys


def rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    a = ap.parse_args(argv)
    total = sum(int(r["amount"]) for r in rows(a.csv))
    print(f"total {total}")


if __name__ == "__main__":
    main()
