# Introduction

_"Dates and times are something we teach to young children. How hard can it be?"_

Many programmers have made that mistake, and the subsequent experience tends to be negative to their health and happiness. 

Anyone doing non-trivial programming with dates and times should at least be prepared to understand and mitigate potential problems.

## The `datetime` module

In python, a wide range of date and time functionality is collected in the [`datetime`][datetime] module.
This can be supplemented by other libraries, but `datetime` is central and often sufficient.

There are five major classes within `datetime`:
 - `datetime.date` for simple dates
 - `datetime.time` for simple times
 - `datetime.datetime` combines date, time and optionally timezone information
 - `datetime.timedelta` for intervals
 - `datetime.timezone` to handle the reality that few people use UTC

 ___Notation detail:___ A `datetime.time` or `datetime.datetime` object that includes timezone information is said to be _aware_, otherwise it is _naive_.
 A `datetime.date` object is always naive.

As `datetime` is a large module with many methods and attributes, only some of the most common will be discussed here.

You are encouraged to explore the [full documentation][datetime].
Dates and times are complex but important, so the Python developers have put many years of effort into trying to support most use cases.

Perhaps the most frequent needs are:

- Parse some appropriate input format to construct a `datetime` object.
This often uses [`strptime()`][strptime-strftime].
- Get the required numerical or string format from a `datetime` object.
String output often uses [`strftime()`][strptime-strftime].
- Apply an offset to a `date`, `time` or `datetime` to create a new object (of the same type).
- Calculate the interval between two such objects.
- Get the current date and/or time.
This will be obtained from the host computer and converted to a Python object.


### Date and time formats

There are many ways to write dates and times, which tend to be culturally-specific.
All-number dates such as "7/6/23" are ambiguous, confusing, and have led to many expensive mistakes in multinational organizations.

The international standard is defined in [`ISO 8601`][ISO8601], with two main advantages:
- Parsing is quick and unambiguous.
- Sorting is easy, as the datetime can be treated as text.

An example:

```python
>>> from datetime import datetime
>>> datetime.now(timezone.utc).isoformat()
'2023-12-04T17:54:13.014513+00:00'
```

This is built up from various parts, with only the date fields required:
- `YYYY-MM-DD`
- Optionally, `Thh:mm:ss`
- Optionally, microseconds after the decimal point.
- Optionally, timezone offset from UTC with a sign and `hh:mm` value.

Internally, `date`, `time` and `datetime` are stored as Python objects with separate attributes for year, month, etc.
Examples of this will be shown below, when each class is discussed.

Most computer operating systems use POSIX timestamps: the number of seconds since `1970-01-01T00:00:00+00.00`. 
The `datetime` module makes it easy to import these.

For code which interacts mainly with computers rather than humans, it may be worth investigating the separate [`time`][time] module, which provides more complete support for POSIX timestamps.

## The [`datetime.date`][datetime-date] class

[`datetime.date`][datetime-date] is a relatively small and simple date-only class, with no understanding of times or timezones.

```python
>>> from datetime import date
>>> date.today()
datetime.date(2023, 12, 4)
>>> date.today().isoformat()
'2023-12-04'
```

The default display has the same `date(year, month, day)` syntax as the default constructor.
A `date` object can also be created from an ISO 8601 date string or a POSIX timestamp.

```python
>>> date(1969, 7, 20)
datetime.date(1969, 7, 20)

>>> date.fromisoformat('1969-07-20')
datetime.date(1969, 7, 20)

>>> date.fromisoformat('1969-07-20') == date(1969, 7, 20)
True
```

Individual parts of the date can be accessed as instance attributes:

```python
>>> date.today().month  # in December
12
```

There are a number of other methods, mostly related to output formats.
See the [class documentation][datetime-date] for details.

`datetime.date` is designed to be fairly minimalist, to keep simple applications simple.

If your application is ever likely to need times or timezones, it may be better to use `datetime.datetime` from the start.

For more complex date-only applications, compare `datetime.date` with [`calendar`][calendar] and decide which better fits your needs.

## The [`datetime.time`][datetime-time] class

`datetime.time` is the basic time-only class.
It has no understanding of dates: times automatically roll over to `time(0, 0, 0)` at midnight.

Timezone information can optionally be included.

The full constructor format is `timezone.time(hour, min, sec, microsec, timezone)`.

All the parameters are optional: numerical values will default to `0`, timezone to `None`.

```python
>>> from datetime import time
>>> time()
datetime.time(0, 0)
>>> time(14, 30, 23)
datetime.time(14, 30, 23)
```

Starting from an ISO 8601 format may be more readable in some cases:

```python
>>> time.fromisoformat('15:17:01-07:00')  # mid-afternoon in Arizona
datetime.time(15, 17, 1, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
```

