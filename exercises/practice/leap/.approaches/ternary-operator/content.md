# Ternary operator

```python
def leap_year(year):
    return not year % 400 if not year % 100 else not year % 4
    
```

A [ternary operator][ternary-operator] uses a maximum of two checks to determine if a year is a leap year.

It starts by testing the outlier condition of the year being evenly divisible by `100`.
It does this by using the [modulo operator][modulo-operator].
Also, by using the [falsiness][falsiness] of `0`, the [`not` operator][not-operator] can be used instead of comparing equality to `0`.

- If the year is evenly divisible by `100`, then the expression is `True`, and the ternary operator returns if the year is evenly divisible by `400`.
- If the year is _not_ evenly divisible by `100`, then the expression is `False`, and the ternary operator returns if the year is evenly divisible by `4`.

| year | year % 100 == 0 | year % 400 == 0 | year % 4 == 0  | is leap year |
| ---- | --------------- | --------------- | -------------- | ------------ |
| 2020 |           False |   not evaluated |           True |        True  |
| 2019 |           False |   not evaluated |          False |       False  |
| 2000 |           True  |            True |  not evaluated |        True  |
| 1900 |           True  |           False |  not evaluated |        False |

Although it uses a maximum of only two checks, the ternary operator tests an outlier condition first,
making it less efficient than another approach that would first test if the year is evenly divisible by `4`,
which is more likely than the year being evenly divisible by `100`.
The ternary operator was fastest in benchmarking when the year was a leap year or was evenly divisible by `100`,
but those are the least likely conditions.

[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[modulo-operator]: https://realpython.com/python-modulo-operator/
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[not-operator]: https://realpython.com/python-not-operator/
