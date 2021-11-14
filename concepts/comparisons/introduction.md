# Introduction

A [comparison operator][comparisons] in Python (_also called a Python relational operator_), looks at the values of two operands and returns `True` or `False` based on whether the `comparison` condition is met. The most common comparison operators are `"<"`, `">"`, `"=="`, `">="`, `"<="`, and `"!="`.


```python
```

## Comparison Chaining

Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y` `and` `y <= z`, except that `y` is evaluated only once (but in both cases `z` is _not_ evaluated at all when `x < y` is found to be `False`).

Also unlike `C`, expressions like `a < b < c` have the interpretation that is conventional in mathematics.

```python
>>> x, y, z = 2, 5, 10
>>> x < y < z
True
>>> x < y > z
False
>>> x > y < z
False
```

## Comparison of different data types

Since everything in `python` represents an `object` things start getting interesting when we compare objects of different types. For example, the `string` value of a number is considered a completely different value from the `integer` or `floating-point` version, an `integer` can be equal to a `floating point`.

```python
>>> 17 == '17'
False
>>> 17 == 17.0
True
>>> 17.0 == 0017.000
True
```

Python makes this distinction because strings are text, while `integers` and `floats` are both numbers.
