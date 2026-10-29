import unittest

import pricing


class TestPricing(unittest.TestCase):
    def test_threshold(self):
        self.assertEqual(pricing.discount(100), 90)

    def test_small_order(self):
        self.assertEqual(pricing.discount(50), 50)

    def test_to_eur(self):
        self.assertGreater(pricing.to_eur(10), 0)
