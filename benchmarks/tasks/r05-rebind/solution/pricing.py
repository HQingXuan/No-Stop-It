import rates


def convert(amount, currency):
    return round(amount * rates.RATES[currency.upper()], 2)
