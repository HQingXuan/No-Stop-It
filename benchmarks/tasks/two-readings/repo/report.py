ENTRIES = [
    {"date": "2026-03-02", "amount": 120, "what": "invoice sent"},
    {"date": "2026-01-15", "amount": 9800, "what": "account opened"},
    {"date": "2026-02-20", "amount": 450, "what": "first order"},
]


def main():
    for e in ENTRIES:
        print(e["date"], e["amount"], e["what"])


if __name__ == "__main__":
    main()
