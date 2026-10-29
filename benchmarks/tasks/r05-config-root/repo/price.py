import settings


def gross(net):
    return round(net * (1 + settings.TAX), 2)
