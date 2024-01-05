# The `calendar.isleap()` function

```pythoon
from calendar import isleap

def leap_year(year):
    return isleap(year)
```

~~~~exercism/caution
This approach may be considered a "cheat" for this exercise.
~~~~

The Python standard library includes a `calendar` module for working with many aspects of dates in the [Gregorian calendar][gregorian-calendar].

One of the methods provided is [`isleap()`][isleap], which implements exactly the same functionality as this exercise.

This is not a good way to practice the use of booleans, as the exercise intends.
However, it may be convenient if you are working with calendar functions more broadly.


[isleap]: https://docs.python.org/3/library/calendar.html
[gregorian-calendar]: https://en.wikipedia.org/wiki/Gregorian_calendar
