In Python, [an enum][enum-docs] is a set of unique names that are bound unique, **constant** values. Enums are defined by inheriting an `Enum` class. Built-in enum types are available in the module `enum` and the class `Enum` can be imported using `from enum import Enum`.

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

Enums can also be created via the following [functional API][enum-functional-api].

```python
Animal = Enum('Animal', 'ANT BEE CAT DOG')
list(Animal)
#=> [<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]

Animal.ANT.value
#=> 1
```

When assigning the same value to two members in an enum, the latter assigned member will be an alias to the formed one. It is not allowed to use the same name for two members of an enum.

```python
class Color(Enum):
    RED = 1
    GREEN = 2
    ALIAS_OF_RED = 1

Color.ALIAS_OF_RED
#=> <Color.RED: 1>
```

Iterating through the members of the enum can be done with the standard `for member in` syntax:

```python
for member in Color:
    print((member.name, member.value))
#=> (RED, 1)
#=> (GREEN, 2)

# __members__.items() helps you to loop through alias as well
for member in Color.__members__.items():
    print(member)
#=>('RED', <Color.RED: 1>)
#=>('GREEN', <Color.GREEN: 2>)
#=>('ALIAS_OF_RED', <Color.RED: 1>)
```

Enum members can be compared using [`is` (_identity operator_)][identity-keyword] or `is not`. The `==` or `!=` (_equality operators_) work likewise.

```python
a = Color.RED

a is Color.RED
#=> True

a == Color.RED
#=> True
```

To assign integer values, the [`auto()` function][enum-auto-docs] starts with `1` and automatically sets subsequent values.

```python
class Shape(Enum):
    CIRCLE = auto()
    SQUARE = auto()
    OVAL = auto()
```

To disallow aliasing (_preventing duplicate values with different names_), the `@unique` decorator may be used.

```python
@unique
class Shape(Enum):
    CIRCLE = 1
    SQUARE = 2
    TRIANGLE = 1
#=> ValueError: duplicate values found in <enum 'Shape'>: TRIANGLE -> CIRCLE
```

To access an enum member for a given value, this notation can be used: `EnumName(value)`.

```python
g = Color(2)

g is Color.GREEN
#=> True

g
#=> <Color.GREEN: 2>
```

A custom [restricted `Enum`][restricted-enums] can be written by subclassing `Enum` with any mix-in or data-type. For example:

```python
class StrEnum(str, Enum):
    pass
```

[enum-docs]: https://docs.python.org/3/library/enum.html
[enum-auto-docs]: https://docs.python.org/3/library/enum.html#using-auto
[enum-functional-api]: https://docs.python.org/3/library/enum.html#functional-api
[restricted-enums]: https://docs.python.org/3/library/enum.html#restricted-enum-subclassing
[identity-keyword]: https://www.w3schools.com/python/ref_keyword_is.asp
