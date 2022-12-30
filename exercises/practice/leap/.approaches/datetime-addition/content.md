# `datetime` addition

```python
import datetime


def leap_year(year):
    return (datetime.datetime(year, 2, 28)
            + datetime.timedelta(days=1)).day == 29

```

```exercism/caution
This approach may be considered a "cheat" for this exercise.
```

By adding a day to February 28th for the year, you can see if the new day is the 29th or the 1st.
If it is the 29th, then the function returns `True` for the year being a leap year.

- A new [datetime][datetime] object is created for February 28th of the year.
- Then the [timedelta][timedelta] of one day is added to that `datetime`,
  and the function returns if the [day][day] property of the resulting `datetime` object is the 29th.

[timedelta]: https://docs.python.org/3/library/datetime.html#timedelta-objects
[day]: https://docs.python.org/3/library/datetime.html#datetime.datetime.day
[datetime]: https://docs.python.org/3/library/datetime.html#datetime-objects
