# Sets

A [`set`][type-set] is a _mutable_ and _unordered_ collection of [_hashable_][hashable] objects.
Set members must be distinct — duplicate items are not allowed.
They can hold multiple different data types and even nested structures like a `tuple` of `tuples` — as long as all elements can be _hashed_.
Sets also come in an immutable [`frozensets`][type-frozenset] flavor.

Sets are most commonly used to quickly remove duplicates from other data structures or item groupings.
They are also used for efficient comparisons when sequencing and duplicate tracking are not needed.

Like other collection types (_dictionaries, lists, tuples_), `sets` support:
- Iteration via `for item in <set>`
- Membership checking via `in` and `not in`,
- Length calculation through `len()`, and
- Shallow copies through `copy()`

`sets` do not support:
- Indexing of any kind
- Ordering via sorting or insertion
- Slicing
- Concatenation via `+`


Checking membership in a `set` has constant time complexity (on average) versus checking membership in a `list` or `string`, where the time complexity grows as the length of the data increases.
Methods such as `<set>.union()`, `<set>.intersection()`, or `<set>.difference()` also have constant time complexity (on average).

[type-set]: https://docs.python.org/3/library/stdtypes.html#set
[hashable]: https://docs.python.org/3.7/glossary.html#term-hashable
[type-frozenset]: https://docs.python.org/3/library/stdtypes.html#frozenset
