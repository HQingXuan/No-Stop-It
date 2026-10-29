import contextlib, io, unittest

import report


def run(*args):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        report.main(list(args))
    return out.getvalue().strip()


class TestReport(unittest.TestCase):
    def test_total(self):
        self.assertEqual(run("sales.csv"), "total 70")

    def test_since(self):
        self.assertEqual(run("sales.csv", "--since", "2026-02-10"), "total 60")


if __name__ == "__main__":
    unittest.main()
