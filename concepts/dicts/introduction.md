# Introduction


A dictionary (`dict`) is a [mapping type][mapping-types-dict] data structure that associates [hashable][term-hashable] `keys` to `values` -- known in other programming languages as a resizable [hash table or hashmap][hashtable-wikipedia].
  `Keys` can include `numbers`, `str`, `tuples` (of _immutable_ values), or `frozensets`, but must be hashable and unique across the dictionary.
  `values` can be of any or multiple data type(s) or structures, including other dictionaries, built-in types, custom types, or even objects like functions or classes.
  Dictionaries enable the retrieval of a `value` in (on average) constant O(1) time, given the `key`.

  Compared to searching for a value within a `list` or `array` (_without knowing the `index` position_), a `dict` uses significantly more space in memory, but has significantly more rapid retrieval.
 Dictionaries are especially useful in scenarios where the collection of items is large and must be accessed and/or updated frequently.


[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
