import unittest

import invoice, price


class TestBilling(unittest.TestCase):
    def test_gross(self):
        self.assertEqual(price.gross(100), 108.0)

    def test_label(self):
        self.assertEqual(invoice.tax_label(), "VAT 8%")

    def test_line(self):
        self.assertEqual(invoice.line("pen", 10), "pen: 10.80 EUR (VAT 8%)")


if __name__ == "__main__":
    unittest.main()
