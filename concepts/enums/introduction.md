# Introduction

In Python, [an enum](https://docs.python.org/3/library/enum.html) is a set of names that are bound to unique `literal`, or `constant` values. Enums are defined by inheriting an `Enum` class. Built-in enum types are available in the module `enum` and the class `Enum` can be imported using `from enum import Enum`.

```python
class Color(Enum):
    RED = 1
    GREEN = 2
```

Note that the values of the enum members can be any data types such as str, tuple, float, etc.

```python
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
```

When assigning the same value to two members in an enum, the latter assigned member will be an alias to the formed one. It is not allowed to use the same name for two members of an enum.

```python
class Color(Enum):
    RED = 1
    GREEN = 2
    ALIAS_OF_RED = 1

Color.ALIAS_OF_RED
#=> <Color.RED: 1>

Color.ALIAS_OF_RED.value
#=> 1
```

Iterating through the members of the enum can be done with the standard `for member in` syntax:

```python
for member in Color:
    print((member.name, member.value))
#=> (RED, 1)
#=> (GREEN, 2)
```

Enum members can be compared using [`is` (_identity operator_)](https://www.w3schools.com/python/ref_keyword_is.asp) or `is not`. The `==` or `!=` (_equality_operators_) work likewise.

```python
a = Color.RED

a is Color.RED
#=> True

a == Color.RED
#=> True
```

To access an enum member for a given value, `EnumName(value)` can be used:

```python
g = Color(2)

g is Color.GREEN
#=> True

g
#=> <Color.GREEN: 2>
```
