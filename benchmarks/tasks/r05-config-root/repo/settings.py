import configparser, pathlib

_cfg = configparser.ConfigParser()
_cfg.read(pathlib.Path(__file__).with_name("config") / "defaults.ini")
TAX = float(_cfg["pricing"]["tax_percent"]) / 100
CURRENCY = _cfg["pricing"]["currency"]
