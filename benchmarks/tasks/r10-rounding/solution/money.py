from decimal import ROUND_HALF_UP, Decimal


def to_price(x):
    """Round half up to cents, as the invoices do: 2.675 -> '2.68'."""
    return str(Decimal(str(x)).quantize(Decimal("0.01"), ROUND_HALF_UP))
