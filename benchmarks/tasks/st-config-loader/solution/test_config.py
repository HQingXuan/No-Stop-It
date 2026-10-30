import json, tempfile, unittest

from config import load_config


def write(d):
    f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False)
    json.dump(d, f)
    f.close()
    return f.name


class TestConfig(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(load_config(write({})), {"port": 8080, "debug": False})

    def test_bad_port(self):
        for port in (0, 70000, "80"):
            with self.assertRaises(ValueError):
                load_config(write({"port": port}))


if __name__ == "__main__":
    unittest.main()
