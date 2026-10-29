import json, pathlib, unittest


class TestRates(unittest.TestCase):
    def test_shape(self):
        rates = json.loads(pathlib.Path(__file__).with_name("rates.json").read_text())
        self.assertIn("EUR", rates)


if __name__ == "__main__":
    unittest.main()
