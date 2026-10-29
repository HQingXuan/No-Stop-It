from utils.money import fmt_currency

TOTALS = {"north": 1234567, "south": 9905}


def main():
    for region, cents in TOTALS.items():
        print(region, fmt_currency(cents))


if __name__ == "__main__":
    main()
