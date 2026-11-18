# Sequences

A sequence is an ordered, indexable collection of items.
All sequence types support a common set of operations that include `in`/`not in`,  `min()`/`max()`, `<sequence>.index`, `<sequence>.count()` and `<sequence>.len()`.
`lists` support additional mutable operations such as [slice assignment][<url ref here>], `.append()`, `.extend()`, `.reverse()`, and `.copy()`.

All sequences can be indexed into using `<sequence>[<index number>]`, copied in whole or in part using `<sequence>[<start_index>:<stop_index>:<step>]`(_a full copy can be made with `<sequence>[:]`), and iterated over using the `for item in <sequence>` construct.
 `for index, item in enumerate(<sequence>)` can be used when both the element index and the element value are needed.


Pythons `list`, `tuple`, `str`, `byte`, and `range` types all belong to this wider sequence type.
In the case of `str`, the “collection” is made up of unicode code points.
In the case of  `byte`, bytes.
Ranges are “collections” of numbers conforming to a `start:stop:step` rule.


