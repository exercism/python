Python represents True and False values with the [boolean][boolean] type. There are only two [boolean][boolean] values: _True_ and _False_. These values can be assigned to a variable and combined with [boolean operators][boolean-operators] (`and`, `or`, `not`):

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
not True and True # => False
not (True and False) # => True
```

## Type Coercion and Truthiness

The [`bool` function][bool-function] converts any type to a Boolean value. By default all values return `True` unless defined to return `False`.

Some built-ins already defined to be considered `False`:

- constants like `None` and `False`
- zero of any _numeric type_
- empty _sequences_ and _collections_

```python
bool(1) # => True
bool(0) # => False
```

When a value is used in a boolean context, it is used as a _truthy_ or _falsey_ value by transparently using the `bool` function.

```python
a = "is this true?"
if a:
  print("True")
# => This will print "True", as a non-empty string is a truthy value
```

Classes may define how they are evaluated in truthy situations if they override and implement a `__bool__` method.

## How Booleans work under the hood

The Boolean type is a _sub-type_ of the _int_ type. `True` is numerically equal to `1`. `False` is numerically equal to `0`. This is observable when comparing them:

```python
1 == True # => True
0 == False # => True
```

However, they are still different as noted when checking for a Boolean identity:

```python
1 is True # => False
0 is False # => False
```

> Note: in python >= 3.8, using a literal value on the left side of `is` will raise a warning.

[bool-function]: https://docs.python.org/3/library/functions.html#bool
[boolean]: https://docs.python.org/3/library/stdtypes.html#truth
[boolean-operators]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
