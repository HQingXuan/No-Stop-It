import unittest

from store import list_items


class TestStore(unittest.TestCase):
    def test_first(self):
        self.assertEqual(list_items()[0], "item-1")


if __name__ == "__main__":
    unittest.main()
