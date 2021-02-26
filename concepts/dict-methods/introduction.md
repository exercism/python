# Dictionary Methods in Python

A dictionary (`dict`) in Python is a data structure that associates [hashable][term-hashable] _keys_ to _values_ and is known in other programming languages as a [hash table or hashmap][hashtable-wikipedia].
In Python, it's considered a [mapping type][mapping-types-dict].
`dicts` enable the retrieval of a value in constant time (on average), given the key.

Compared to searching for a value within a list or array (_without knowing the index position_), a dictionary uses significantly more memory, but has very rapid retrieval.
It's especially useful in scenarios where the collection of items is large and must be accessed/updated frequently.

The `dict` class in Python provides many useful [methods][dict-methods] for working with dictionaries.
Some are introduced in the concept exercise for `dicts`.
This concept tackles a few more - along with some techniques for iterating through and manipulating `dicts`.

[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
[dict-methods]: https://docs.python.org/3/library/stdtypes.html#dict
