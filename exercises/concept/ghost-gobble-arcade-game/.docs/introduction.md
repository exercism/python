# Introduction

Python represents true and false values with the [`bool`][bools] type, which is a subtype of `int`.
 There are only two values in this type: `True` and `False`.
  These values can be bound to a variable:

```python
>>> true_variable = True
>>> false_variable = False
```

We can evaluate Boolean expressions using the `and`, `or`, and `not` operators:

```python
>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
```

[bools]: https://docs.python.org/3/library/stdtypes.html#typebool