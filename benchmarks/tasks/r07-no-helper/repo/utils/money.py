def fmt_currency(cents, symbol="€"):
    """1234567 -> '€12,345.67'"""
    return f"{symbol}{cents // 100:,}.{cents % 100:02d}"
