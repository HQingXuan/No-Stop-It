import json
import pathlib

DATA = pathlib.Path(__file__).parent / "data" / "users.json"


def count_users():
    return len(json.loads(DATA.read_text()))