Timezones will be discussed in more detail below.

Arithmetic is not possible with `datetime.time` objects, but they do support comparisons.

```python
>>> time1 = time(14, 45)
>>> time2 = time(16, 21, 30)
>>> time1 > time2
False
```

As with `date`, individual parts are available as instance attributes:

```python
>>> time(16, 21, 30).hour
16
```

For other methods and properties, see the [class documentation][datetime-time].
Much of it relates to working with timezones.

## The [`datetime.datetime`][datetime-datetime] class

`datetime.datetime` combines most of the features of the `date` and `time` classes and adds some extras.

It is the most versatile of these three classes, at the cost of some additional complexity.

```python
>>> from datetime import datetime

>>> datetime.now()
datetime.datetime(2023, 12, 4, 15, 45, 50, 66178)

>>> datetime.now().isoformat()
'2023-12-04T15:46:30.311480'
```

As with `date`, the default constructor has the same syntax as the default display.

The year, month and day parameters are required. Time parameters default to `0`. Timezone defaults to `None`, as in the example above.

Keeping all these parameters straight can be a challenge, so the ISO format may be preferable:

```python
>>> datetime.fromisoformat('2023-12-04T15:53+05:30')  # Delhi time
datetime.datetime(2023, 12, 4, 15, 53, tzinfo=datetime.timezone(datetime.timedelta(seconds=19800)))
```

Much of the functionality in `datetime.datetime` will be familar from `date` and time.

One addition that may be useful is `combine(date, time)` which constructs a `datetime` instance from a `date` and a `time` instance (and optionally a timezone).

```python
>>> today = date.today()
>>> current_time = time(4, 5)

>>> datetime.combine(today, current_time)
datetime.datetime(2023, 12, 4, 4, 5)

>>> datetime.combine(today, current_time).isoformat()
'2023-12-04T04:05:00'
```

For other methods and properties, see the [class documentation][datetime-time].
Much of it relates to working with timezones.


## The [`strptime()` and `strftime()`][strptime-strftime] methods

The `datetime.datetime` class supports a complementary pair of methods:
- `strptime()` parses a string representation to a `datetime` object.
- `strftime()` outputs a string representation of a `datetime` object.

Only `strftime()` is available in `datetime.date` and `datetime.time`.

A wide variety of format codes is available.
Some of the common ones are shown in the examples below, but see the [official documentation][strptime-strftime] for the full list.
These format codes are copied directly from C, and may be familiar to programmers who have worked in other languages.

```python
>>> date_string = '14/10/23 23:59:59.999999'
>>> format_string = '%d/%m/%y %H:%M:%S.%f'
>>> dt = datetime.strptime(date_string, format_string)
>>> dt
datetime.datetime(2023, 10, 14, 23, 59, 59, 999999)

>>> dt.strftime('%a %d %b %Y, %I:%M%p')
'Sat 14 Oct 2023, 11:59PM'
```

## Related modules

This Concept has concentrated on the [`datetime`][datetime] module.

Python has other modules which work with dates and times.

### The [`time`][time] module
Optimized for working with computer timestanps, for example in software logs.

Not to be confused with `datetime.time`, a completely separate class.

### The [`calendar`][calendar] module
An alternative to `datetime.date`, `calendar` is more sophisticated in dealing with dates across a wide span of historical and future time.

It also has CSS methods to halp with displaying calendars.


### The [`zoneinfo`][zoneinfo] module
Mainly consisting of the `ZoneInfo` class, a subclass of `datetime.tzinfo` which supports the [IANA database][IANA] and automatic DST adjustments.



[ISO8601]: https://en.wikipedia.org/wiki/ISO_8601
[datetime]: https://docs.python.org/3/library/datetime.html
[datetime-date]: https://docs.python.org/3/library/datetime.html#date-objects
[datetime-time]: https://docs.python.org/3/library/datetime.html#time-objects
[datetime-datetime]: https://docs.python.org/3/library/datetime.html#datetime-objects
[datetime-timedelta]: https://docs.python.org/3/library/datetime.html#timedelta-objects
[datetime-tzinfo]: https://docs.python.org/3/library/datetime.html#tzinfo-objects
[datetime-timezone]: https://docs.python.org/3/library/datetime.html#timezone-objects
[strptime-strftime]: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
[time]: https://docs.python.org/3/library/time.html
[calendar]: https://docs.python.org/3/library/calendar.html
[ABC]: https://docs.python.org/3/library/abc.html
[zoneinfo]: https://docs.python.org/3/library/zoneinfo.html
[tzdata]: https://peps.python.org/pep-0615/
[IANA]: https://en.wikipedia.org/wiki/Tz_database
[IANA-names]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones


