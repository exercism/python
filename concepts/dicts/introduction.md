# Introduction

A dictionary (`dict`) is a data structure that associates [hashable][term-hashable] _keys_ to _values_.
It is known in other programming languages as a resizable [hash table][hashtable-wikipedia], hashmap, or [associative array][associative-array].
Dictionaries are Python's only built-in [mapping type][mapping-types-dict].


`Keys` can include `numbers`, `str`, `tuples` (of _immutable_ values), or `frozensets`, but must be hashable and unique across the dictionary.
  `values` can be of any or multiple data type(s) or structures, including other dictionaries, built-in types, custom types, or even objects like functions.
As of Python 3.7, key order is guaranteed to be the order in which entries are inserted.


`dict`s enable the retrieval of a `value` in (on average) constant O(1) time, given the `key`.
Compared to searching for a value within a `list` or `array` (_without knowing the `index` position_), a dictionary uses significantly more memory, but has very rapid retrieval.
Dictionaries are especially useful in scenarios where the collection of items is large and must be accessed/updated frequently.

[associative-array]: https://en.wikipedia.org/wiki/Associative_array#:~:text=In%20computer%20science%2C%20an%20associative,a%20function%20with%20finite%20domain.
[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
