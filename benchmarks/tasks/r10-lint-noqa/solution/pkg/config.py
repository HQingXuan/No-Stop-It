import json, logging

log = logging.getLogger(__name__)


def load_config(text):
    cfg = json.loads(text)
    if "timeout" not in cfg:
        log.warning("config has no timeout, using 30")
        cfg["timeout"] = 30
    return cfg
