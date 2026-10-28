ENTRIES = [
    ("2026-03-02", "invoice sent"),
    ("2026-01-15", "account opened"),
    ("2026-02-20", "first order"),
]


def main():
    for date, what in ENTRIES:
        print(date, what)


if __name__ == "__main__":
    main()
