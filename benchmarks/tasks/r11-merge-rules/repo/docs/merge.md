# Config merge

`merge(base, override)` returns a new dict and changes neither input.

1. Keys only in one side are kept as they are.
2. When both sides have a dict, merge them with these same rules, at any depth.
3. When both sides have a list, the result is base's items followed by override's items that base does not already have.
4. A key whose override value is `None` is removed from the result.
5. A key in override written as `"!name"` replaces base's `name` outright, with no merging; the result key is `name`.
6. Anything else: override wins.
