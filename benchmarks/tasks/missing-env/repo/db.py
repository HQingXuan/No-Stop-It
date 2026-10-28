import os


def dsn():
    return f"postgres://app:{os.environ['DB_PASSWORD']}@db.internal/orders"
