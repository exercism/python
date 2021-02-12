# Design

## Goal

The goal of this exercise is to teach the student how Enums ([Enumerations](https://en.wikipedia.org/wiki/Enumerated_type)) are implemented & used in Python. We will teach this through Pythons Enum class/type.

## Learning objectives

- What is an enumeration / enum is, and why they are needed/wanted in Python?
- Understand the nomenclature (naming) used in reference to enums (e.g. enumeration/enum, enum members, enum member names, and enum member values)
- Understand that enumeration members are functionally constants (and therefore should be formatted as such)
- How Enums are different from other, more generic Python classes.
- How to create various Enums
  - By using the class syntax by importing & subclassing Enum.
  - By using the Enum Functional API
  - By defining enum members with values that include non-int types (like str, tuple, float etc.)
  - Using the auto() function to automatically assign integer values to members when exact value types are unimportant/not needed.
  - Creating member aliases by assigning the same value to different names (two different names can have the same value; the second name defined becomes an alias of the first)
  - Using the class decorator @enum.unique to prevent member aliases and enforce that member values be unique.
- How to use an enumeration and enumeration members in other functions/code
  - Enum members are iterable in member definition order, but iteration will not include aliases.
  - An ordered mapping of names to members can be retrieved via **members**.items()
  - enumeration members are compared by identity, using the is/is not keywords
  - Ordered comparison (<, >, <=, '>=) between enumeration values is not supported, and will throw aTypeError`.
  - Equality/inequality comparison is defined, and == and != can be used.
  - Comparisons between enumeration values and non-enumeration values will always return False

## Out of scope

- Flag enum subtype (perhaps better as an advanced exercise that includes bitwise operations)
- IntEnum and IntFlag subtypes (since they break the semantic promises of an enum by being comparable to int)
- mixins & multiple inheritance for the creation of Enums
- using **new**() to customize the value of an enum member (better for an advanced/extended enum exercise)
- omitting values
- subclassing an "empty" pre-defined enum
- customization of auto()
- Pickling

## Concepts

- enumeration, enums

## Prerequisites

- `decorators, @`
- `__init__()`
- `classes, OOP`
- `inheritance`
- `iteration`
- `iterables`
- `dunder methods`
- `comparisons`
- `rich comparisons`
- `class attributes`
- `importing`
- `aliasing`
- `dicts, dict methods (specifically dict.items())`
- `mapping types`
- `immutable, immutability`
- `class properties`

## Resources

- [Exercism v3 C# Enums concept exercise](https://github.com/exercism/v3/tree/master/languages/csharp/exercises/concept/enums)
- [Python Docs: Enum](https://docs.python.org/3/library/enum.html)
- [Enum - Mouse vs. Python](https://www.blog.pythonlibrary.org/2018/03/20/python-3-an-intro-to-enumerations/)
- [Why you should use more enums in Python - Florian Dahlitz](https://florian-dahlitz.de/blog/why-you-should-use-more-enums-in-python)
- [Python Docs: How are Enums Different?](https://docs.python.org/3/library/enum.html#how-are-enums-different)
- [Python Docs: The Enum Functional API](https://docs.python.org/3/library/enum.html#functional-api)
- [Stack Overflow: Python enum, when and where to use?](https://stackoverflow.com/questions/22586895/python-enum-when-and-where-to-use)
- [PEP435: Adding an Enum Type to the Python Standard Library](https://www.python.org/dev/peps/pep-0435/)
- [Using Enums and Django model Choices - Ben Cleary](https://medium.com/@bencleary/using-enums-as-django-model-choices-96c4cbb78b2e)
