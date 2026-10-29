# kv.py

A key-value store in `store.json` next to kv.py (or the path in `$KV_STORE`).

| Command | Does |
|---|---|
| `set KEY VALUE` | Stores VALUE. The previous value, if any, goes to the key's history. |
| `get KEY` | Prints the value. Missing key: prints `error: no such key` to stderr and exits 1. |
| `del KEY` | Removes the key and its history. Missing key: same error as get. |
| `list [--prefix P]` | Prints the keys, sorted, one per line; only keys starting with P if given. |
| `export --format csv\|json` | csv: a `key,value` header then one row per key, sorted. json: one object of all keys. |
| `history KEY` | Prints every value KEY has had, oldest first, the current one last. |
