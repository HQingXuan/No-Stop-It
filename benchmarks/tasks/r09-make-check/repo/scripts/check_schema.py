"""schema.json, the User dataclass and every example must agree."""
import dataclasses, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parents[1]))
from user import User

root = pathlib.Path(__file__).parents[1]
schema = json.loads((root / "schema.json").read_text())
types = {"integer": int, "string": str}
fields = [f.name for f in dataclasses.fields(User)]
errors = []
if sorted(schema["required"]) != sorted(fields):
    errors.append(f"schema.json required {schema['required']} != User fields {fields}")
for ex in sorted((root / "examples").glob("*.json")):
    doc = json.loads(ex.read_text())
    for key in schema["required"]:
        if key not in doc:
            errors.append(f"{ex.name}: missing {key}")
        elif not isinstance(doc[key], types[schema["properties"][key]["type"]]):
            errors.append(f"{ex.name}: {key} has the wrong type")
print("\n".join(errors) or "schema ok")
sys.exit(bool(errors))
