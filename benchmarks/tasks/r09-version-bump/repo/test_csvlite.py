import unittest

from csvlite import parse


class TestParse(unittest.TestCase):
    def test_rows(self):
        self.assertEqual(parse("a, b\n1, 2"), [{"a": "1", "b": "2"}])


if __name__ == "__main__":
    unittest.main()
