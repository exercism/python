# Dictionary Methods in Python

A dictionary (`dict`) in Python is a data structure that associates [hashable][term-hashable] _keys_ to _values_ and is known in other programming languages as a resizable [hash table][hashtable-wikipedia], hashmap, or [associative array][associative-array].
Dictionaries are Python's only built-in [mapping type][mapping-types-dict].
As of Python 3.7, `dict` key order is guaranteed to be the order in which entries are inserted.

Given a `key`, dictionaries can retrieve a `value` in (on average) constant time (_independent of the number of entries_).
Compared to searching for a value within a `list` or `array` (_without knowing the `index` position_), a `dict` uses significantly more memory, but has very rapid retrieval.
Dictionaries are especially useful in scenarios where the collection of items is large and must be accessed and updated frequently.
The `dict` class in Python provides many useful [methods][dict-methods], some of which are introduced in the concept exercise for dictionaries.

This concept tackles a few more:

- `dict.setdefault()` for automatically adding keys when needed.
- `dict.fromkeys(iterable, <default value>)` for creating a new `dict` from any number of iterables.
- `.keys()`, `.values()`, and `.items()` for convenient iterators.
- `sorted(<dict>.items())`. for re-ordering entries in a `dict`.
- `dict_one.update(<dict_two>)` for updating one `dict` with overlapping values from another `dict`.
- `dict | other_dict` and `dict |= other_dict` for merging or updating two `dict`s via operators.
- `reversed(dict.keys())`, `reversed(dict.values())`, or `reversed(dict.items())` for reversed views.
- `<dict>.popitem()` for removing and returning a `key`, `value` pair.

[associative-array]: https://en.wikipedia.org/wiki/Associative_array#:~:text=In%20computer%20science%2C%20an%20associative,a%20function%20with%20finite%20domain.
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
[dict-methods]: https://docs.python.org/3/library/stdtypes.html#dict
