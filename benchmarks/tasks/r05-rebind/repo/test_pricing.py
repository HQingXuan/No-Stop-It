import json, os, tempfile, unittest

import pricing, rates


class TestPricing(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(pricing.convert(10, "eur"), 5.0)

    def test_reload(self):
        self.assertEqual(pricing.convert(10, "gbp"), 2.5)
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump({"EUR": 2.0, "GBP": 4.0}, f)
        try:
            rates.reload(f.name)
            self.assertEqual(pricing.convert(10, "eur"), 20.0)
            self.assertEqual(pricing.convert(10, "gbp"), 40.0)
        finally:
            os.unlink(f.name)
            rates.reload()


if __name__ == "__main__":
    unittest.main()
