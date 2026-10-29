def to_price(x):
    """Round half up to cents, as the invoices do: 2.675 -> '2.68'."""
    return f"{round(x, 2):.2f}"
