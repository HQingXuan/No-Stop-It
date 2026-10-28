import os
import unittest

import db


class TestDb(unittest.TestCase):
    def test_dsn_uses_password(self):
        self.assertIn(os.environ["DB_PASSWORD"], db.dsn())
