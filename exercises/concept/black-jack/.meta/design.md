## Goal

This concept exercise should teach how basic _non-customized_ comparisons work in python and how to use them effectively.

## Learning objectives

- understand all comparison operations in Python have the same priority and are evaluated after arithmetic, shifting, or bitwise operations.
- understand all comparisons yield the boolean values True and False
- know that identity comparisons is and is not are for checking an objects identity only
- understand that `==` and `!=` compare both the value & type of an object.
- know where Python has altered the behavior of `==` and `!=` for certain `built-in` types (such as [numbers][numbers], or for standard library types like [decimals][decimals], and [fractions][fractions] to allow comparison across and within type.
- know that unlike numeric types, strings (`str`) and binary sequences (`bytes` & `byte array`) **cannot** be directly compared.
- understand how comparisons work within `built-in` [sequence types][sequence types](`list`, `tuple`, `range`) and `built-in` `collection types` (`set`, `[dict]`)
- know about the "special" comparisons `None`, `NotImplemented` (comparing either should use identity operators and not equality operators because they are singleton objects) and NaN (`NaN` is **never** `==` to itself)
- use the value comparison operators `==`, `>`, `<`, `!=` with numeric types
- use the value comparison operators `==`, `>`, `<`, `!=` with non-numeric types
- use `is` and `is not` to check/verify identity

## Out of scope

- rich comparison with `__lt__`, `__le__`, `__ne__`, `__ge__`, `__gt__`
- understanding (_and using the concept_) that the `==` operator calls the dunder method `__eq__()` on a specific object, and uses that object's implementation for comparison. Where no implementation is present, the default `__eq__()` from generic `object` is used.
- overloading the default implementation of the `__eq__()` dunder method on a specific object to customize comparison behavior.
- `set operations`
- performance considerations

## Concepts

- Comparison priority in Python
- Comparison operators `==`, `>`, `<`, `!=`
- Identity methods `is` and `is not`
- Equality applied to `built-in` types
- Equivalence vs equality
- Inequality

## Prerequisites

- `basics`
- `booleans`
- `dicts`
- `lists`
- `sets`
- `strings`
- `tuples`
- `numbers`
- `iteration`

## Resources

- [Comparisons in Python (Python language reference)](https://docs.python.org/3/reference/expressions.html#comparisons)
- [Value comparisons in Python (Python language reference)](https://docs.python.org/3/reference/expressions.html#value-comparisons)
- [Identity comparisons in Python (Python language reference)](https://docs.python.org/3/reference/expressions.html#is-not)
- [Python operators official doc](https://docs.python.org/3/library/operator.html)
- [Python Object Model (Python docs)](https://docs.python.org/3/reference/datamodel.html#objects)
- [Basic Customization](https://docs.python.org/3/reference/datamodel.html#customization)
- [Python basic operators on tutorialspoint](https://www.tutorialspoint.com/python/python_basic_operators.htm)
- [Python comparison operators on data-flair](https://data-flair.training/blogs/python-comparison-operators/)
- [PEP 207 to allow Operator Overloading for Comparison](https://www.python.org/dev/peps/pep-0207/)

[numbers]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[decimals]: https://docs.python.org/3/library/decimal.html#decimal.Decimal
[fractions]: https://docs.python.org/3/library/fractions.html#fractions.Fraction
[sequence types]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range