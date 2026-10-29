import unittest

from pkg.config import load_config


class TestConfig(unittest.TestCase):
    def test_load(self):
        self.assertEqual(load_config('{"timeout": 5}')["timeout"], 5)


if __name__ == "__main__":
    unittest.main()
