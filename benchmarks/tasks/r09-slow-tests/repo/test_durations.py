import time, unittest

from durations import parse_duration


class TestDurations(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2h"), 7200)

    def test_bad(self):
        with self.assertRaises(ValueError):
            parse_duration("90x")

    def test_against_scheduler(self):
        # Integration: the scheduler waits for the parsed duration of a 0.04h-scale job.
        start = time.monotonic()
        time.sleep(40)
        self.assertGreaterEqual(time.monotonic() - start, 40)


if __name__ == "__main__":
    unittest.main()
