import unittest

from money import to_price


class TestMoney(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(to_price(3), "3.00")
        self.assertEqual(to_price(2.5), "2.50")

    def test_half_up(self):
        self.assertEqual(to_price(2.675), "2.68")
        self.assertEqual(to_price(1.005), "1.01")


if __name__ == "__main__":
    unittest.main()
