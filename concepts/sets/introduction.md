# Sets

A [`set`][type-set] is a mutable and _unordered_ collection of _hashable_ objects.
Items within a `set` are unique, and no duplicates are allowed.
Like most collections, `sets` can hold any (or multiple) data type(s) -- as long as those types can be [hashed][hashable].
Sets also come in an _immutable_ [`frozenset`][type-frozenset] flavor.

Like other collection types, `sets` support membership testing through `in`, length calculation through `len()`, shallow copies through `copy()`, & iteration via `for item in <set>`.
_Unlike_ sequence types (_`string`, `list` & `tuple`_), `sets` are **neither ordered nor indexed**, and _do not support_ slicing, sorting, or other sequence-type behaviors.

`sets` are most commonly used to quickly dedupe groups of items.

[type-set]: https://docs.python.org/3/library/stdtypes.html#set
[hashable]: https://docs.python.org/3/glossary.html#term-hashable
[type-frozenset]: https://docs.python.org/3/library/stdtypes.html#frozenset
