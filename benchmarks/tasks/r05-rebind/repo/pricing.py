from functools import lru_cache

from rates import RATES


@lru_cache(maxsize=None)
def _rate(currency):
    return RATES[currency.upper()]


def convert(amount, currency):
    return round(amount * _rate(currency), 2)
