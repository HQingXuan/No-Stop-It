import json, pathlib

users = [{"id": i, "name": f"user{i}", "email": f"user{i}@example.com", "active": i % 7 != 0} for i in range(1, 51)]
out = pathlib.Path(__file__).with_name("fixtures") / "users.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(users, indent=1))
