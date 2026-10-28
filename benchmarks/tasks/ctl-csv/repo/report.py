import sys
from collections import defaultdict


def totals(path):
    out = defaultdict(int)
    with open(path) as f:
        next(f)
        for line in f:
            region, customer, amount = line.strip().split(",")[:3]
            out[region] += int(amount) if amount.strip().isdigit() else 0
    return dict(out)


if __name__ == "__main__":
    for region, total in sorted(totals(sys.argv[1]).items()):
        print(f"{region} {total}")
