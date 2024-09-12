# Dig deeper
There is only one correct and safe way to deal with date and datetime in python. We are going to use the built-in `datetime` module. A `datetime` object contains multiple attributes, like `year`, `month`, `day`, `hour`, `minute` and `second`.
But you can't update a `datetime` object directly like:
```py
from datetime import datetime
datetime_2000_01_25 = datetime(year = 2000, month = 1, day = 25)
wrong_date = datetime_2000_01_25 + "2 weeks" # This won't work at all
```
Instead, we have to use another one object, `timedelta`. It will be used to accomplish the same thing as shown in the previous example. This object is a time interval, which can be used to modify a `datetime` object. We can add or subtract the `timedelta` to a `datetime` object to create a new `datetime` object with the updated values.
```py
from datetime import timedelta, datetime
datetime_2000_01_01 = datetime(year = 2000, month = 1, day = 1)
delta = timedelta(weeks=2)
datetime_2000_01_15 = datetime_2000_01_01 + delta
```
In the exercise, we have one `datetime` parameter, so one of the correct answer is:
```py
from datetime import timedelta, datetime
def add(moment: datetime) -> datetime: 
    return moment + timedelta(seconds=10**9)
```
For more information, check the official [datetime documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.year)
