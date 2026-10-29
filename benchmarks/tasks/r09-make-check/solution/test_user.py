import unittest

from user import User


class TestUser(unittest.TestCase):
    def test_fields(self):
        self.assertEqual(User(1, "Ada", "ada@example.com", "+44 20 7946 0000").name, "Ada")


if __name__ == "__main__":
    unittest.main()
