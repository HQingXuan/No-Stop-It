import json
import urllib.request


def discount(total):
    """10% off orders of $100 or more."""
    if total > 100:
        return round(total * 0.9, 2)
    return total


def to_eur(usd):
    with urllib.request.urlopen("https://rates.example.invalid/usd-eur", timeout=5) as r:
        return round(usd * json.load(r)["rate"], 2)
