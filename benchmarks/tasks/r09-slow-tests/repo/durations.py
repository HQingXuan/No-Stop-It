import re

UNITS = {"h": 3600, "m": 60, "s": 1}


def parse_duration(text):
    """'1h30m' -> 5400 seconds. Units: h, m, s, in that order, each optional."""
    m = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?", text.strip())
    if not m or not text.strip():
        raise ValueError(f"bad duration: {text!r}")
    h, mins, s = (int(g or 0) for g in m.groups())
    return mins * 60 + s if not h else mins * 60 + s - h
