import os, time, unittest

import events

# CI runs in Los Angeles; report days are UTC days.
os.environ["TZ"] = "America/Los_Angeles"
time.tzset()


class TestEvents(unittest.TestCase):
    def test_day(self):
        self.assertEqual(events.day_of(1772841600), "2026-03-07")  # 2026-03-07T00:00:00Z

    def test_per_day(self):
        self.assertEqual(events.per_day([1772841600, 1772845200, 1772924400]), {"2026-03-07": 3})


if __name__ == "__main__":
    unittest.main()
