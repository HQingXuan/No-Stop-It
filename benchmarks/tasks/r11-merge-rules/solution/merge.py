import copy


def merge(base, override):
    """See docs/merge.md."""
    out = copy.deepcopy(base)
    for key, val in override.items():
        if key.startswith("!"):
            out[key[1:]] = copy.deepcopy(val)
        elif val is None:
            out.pop(key, None)
        elif isinstance(val, dict) and isinstance(out.get(key), dict):
            out[key] = merge(out[key], val)
        elif isinstance(val, list) and isinstance(out.get(key), list):
            out[key] = out[key] + [v for v in val if v not in out[key]]
        else:
            out[key] = copy.deepcopy(val)
    return out
