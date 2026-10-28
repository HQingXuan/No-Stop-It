import unittest

import text


class TestText(unittest.TestCase):
    def test_parse_kv(self):
        self.assertEqual(text.ParseKV("a=1; b = 2;"), {"a": "1", "b": "2"})
