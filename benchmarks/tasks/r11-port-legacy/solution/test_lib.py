import unittest
from datetime import date

from lib import chunk, clamp, parse_relative, slugify


class TestLib(unittest.TestCase):
    def test_ported(self):
        self.assertEqual(slugify(" Hello, World "), "hello-world")
        self.assertEqual(clamp(9, 0, 5), 5)
        self.assertEqual(chunk([1, 2, 3], 2), [[1, 2], [3]])

    def test_parse_relative(self):
        wed = date(2026, 10, 28)
        self.assertEqual(parse_relative("in 2 weeks", wed), date(2026, 11, 11))
        self.assertEqual(parse_relative("next wednesday", wed), date(2026, 11, 4))
        self.assertEqual(parse_relative("last monday", wed), date(2026, 10, 26))
        with self.assertRaises(ValueError):
            parse_relative("someday", wed)


if __name__ == "__main__":
    unittest.main()
