import price, settings


def tax_label():
    return f"VAT {settings.TAX * 100:g}%"


def line(name, net):
    return f"{name}: {price.gross(net):.2f} {settings.CURRENCY} ({tax_label()})"
