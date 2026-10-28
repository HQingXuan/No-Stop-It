import unittest

from app import admin, views
from app.users import get_user


class TestApp(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get_user(1), "ada")

    def test_views(self):
        self.assertEqual(views.profile(2), "<h1>linus</h1>")
        self.assertEqual(admin.ban(1), "banned ada")


if __name__ == "__main__":
    unittest.main()
