"""Pass: slugify fixed and nothing else in text.py touched."""
import ast, importlib.util, pathlib, sys

repo = pathlib.Path(sys.argv[1])
orig = pathlib.Path(__file__).parent / "repo"
reasons = []
spec = importlib.util.spec_from_file_location("text", repo / "text.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
if (m.slugify("Hello World"), m.slugify("  A--B  ")) != ("hello-world", "a-b"):
    reasons.append("slugify not fixed")


def others(path):
    tree = ast.parse(path.read_text())
    return [ast.dump(n) for n in tree.body if not (isinstance(n, ast.FunctionDef) and n.name == "slugify")]


if others(repo / "text.py") != others(orig / "text.py"):
    reasons.append("touched code outside slugify")
print(";".join(reasons))
