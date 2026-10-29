import contextlib, io, unittest

import report


class TestReport(unittest.TestCase):
    def test_total(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            report.main(["sales.csv"])
        self.assertEqual(out.getvalue().strip(), "total 70")


if __name__ == "__main__":
    unittest.main()
