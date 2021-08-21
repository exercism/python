# Introduction

A [list][list] is a mutable collection of items in _sequence_.
Lists can hold reference to any (or multiple) data type(s) - including other lists or data structures such as [tuples][tuples], [sets][sets], or [dicts][dicts].
Content can be iterated over using `for item in <list>` construct.
If indexes are needed with the content, `for index, item in enumerate(<list>)` can be used.
Elements within a `list` can be accessed via `0-based index` number from the left, or `-1-based index` number from the right.
Lists can be copied in whole or in part using  _slice notation_ or `<list>.copy()`.
Python provides many useful and convenient [methods][list-methods] for working with lists.

[tuples]: https://github.com/exercism/python/tree/main/concepts/tuples
[dicts]: https://github.com/exercism/python/tree/main/concepts/dicts
[sets]: https://github.com/exercism/python/tree/main/concepts/sets
[list]: https://docs.python.org/3/library/stdtypes.html#list
[list-methods]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
