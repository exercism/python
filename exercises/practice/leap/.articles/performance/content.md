# Performance

In this article, we'll find out how to most efficiently calculate if a year is a leap year in Python.

The [approaches page][approaches] lists two idiomatic approaches to this exercise:

1. [Using the boolean chain][approach-boolean-chain]
2. [Using the ternary operator][approach-ternary-operator]

For our performance investigation, we will also include a two further approaches:
3. [datetime addition][approach-datetime-addition]
4. The [`calendar.isleap()`][approach-calendar-isleap] function from the calendar module in the standard library


## Benchmarks

To benchmark the approaches, we wrote a [small benchmark application][benchmark-application] using the [`timeit`][timeit] module.
All methods are "fast", but the difference may be easier to see graphically.
**Note**: The y-axis values in the chart have a `1e-7` multiplier.
 All run times are sub-microsecond.

!["Grouped Bar Chart showing execution timings for 4 leap approaches using the years 1900, 200, 2019, and 202 as input data. Described under the heading Timings for approaches by input year."](https://assets.exercism.org/images/tracks/python/leap/leap_timeit_bar_plot-light.svg)


### Timings for approaches by input year

<br>

|                 |    1900 |    2000 |    2019 |    2020 |
|:----------------|--------:|--------:|--------:|--------:|
| if-statements   | 1.7e-07 | 1.6e-07 | 9.0e-08 | 1.3e-07 |
| ternary         | 1.2e-07 | 1.0e-07 | 1.1e-07 | 1.1e-07 |
| datetime-add    | 6.9e-07 | 6.7e-07 | 7.0e-07 | 6.7e-07 |
| calendar-isleap | 2.2e-07 | 2.2e-07 | 1.4e-07 | 1.7e-07 |

<br>

- The `if-statements` (_boolean chain_) is the fastest approach when testing a year that is not evenly divisible by `100` and is not a leap year.
Since most years fit those conditions, it is overall the most efficient approach.
- The ternary operator is faster in benchmarking when the year is a leap year or is evenly divisible by `100`,
but those are the least likely conditions.
- Adding to the `datetime` may not only be a "cheat", but it is slower than the other approaches.
  - Comparing `import datatime` and `from datetime import datetime, timedelta` showed  little speed difference _(data not shown)_.
- Using the built-in `calendar.isleap()` function is terse, convenient and very readable, but not quite as fast as writing your own logic.
This is likely due to the overhead of both loading the `calendar` module and then calling `calendar.isleap()`.

Often, it is helpful to the programmer to use imported packages, but a large `import` to use a simple function may not give the fastest code.
Consider the context, and decide which is best for you in each case.

[approach-boolean-chain]: https://exercism.org/tracks/python/exercises/leap/approaches/boolean-chain
[approach-calendar-isleap]: https://exercism.org/tracks/python/exercises/leap/approaches/calendar-isleap
[approach-datetime-addition]: https://exercism.org/tracks/python/exercises/leap/approaches/datetime-addition
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/leap/approaches/ternary-operator
[approaches]: https://exercism.org/tracks/python/exercises/leap/approaches
[benchmark-application]: https://github.com/exercism/python/blob/main/exercises/practice/leap/.articles/performance/code/Benchmark.py
[timeit]: https://docs.python.org/3/library/timeit.html
