# Introduction

There are various idiomatic approaches to solve Leap.
You can use a chain of boolean expressions to test the conditions.
Or you can use a [ternary operator][ternary-operator].

## General guidance

The key to solving Leap is to know if the year is evenly divisible by `4`, `100` and `400`.
For determining that, you will use the [modulo operator][modulo-operator].

## Approach: Chain of Boolean expressions

```python
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
```

For more information, check the [Boolean chain approach][approach-boolean-chain].

## Approach: Ternary operator of Boolean expressions

```python
def leap_year(year):
    return (not year % 400 if not year % 100 else not year % 4)
    
```

For more information, check the [Ternary operator approach][approach-ternary-operator].

## Other approaches

Besides the aforementioned, idiomatic approaches, you could also approach the exercise as follows:

### Approach: datetime addition

Add a day to February 28th for the year and see if the new day is the 29th. For more information, see the [`datetime` addition approach][approach-datetime-addition].

## Which approach to use?

- The chain of boolean expressions should be the most efficient, as it proceeds from the most likely to least likely conditions.
It has a maximum of three checks.
It is the fastest approach when testing a year that is not evenly divisible by `100` and is not a leap year.
Since most years fit those conditions, it is overall the most efficient approach.
- The ternary operator has a maximum of only two checks, but it starts from a less likely condition.
The ternary operator was faster in benchmarking when the year was a leap year or was evenly divisible by `100`,
but those are the least likely conditions.
- Using `datetime` addition may be considered a "cheat" for the exercise, and it was slower than the other approaches in benchmarking.

For more information, check the [Performance article][article-performance].

[modulo-operator]: https://realpython.com/python-modulo-operator/
[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[approach-boolean-chain]: https://exercism.org/tracks/python/exercises/leap/approaches/boolean-chain
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/leap/approaches/ternary-operator
[approach-datetime-addition]: https://exercism.org/tracks/python/exercises/leap/approaches/datetime-addition
[article-performance]: https://exercism.org/tracks/python/exercises/leap/articles/performance
