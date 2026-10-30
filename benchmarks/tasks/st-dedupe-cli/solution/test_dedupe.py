import subprocess, sys, tempfile, unittest


def run(*args, files):
    paths = []
    for text in files:
        f = tempfile.NamedTemporaryFile("w", delete=False)
        f.write(text)
        f.close()
        paths.append(f.name)
    return subprocess.run([sys.executable, "dedupe.py", *args, *paths], capture_output=True, text=True).stdout.splitlines()


class TestDedupe(unittest.TestCase):
    def test_across_files(self):
        self.assertEqual(run(files=["a\nb\na\n", "b\nc\n"]), ["a", "b", "c"])

    def test_ignore_case(self):
        self.assertEqual(run("--ignore-case", files=["A\na\nB\n"]), ["A", "B"])


if __name__ == "__main__":
    unittest.main()
