import contextlib, io, unittest

import orders


class TestOrders(unittest.TestCase):
    def test_amount(self):
        self.assertEqual(orders.load()[0].amount, 100)

    def test_discount(self):
        self.assertEqual(orders.load()[2].total(), 60)

    def test_min(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            orders.main(["--min", "50"])
        self.assertEqual([l.split()[0] for l in out.getvalue().splitlines()], ["1", "3"])


if __name__ == "__main__":
    unittest.main()
