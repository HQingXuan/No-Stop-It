import re
from datetime import timedelta

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]  # date.weekday() order


def slugify(s):
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", s.lower().strip()))


def clamp(x, lo, hi):
    return min(hi, max(lo, x))


def chunk(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]


def parse_relative(text, base):
    """Port of legacy.js parseRelative: base is a date, returns a date."""
    t = text.strip().lower()
    simple = {"today": 0, "yesterday": -1, "tomorrow": 1}
    if t in simple:
        return base + timedelta(days=simple[t])
    if m := re.fullmatch(r"(\d+) (day|week)s? ago", t):
        return base - timedelta(days=int(m[1]) * (7 if m[2] == "week" else 1))
    if m := re.fullmatch(r"in (\d+) (day|week)s?", t):
        return base + timedelta(days=int(m[1]) * (7 if m[2] == "week" else 1))
    if (m := re.fullmatch(r"(next|last) (\w+)", t)) and m[2] in DAYS:
        target, now = DAYS.index(m[2]), base.weekday()
        if m[1] == "next":
            return base + timedelta(days=(target - now) % 7 or 7)
        return base - timedelta(days=(now - target) % 7 or 7)
    raise ValueError(f"cannot parse: {text}")
