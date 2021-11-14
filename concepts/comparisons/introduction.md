# Introduction

A [comparison operator][comparisons] in Python (_also called a Python relational operator_), looks at the values of two operands and returns `True` or `False` based on whether the `comparison` condition is met. The most common comparison operators are `"<"`, `">"`, `"=="`, `">="`, `"<="`, and `"!="`. They all have the same priority (which is higher than that of the Boolean operations)

## Comparison Chaining

Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y` `and` `y <= z`, except that `y` is evaluated only once (but in both cases `z` is _not_ evaluated at all when `x < y` is found to be `False`). This is also called `short-circuit` evaluation which means the execution is stopped if the truth value of the expression has already been determined. Note that the evaluation of expression takes place from left to right. In python, short circuiting is supported by various boolean operators, functions and, in this case, comparison chaining.

## Comparison of different data types

Since everything in Python is an `object`, things can get interesting when objects of different types are compared. For example, the `str` value of a number is considered completely different from the `integer` or `floating-point` value. However, an `integer` **can** be considered equal to a `float`, as they are both numeric types that Python can implicitly convert to compare. For other numeric types, comparison operators are defined where they "make sense", but throw a `TypeError` if the underlying objects cannot be converted for comparison. For more information on the rules that python uses for numeric conversion, see [arithmetic conversions][arithmetic conversions] in the Python documentation.

[comparisons]: https://docs.python.org/3/library/stdtypes.html?
[arithmetic conversions]: https://docs.python.org/3/reference/expressions.html?highlight=number%20conversion#arithmetic-conversions
