## Sequence operations

### In operator

`In` checks if a sequence contains a value.
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

## Get the length of a sequence

## Reverse a sequence

Using slicing with steps allows reversing a sequence.
That is because we can use a negative step to start at the end of the sequence and move backwards.
This is a very common operation.

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[::-1]
[5, 4, 3, 2, 1]

>>> name = "Delizald"
>>> name[::-1]
'dlazileD'
```
