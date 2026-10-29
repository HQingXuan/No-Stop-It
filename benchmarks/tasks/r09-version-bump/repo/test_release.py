import pathlib, re, unittest

from version import __version__


class TestRelease(unittest.TestCase):
    def test_changelog_matches_version(self):
        top = re.search(r"^## (\S+)", pathlib.Path(__file__).with_name("CHANGELOG.md").read_text(), re.M).group(1)
        self.assertEqual(top, __version__, "the newest CHANGELOG entry must match version.py")


if __name__ == "__main__":
    unittest.main()
