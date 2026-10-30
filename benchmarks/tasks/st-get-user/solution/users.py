import pathlib, sqlite3

DB = pathlib.Path(__file__).with_name("app.db")


def connect(path=DB):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db


def get_user(user_id, path=DB):
    with connect(path) as db:
        row = db.execute("select * from users where id = ?", (user_id,)).fetchone()
    if row is None:
        raise KeyError(user_id)
    return dict(row)
