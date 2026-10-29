import unittest

import orders


class TestOrders(unittest.TestCase):
    def test_total(self):
        self.assertEqual(orders.load()[0].total(), 200)


if __name__ == "__main__":
    unittest.main()
