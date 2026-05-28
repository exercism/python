# Instructions append

~~~~exercism/note

The description above mentions [_mathematical sets_][math-sets], but also that a Pythagorean Triplet {a, b, c} _**must**_ be ordered such that a < b < c (_ascending order_). 

This makes Python's [`set` type][python-sets] unsuited to this exercise, since it is inherently _unordered_. 
You should return a [`list`][python-list] of `list`s instead (_e.g. `[[a, b, c]]`_). 
You can generate the triplets themselves in whichever order you would like, as the enclosing `list`'s order will be ignored in the tests. 

[math-sets]: https://en.wikipedia.org/wiki/Set_(mathematics)
[python-sets]: https://docs.python.org/3/tutorial/datastructures.html#sets
[python-list]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
~~~~
