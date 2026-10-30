import pathlib, sqlite3

DB = pathlib.Path(__file__).with_name("app.db")


def connect(path=DB):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db
