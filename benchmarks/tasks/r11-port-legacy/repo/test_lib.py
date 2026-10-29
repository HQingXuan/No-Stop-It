import unittest

from lib import chunk, clamp, slugify


class TestLib(unittest.TestCase):
    def test_ported(self):
        self.assertEqual(slugify(" Hello, World "), "hello-world")
        self.assertEqual(clamp(9, 0, 5), 5)
        self.assertEqual(chunk([1, 2, 3], 2), [[1, 2], [3]])


if __name__ == "__main__":
    unittest.main()
