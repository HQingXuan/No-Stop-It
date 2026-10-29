import unittest

from user import User


class TestUser(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(User(1, "Ada", "ada@example.com").name, "Ada")


if __name__ == "__main__":
    unittest.main()
