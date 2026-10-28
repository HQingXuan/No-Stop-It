import os


def dsn():
    return f"postgres://app:{os.environ['DB_PASSWORD']}@db.internal/orders"


def execute(sql):
    raise RuntimeError(f"no database in this checkout, cannot run against {dsn()}")
