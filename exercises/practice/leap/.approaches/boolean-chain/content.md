# Chain of boolean expressions

```python
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
```

This might be considered the "most idiomatic" or "most Pythonic" solution, as it is exactly the same as the code implemented by the maintainers of the Python language for the [`calendar.isleap()`][isleap-source] method.

The first boolean expression uses the [modulo operator][modulo-operator] to check if the year is evenly divisible by `4`.
- If the year is _not_ evenly divisible by `4`, then the chain will [short circuit][short-ciruiting] due to the next operator being a [logical AND][logical-and] (`and`), and will return `False`.
- If the year _is_ evenly divisible by `4`, then the year is checked to _not_ be evenly divisible by `100`.
- If the year is not evenly divisible by `100`, the expression is `True` and the chain will short circuit and return `True`, since the next operator is a [logical OR][logical-or] (`or`).
- If the year _is_ evenly divisible by `100`, then the expression is `False`, and the returned value from the chain will be `True` if the year is evenly divisible by `400`.


| year | year % 4 == 0 | year % 100 != 0 | year % 400 == 0 | is leap year |
| ---- | ------------- | --------------- | --------------- | ------------ |
| 2020 |          True |            True |   not evaluated |         True |
| 2019 |         False |   not evaluated |   not evaluated |        False |
| 2000 |          True |           False |            True |         True |
| 1900 |          True |           False |           False |        False |


The chain of boolean expressions is efficient, as it proceeds from testing the most to least likely conditions.
It is the fastest approach when testing a year that is not evenly divisible by `100` and is not a leap year.


## Operator precedence

The implementation contains one set of parentheses, around the `or` clause:
- One set is enough, because the `%` operator is highest priority, then the `==` and `!=` relational operators.
- Those parentheses are required, because `and` is higher priority than `or`.
In Python, `a and b or c` is interpreted as `(a and b) or c`, which would give the wrong answer for this exercise.

If in doubt, it is always permissible to add extra parentheses for clarity.


## Variation 1

By using the [falsiness][falsiness] of `0`, the [`not` operator][not-operator] can be used instead of comparing equality to `0`:


```python
def leap_year(year):
    return not year % 4 and (year % 100 != 0 or not year % 400)
    
```

It can be thought of as the expression _not_ having a remainder.

[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/#falsy-and-truthy-values
[isleap-source]: https://github.com/python/cpython/blob/3.13/Lib/calendar.py#L143-L145
[logical-and]: https://realpython.com/python-and-operator/
[logical-or]: https://realpython.com/python-or-operator/
[modulo-operator]: https://realpython.com/python-modulo-operator/
[not-operator]: https://realpython.com/python-not-operator/
[short-ciruiting]: https://mathspp.com/blog/pydonts/boolean-short-circuiting#short-circuiting-in-plain-english
