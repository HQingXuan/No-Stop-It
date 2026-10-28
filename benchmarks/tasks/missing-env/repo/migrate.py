import sys

import db

SQL = "ALTER TABLE orders ADD COLUMN note TEXT;"


def main(argv):
    db.execute(SQL)
    print("migrated")


if __name__ == "__main__":
    main(sys.argv[1:])
