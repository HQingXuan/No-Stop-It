import json, pathlib

FILE = pathlib.Path(__file__).with_name("rates.json")
RATES = json.loads(FILE.read_text())


def reload(path=None):
    global RATES
    RATES = json.loads(pathlib.Path(path or FILE).read_text())
