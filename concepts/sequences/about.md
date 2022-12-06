# Sequences

A sequence is an ordered, indexable collection of items.
All sequence types support a common set of operations that include `in`/`not in`, `min()`/`max()`, `<sequence>.index`, `<sequence>.count()` and `<sequence>.len()`.
`lists` support additional mutable operations such as [slice assignment][<url ref here>], `.append()`, `.extend()`, `.reverse()`, and `.copy()`.

All sequences can be indexed into using `<sequence>[<index number>]`, copied in whole or in part using `<sequence>[<start_index>:<stop_index>:<step>]`(\_a full copy can be made with `<sequence>[:]`), and iterated over using the `for item in <sequence>` construct.
`for index, item in enumerate(<sequence>)` can be used when both the element index and the element value are needed.

Pythons `list`, `tuple`, `str`, `byte`, and `range` types all belong to this wider sequence type.
In the case of `str`, the “collection” is made up of unicode code points.
In the case of `byte`, bytes.
Ranges are “collections” of numbers conforming to a `start:stop:step` rule.

## Common Sequence operations

### In operator

`in` checks if a sequence contains a value.
It returns `True` if the value is found, and `False` otherwise.

```python
>>> 1 in [1, 2, 3]
True

>>> 4 in [1, 2, 3]
False

>>> "a" in "abc"
True

>>> "d" in "abc"
False
```

It does not check if a value is in a sequence within a sequence.

```python
>>> "a" in ["abc", "def"]
False

>>> 1 in [[1, 2, 3], [4, 5, 6]]
False
```

### Not in operator

`Not in` checks if a sequence does not contain a value.
It does the reverse of `in`.

```python
>>> 1 not in [1, 2, 3]
False

>>> 4 not in [1, 2, 3]
True
```

### Get the length of a sequence

`len()` gives the length of a sequence.

```python
>>> len([1, 2, 3])
3

>>> len((1, 2, 3))
3

>>> len("abc")
3
```

### min() and max()

`min()` gives the minimum value in a sequence.

```python
>>> min([1, 2, 3])
1

>>> min("abc")
'a'
```

`max()` gives the maximum value in a sequence.

```python
>>> max([1, 2, 3])
3

>>> max("abc")
'c'
```

Using `max()/min()` on an empty sequence will raise a `ValueError`.

```python
>>> max([])

Traceback (most recent call last):
  File "c:\sequence.py", line 3, in <module>
    print(max([]))
          ^^^^^^^
ValueError: max() arg is an empty sequence
```

Using `min()/max()` on a sequence that includes a number and a `string` will raise a `TypeError`.

```python
>>> max([1, 2, 3, "a"])

Traceback (most recent call last):
  File "c:\sequence.py", line 3, in <module>
    print(max([1, 2, 3, "a"]))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'
```

```exercism/caution
Using `max()/max()` on an `string` is tricky since it compares via acsii values.
Therefore when dealing with characters outside of the english alphabet, the result may not be what you expect.
```

### Reverse a sequence

Using slicing with steps allows reversing a sequence.
That is because we can use a negative step to start at the end of the sequence and walk backwards.
This is a very common operation.

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[::-1]
[5, 4, 3, 2, 1]

>>> name = "Delizald"
>>> name[::-1]
'dlazileD'
```
