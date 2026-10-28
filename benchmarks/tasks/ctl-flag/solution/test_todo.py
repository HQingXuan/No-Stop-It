import contextlib, io, json, unittest

import todo


def run(*args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        todo.main(list(args))
    return out.getvalue()


class TestList(unittest.TestCase):
    def test_list(self):
        self.assertEqual(run("list").splitlines(), ["[x] buy milk", "[ ] write report", "[x] call bob"])

    def test_done(self):
        self.assertEqual(run("list", "--done").splitlines(), ["[x] buy milk", "[x] call bob"])

    def test_json(self):
        self.assertEqual(len(json.loads(run("list", "--json"))), 3)
        self.assertEqual([t["title"] for t in json.loads(run("list", "--done", "--json"))], ["buy milk", "call bob"])


if __name__ == "__main__":
    unittest.main()
