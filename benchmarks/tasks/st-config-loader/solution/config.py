import json

DEFAULTS = {"port": 8080, "debug": False}


def load_config(path):
    with open(path) as f:
        cfg = DEFAULTS | json.load(f)
    port = cfg["port"]
    if not isinstance(port, int) or isinstance(port, bool) or not 1 <= port <= 65535:
        raise ValueError(f"port must be an integer from 1 to 65535, got {port!r}")
    return cfg
