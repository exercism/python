Python represents True and False values with the [bool][bool] type. There are only two boolean values: `True` and `False`. These values can be assigned to a variable and combined with the [boolean operators][boolean-operators] (`and`, `or`, `not`):

```python
true_variable = True and True
false_variable = True and False

true_variable = False or True
false_variable = False or False

true_variable = not False
false_variable = not True
```

[Boolean operators][boolean-operators] use _short-circuit evaluation_, which means that expression on the right-hand side of the operator is only evaluated if needed.

Each of the operators has a different precedence, where `not` is evaluated before `and` and `or`. Brackets can be used to evaluate one part of the expression before the others:

```python
>>>not True and True
False

>>>not (True and False)
True
```

All `boolean operators` are considered lower precedence than Pythons [`comparison operators`][comparisons], such as `==`, `>`, `<`, `is` and `is not`.

## Type Coercion and Truthiness

The bool function ([`bool()`][bool-function]) converts any object to a Boolean value. By default all objects return `True` unless defined to return `False`.

A few `built-ins` are always considered `False` by definition:

- the constants `None` and `False`
- zero of any _numeric type_ (`int`, `float`, `complex`, `decimal`, or `fraction`)
- empty _sequences_ and _collections_ (`str`, `list`, `set`, `tuple`, `dict`, `range(0)`)

```python
>>>bool(None)
False

>>>bool(1)
True
>>>bool(0)
False

>>>bool([1,2,3])
True
>>>bool([])
False

>>>bool({"Pig" : 1, "Cow": 3})
True
>>>bool({})
False
```

When a object is used in a _boolean context_, it is evaluated transparently as _truthy_ or _falsey_ using `bool()`:

```python
a = "is this true?"
b = []

# This will print "True", as a non-empty string is considered a "truthy" value
if a:
  print("True")

# This will print "False", as an empty list is considered a "falsey" value
if not b:
   print("False")
```

Classes may define how they are evaluated in truthy situations if they override and implement a `__bool__()` method, and/or a `__len__()` method.

## How Booleans work under the hood

The `bool` type is implemented as a _sub-type_ of _int_. That means that `True` is _numerically equal_ to `1` and `False` is _numerically equal_ to `0`. This is observable when comparing them using an _equality operator_:

```python
>>>1 == True
True

>>>0 == False
True
```

However, `bools` are **still different** from `ints`, as noted when compairing using the _identity operator_:

```python
>>>1 is True
False

>>>0 is False
False
```

> Note: in python >= 3.8, using a literal (such as 1, '', [], or {}) on the left side of `is` will raise a warning.

It is considered a [Python anti-pattern][comparing to true in the wrong way] to use the equality operator to comaire a booleand variable to `True` or `False`. Instead, the identity operator `is` should be used:

```python

flag = True

# Not "Pythonic"
if flag == True:
    print("This works, but it's not considered Pythonic.")

# A better way
if flag:
    print("Pythonistas prefer this pattern as more Pythonic.")
```

[bool-function]: https://docs.python.org/3/library/functions.html#bool
[bool]: https://docs.python.org/3/library/stdtypes.html#truth
[boolean-operators]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
[comparing to true in the wrong way]: https://docs.quantifiedcode.com/python-anti-patterns/readability/comparison_to_true.html
