# `datetime` addition

```python
from datetime import datetime, timedelta


def leap_year(year):
    return (datetime(year, 2, 28)
            + timedelta(days=1)).day == 29
```

~~~~exercism/note
This approach may be considered a "cheat" for this exercise, which is intended to practice Boolean operators and boolean logic.
It also adds overhead in both performance and memory, as it imports methods from the `datetime` module and requires the instantiation of both a `datetime` object and a `timedelta` object.

For more information, see the performance article for this exercise.
~~~~


By adding a day to February 28th for a given year, you can see if the new day falls on the 29th of February or the 1st of March.
If it is February 29th, then the function returns `True` for the year being a leap year.

- A new [`datetime`][datetime] object is created for February 28th of the year.
- A [`timedelta`][timedelta] of one day is added to that `datetime`,
- The function returns if the [`day`][day] property of the resulting `datetime` object is the 29th.

[datetime]: https://docs.python.org/3/library/datetime.html#datetime-objects
[day]: https://docs.python.org/3/library/datetime.html#datetime.datetime.day
[timedelta]: https://docs.python.org/3/library/datetime.html#timedelta-objects
