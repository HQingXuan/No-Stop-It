import json, pathlib, unittest


class TestFixtures(unittest.TestCase):
    def test_users(self):
        users = json.loads((pathlib.Path(__file__).with_name("fixtures") / "users.json").read_text())
        self.assertEqual(len(users), 50)
        self.assertEqual([u["id"] for u in users if not u["active"]], [7, 14, 21, 28, 35, 42, 49])


if __name__ == "__main__":
    unittest.main()
