# Introduction

There are multiple approaches to solving the Leap exercise in Python.
You can use a chain of boolean expressions or a [`ternary operator`][ternary-operator] to test conditions.
You can also utilize built-in methods from the `datetime` or `calendar` modules.


## General Guidance

The key to efficiently solving Leap is to calculate if the year is evenly divisible by `4`, `100` and `400`.
Using the [modulo operator][modulo-operator] is a good way of determining that.


## Approach: Chain of Boolean Expressions


```python
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
```

For more information, see the [Boolean chain approach][approach-boolean-chain].


## Approach: Ternary Operator of Boolean Expressions

```python
def leap_year(year):
    return (not year % 400 if not year % 100 else not year % 4)
    
```

For more information, see the [Ternary operator approach][approach-ternary-operator].


## Other Approaches

Besides the aforementioned idiomatic approaches, you could also approach the exercise as follows:


### Approach: Using `datetime` Addition

Add a day to February 28th for the year and see if the new day is the 29th.
However, this approach may trade speed for convenience.

```python
import datetime

def leap_year(year):
    return (datetime.datetime(year, 2, 28) + datetime.timedelta(days=1)).day == 29
```

For more information, see the [`datetime` addition approach][approach-datetime-addition].


### Approach: Using the `calendar` module

It is possible to use [`calendar.isleap(<year>)`][isleap] from the standard library, which solves this exact problem:


```python
from calendar import isleap

def leap_year(year):
    return isleap(year)
```

This is self-defeating in the context of Exercism.
This practice exercise was designed to explore ways to use `booleans` and boolean logic.
The point is not _really_ leap year determination.
In a wider context, anyone testing for leap years is likely using `calendar` or related modules (_hand rolling your own test is likely to introduce bugs_), so it is good to know what library functions are available.

For more discussion, see the [`calendar.isleap()` approach][approach-calendar-isleap].


## Which approach to use?

- The chain of `boolean expressions` should be the most efficient, as it proceeds from most to least likely conditions and takes advantage of [`short-circuiting`][short-circuting].
It has a maximum of three checks.
It is the fastest approach when testing a year that is not evenly divisible by `100` that is not a leap year.
Since most years fit those conditions, it is overall the most efficient approach.
It also happens to be the approach taken by the maintainers of the Python language in [implementing `calendar.isleap()`][calendar_isleap-code].

- The `ternary operator` approach has a maximum of only two checks, but it starts from a less likely condition.
The `ternary operator` was faster in benchmarking when the year was a leap year or was evenly divisible by `100`,
but those are the _least likely_ conditions!
- Using `datetime` addition may be considered a "cheat" for the exercise, and it was slower by far than the other approaches in benchmarking, due to import and method overhead.

For more information, check out the [Performance article][article-performance].


[approach-boolean-chain]: https://exercism.org/tracks/python/exercises/leap/approaches/boolean-chain
[approach-calendar-isleap]: https://exercism.org/tracks/python/exercises/leap/approaches/calendar-isleap
[approach-datetime-addition]: https://exercism.org/tracks/python/exercises/leap/approaches/datetime-addition
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/leap/approaches/ternary-operator
[article-performance]: https://exercism.org/tracks/python/exercises/leap/articles/performance
[calendar_isleap-code]: https://github.com/python/cpython/blob/3.13/Lib/calendar.py#L143-L145
[isleap]: https://docs.python.org/3/library/calendar.html#calendar.isleap
[modulo-operator]: https://realpython.com/python-modulo-operator/
[short-circuting]: https://www.pythonmorsels.com/short-circuit-evaluation/
[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
