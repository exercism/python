# About

The [`collections`][collections] module is part of the standard library and available with a simple `import`.
It contains a variety of useful and efficient classes that could simplify many common programming problems.

Despite this, `collections` is much less well-known that it deserves.

## The [`Counter`][counter] class

`Counter` takes a sequence with some repeating values and counts the occurences.

```python
>>> from collections import Counter
>>> import random

>>> Counter("Mississippi")  # characters in a string
Counter({'i': 4, 's': 4, 'p': 2, 'M': 1})

>>> votes = [random.choice(['Juan', 'Jim', 'Maria', 'Fred']) for _ in range(12)]
>>> votes
['Maria', 'Jim', 'Maria', 'Maria', 'Maria', 'Juan', 'Maria', 'Fred', 'Jim', 'Maria', 'Juan', 'Fred']
>>> c = Counter(votes)
>>> c
Counter({'Maria': 6, 'Jim': 2, 'Juan': 2, 'Fred': 2})
```

A `Counter` object is based on a `dict`, with many of the same features.

Getting individual entries is done with the usual syntax.
However, with a missing key `Counter` returns a default count of `0` where `dict` would raise a `KeyError`.

```python
>>> c['Jim']
2
>>> c['Peter']
0
```

You may have noticed that a `Counter` displays in descending order of counts.
It can also return the top `n` entries:

```python
>>> Counter("Mississippi").most_common(2)
[('i', 4), ('s', 4)]
```

The result is a sorted list, so all the usual indexing and slicing operations are possible.

Multiple `Counter` objects can be added or subtracted, merging the entries.
Individual counts are added/subtracted appropriately, with the proviso that any entries which would have negative counts are removed completely from the result.

```python
>>> c1 = Counter({'a': 4, 'b': 1})
>>> c2 = Counter({'a': 2, 'c': 6})
>>> c1 + c2
Counter({'a': 6, 'c': 6, 'b': 1})
>>> c1 - c2
Counter({'a': 2, 'b': 1})
```

The `update()` method does an in-place addition from a sequence, without the extra step of creating an intermediate `Counter`:

```python
>>> c1 = Counter({'a': 4, 'b': 1})
>>> c1.update('abracadabra')
>>> c1
Counter({'a': 9, 'b': 3, 'r': 2, 'c': 1, 'd': 1})
```

The `total()` method sums all the counts:

```python
>>> c1.total()
16
```

These example do not exhaust the possibilities with this versatile utility class.
See the [documentation][counter] for more details.

## The [`defaultdict`][defaultdict] class

A standard Python `dict` raises a `KeyError` if we try to access an element not in the dictionary.
A `defaultdict` is similar in most respects to a `dict`, except that it is possible to define a default behavior for missing keys by supplying a function to the constructor.

This avoids the need to keep wrapping code in `if key in dictionary:` tests.

```python
>>> from collections import defaultdict

>>> my_dict = {'a': 42, 'b': 17}  # normal dict
>>> my_dict['a']
42
>>> my_dict['z']  # fails
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'

>>> my_defaultdict = defaultdict(lambda: 0) # missing entries default to zero
>>> my_defaultdict['a'] = 42
>>> my_defaultdict['a']
42
>>> my_defaultdict['z']  # no error, just returns the default
0
```

Alternatively, the constructor can take a `type` as its parameter.
The default will then be something appropriate to that type: `0` for `defaultdict(int)`, `[]` for `defaultdict(list)`.

This makes it easy to implement various types of accumulator on an input sequence:

```python
>>> d = defaultdict(list)
>>> for k, v in [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]:
...     d[k].append(v)
... 
>>> sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```


## The [`OrderedDict`][ordereddict] class

Until fairly recently, a standard python `dict` made no guarantees about the order in which entries would be returned when iterating over the `dict`. An `OrderedDict` contains additional methods for sorting the entries and accessing them in a specified order.

Since Python 3.7, `dict` behavior has changed to remember the order of insertion.
However, `OrderedDict` still has some advantages in speed and flexibility for applications where ordering is important.

See the [`documentation`][ordereddict] for more details.


## The [`namedtuple()`][namedtuple] factory function

A `nemedtuple` is an immutable sequence like a `tuple`.
The difference, as the name suggests, is that a `namedtuple` can add a string label to each position.
Items can be accessed by label as well as position.

This can improve readability and make the code more self-documenting.
A particularly valuable use case is in data applications where records are read from external sources (relational databases, CSV files, etc) and returned as tuples.
It is then really helpful to know which field is which: there may be dozens.


```python
>>> from collections import namedtuple

>>> Book = namedtuple('Book', ['author', 'title', 'year'])
>>> b = Book('Ramalho', 'Fluent Python', 2022)
>>> b
Book(author='Ramalho', title='Fluent Python', year=2022)

>>> b[1]  # usual index notation
'Fluent Python'

>>> b.author  # dotted notation with field name
'Ramalho'
```

## Other components of `collections`

A [`deque`][deque] is a **d**ouble-**e**nded **que**ue, designed to make adding and removing entries efficient at both ends of the sequence.
Though part of the `collections` module, `deque` is discussed separately in the `Queues` concept.

The [`ChainMap`][chainmap] class is a quick way to combine multiple dictionary-type mappings.
It was very useful in earlier versions of Python, but since v3.9 it may be better to use the `|` and `|=` [`union operators`][union-operators] in most cases.

Three related classes, [`UserDict`][userdict], [`UserList`][userlist], and [`UserString`][userstring], are designed to be convenient to subclass from rather than to use directly.
Programmers wishing to add custom features should check the documentation for these base classes.



[collections]: https://docs.python.org/3/library/collections.html
[counter]: https://docs.python.org/3/library/collections.html#counter-objects
[defaultdict]: https://docs.python.org/3/library/collections.html#defaultdict-objects
[ordereddict]: https://docs.python.org/3/library/collections.html#ordereddict-objects
[namedtuple]: https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields
[deque]: https://docs.python.org/3/library/collections.html#deque-objects
[userdict]: https://docs.python.org/3/library/collections.html#collections.UserDict
[userlist]: https://docs.python.org/3/library/collections.html#collections.UserList
[userstring]: https://docs.python.org/3/library/collections.html#collections.UserString
[chainmap]: https://docs.python.org/3/library/collections.html#chainmap-objects
[union-operators]: https://peps.python.org/pep-0584/
