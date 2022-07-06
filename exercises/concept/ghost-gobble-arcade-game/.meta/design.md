# Design

## Goal

The goal of this exercise is to teach the student how [`bool`][bools] is implemented and used in Python. We will teach the `bool` type by showing the student how to use it.

## Learning objectives

- create a `bool` object via literal declaration
- obtain a `bool` object from using [logical operators][logical operators] (`and`, `or`, `not`)

## Out of scope

- obtain a `bool` object from [comparison operators][comparison operators] (`>`, `<`, `==`)
- obtain a `bool` object from [membership operators][membership operators] (`in`, `not in`)
- obtain a `bool` object from [identity operators][identity operators] (`is`, `is not`)
- 'truthyness' and 'falsyness'
  - create a `bool` object from other objects (`collections`, `integers`, `strings`) with the `bool()` constructor.
- catching/raising Exceptions
- covering that `bool` is a subtype of `int`
- bitwise logical operators
- orders of evaluation

## Concepts

- **booleans:** know of the existence of the bool type and its two values; know about boolean operators and how to build logical expressions with them; know of the boolean operator precedence rules.

## Prerequisites

- `basics`
- `comparison-operators`

## Resources

- [Boolean Operations — and, or, not][Boolean Operations — and, or, not]
- [Built-in Functions - bool][Built-in Functions - bool]
- [Truth Value Testing][Truth Value Testing]
- [Comparisons][Comparisons]


[Boolean Operations — and, or, not]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[Built-in Functions - bool]: https://docs.python.org/3/library/functions.html#bool
[Comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
[Truth Value Testing]: https://docs.python.org/3/library/stdtypes.html#truth
[bools]: https://github.com/exercism/v3/blob/master/languages/python/reference/concepts/builtin_types/bool.md
[comparison operators]: https://docs.python.org/3/reference/expressions.html#value-comparisons
[identity operators]: https://docs.python.org/3/reference/expressions.html#is-not
[logical operators]: https://docs.python.org/3/reference/expressions.html#boolean-operations
[membership operators]: https://docs.python.org/3/reference/expressions.html#membership-test-operations
