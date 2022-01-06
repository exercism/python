# Introduction

A [comparison operator][comparisons] in Python (_also called a Python relational operator_), looks at the _values_ of two [operands][operand] and returns a boolean `True` or `False` if the `comparison` condition is or is not met.

The table below shows the most common Python comparison operators:


| Operator | Operation                | Description                                                    |
| -------- | ------------------------ | -------------------------------------------------------------- |
| `>`      | "greater than"             | `a > b` is `True` if `a` is **strictly** greater in value than `b` |
| `<`      | "less than"                | `a < b` is `True` if `a` is **strictly** less in value than `b`    |
| `==`     | "equal to"                 | `a == b` is `True` if `a` is **strictly** equal to `b` in value    |
| `>=`     | "greater than or equal to" | `a >= b` is `True` if `a > b` OR `a == b` in value             |
| `<=`     | "less than or equal to"    | `a <= b` is `True` if `a < b` or `a == b` in value             |
| `!=`     | "not equal to"             | `a != b` is `True` if `a == b` is `False`                      |
| `is`     | "identity"                 | `a is b` is `True` if **_and only if_** `a` and `b` are the same _object_  |
| `is not` | "negated identity"                 | `a is not b` is `True` if `a` and `b` are **not** the same _object_ |
| `in`     | "containment test"         | `a in b` is `True` if `a` is member, subset, or element of `b`               |
| `not in` | "negated containment test" | `a not in b` is `True` if `a` is not a member, subset, or element of `b`     |


They all have the same priority (_which is higher than that of [Boolean operations][boolean operations], but lower than that of arithmetic or bitwise operations_).


## Comparison between different data types

Objects that are different types (_except numeric types_) never compare equal by default.
Non-identical instances of a `class` will also _**not**_ compare as equal unless the `class` defines special methods that customize the default `object` comparison behavior.


Numeric types are (mostly) an exception to this type matching rule.
An `integer` **can** be considered equal to a `float` (_or an [`octal`][octal] equal to a [`hexadecimal`][hex]_), as long as the types can be implicitly converted for comparison.

For the other numeric types ([complex][complex numbers], [decimal][decimal numbers], [fractions][rational numbers]), comparison operators are defined where they "make sense" (_where implicit conversion does not change the outcome_), but throw a `TypeError` if the underlying objects cannot be accurately converted for comparison.


## Comparing object identity

The operators `is` and `is not` test for object [_identity_][object identity], as opposed to object _value_.
An object's identity never changes after creation and can be found by using the [`id()`][id function] function.

\<apple\> `is` \<orange\> evaluates to `True` if _**and only if**_ `id(<apple>)` == `id(<orange>)`.
apple `is not` orange yields the inverse.

Due to their singleton status, `None` and `NotImplemented` should always be compared to items using `is` and `is not`.


## Membership comparisons

The operators `in` and `not in` test for _membership_.
\<fish\> `in` \<soup\> evaluates to `True` if \<fish\> is a member of \<soup\> (_if \<fish\> is a subset of or is contained within \<soup\>_), and evaluates `False` otherwise.
\<fish\> `not in` \<soup\> returns the negation, or _opposite of_ \<fish\> `in` \<soup\>.

For string and bytes types, \<name\> `in` \<fullname\> is `True` _**if and only if**_ \<name\> is a substring of \<fullname\>.

[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html?highlight=comparisons#comparisons
[complex numbers]: https://docs.python.org/3/library/functions.html#complex
[decimal numbers]: https://docs.python.org/3/library/decimal.html
[hex]: https://docs.python.org/3/library/functions.html?highlight=hex#hex
[id function]: https://docs.python.org/3/library/functions.html#id
[object identity]: https://docs.python.org/3/reference/datamodel.html
[octal]: https://docs.python.org/3/library/functions.html?#oct
[operand]: https://www.computerhope.com/jargon/o/operand.htm
[rational numbers]: https://docs.python.org/3/library/fractions.html
