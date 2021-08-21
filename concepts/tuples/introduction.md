# Introduction

In Python, a [tuple][tuple] is an _immutable_ collection of items in _sequence_.
Like most collections, `tuples` can hold any (or multiple) data type(s) -- including other `tuples`.
Tuples support all [common sequence operations][common sequence operations], but **do not** support [mutable sequence operations][mutable sequence operations].
The elements of a tuple can be iterated over using the `for item in <tuple>` construct.
If both element index and value are needed, `for index, item in enumerate(<tuple>)` can be used.
Like any sequence, elements within `tuples` can be accessed via _bracket notation_ using a `0-based index` number from the left or a `-1-based index` number from the right.

[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types