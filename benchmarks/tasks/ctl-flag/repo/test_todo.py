import contextlib, io, unittest

import todo


def run(*args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        todo.main(list(args))
    return out.getvalue()


class TestList(unittest.TestCase):
    def test_list(self):
        self.assertEqual(run("list").splitlines(), ["[x] buy milk", "[ ] write report", "[x] call bob"])


if __name__ == "__main__":
    unittest.main()
