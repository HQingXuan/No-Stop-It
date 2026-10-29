import re


def slugify(s):
    return re.sub(r"^-|-$", "", re.sub(r"[^a-z0-9]+", "-", s.lower().strip()))


def clamp(x, lo, hi):
    return min(hi, max(lo, x))


def chunk(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]
