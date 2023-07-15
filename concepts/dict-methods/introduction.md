# Dictionary Methods in Python

The `dict` class in Python provides many useful [methods][dict-methods], some of which are introduced in the concept exercise for dictionaries.

This concept tackles a few more:

- `dict.setdefault()` automatically adds keys without throwing a `KeyError`.
- `dict.fromkeys(iterable, <default value>)` creates a new `dict` from any number of iterables.
- `.keys()`, `.values()`, and `.items()` provide convenient iterators.
- `sorted(<dict>.items())`. can easily re-order entries in a `dict`.
- `dict_one.update(<dict_two>)` updates one `dict` with overlapping values from another `dict`.
- `dict | other_dict` and `dict |= other_dict` merges or updates two `dict`s via operators.
- `reversed(dict.keys())`, `reversed(dict.values())`, or `reversed(dict.items())` produce _reversed_ views.
- `<dict>.popitem()` removes and returns a `key`, `value` pair.

[dict-methods]: https://docs.python.org/3/library/stdtypes.html#dict
