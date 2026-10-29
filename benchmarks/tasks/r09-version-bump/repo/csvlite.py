def parse(text):
    header, *rows = text.splitlines()
    keys = [k.strip() for k in header.split(",")]
    return [dict(zip(keys, (v.strip() for v in r.split(",")))) for r in rows]
