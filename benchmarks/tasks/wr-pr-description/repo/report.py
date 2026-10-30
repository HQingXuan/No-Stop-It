import csv, sys
from collections import defaultdict


def totals(path):
    out = defaultdict(int)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            out[row["region"]] += int(row["amount"])
    return dict(out)


if __name__ == "__main__":
    for region, total in sorted(totals(sys.argv[1]).items()):
        print(f"{region} {total}")
