# Instructions

Recurring monthly meetups are generally scheduled on the given weekday of a given week each month.
In this exercise you will be given the recurring schedule, along with a month and year, and then asked to find the exact date of the meetup.

For example a meetup might be scheduled on the _first Monday_ of every month.
You might then be asked to find the date that this meetup will happen in January 2018.
In other words, you need to determine the date of the first Monday of January 2018.

Similarly, you might be asked to find:

- the third Tuesday of August 2019 (August 20, 2019)
- the teenth Wednesday of May 2020 (May 13, 2020)
- the fourth Sunday of July 2021 (July 25, 2021)
- the last Thursday of November 2022 (November 24, 2022)

The descriptors you are expected to process are: `first`, `second`, `third`, `fourth`, `last`, `teenth`.

Note that descriptor `teenth` is a made-up word.

It refers to the seven numbers that end in '-teen' in English: 13, 14, 15, 16, 17, 18, and 19.
But general descriptions of dates use ordinal numbers, e.g. the _first_ Monday, the _third_ Tuesday.

For the numbers ending in '-teen', that becomes:

- 13th (thirteenth)
- 14th (fourteenth)
- 15th (fifteenth)
- 16th (sixteenth)
- 17th (seventeenth)
- 18th (eighteenth)
- 19th (nineteenth)

So there are seven numbers ending in '-teen'.
And there are also seven weekdays (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).
Therefore, it is guaranteed that each day of the week (Monday, Tuesday, ...) will have exactly one numbered day ending with "teen" each month.

If asked to find the teenth Saturday of August, 1953 (or, alternately the "Saturteenth" of August, 1953), we need to look at the calendar for August 1953:

```plaintext
    August 1953
Su Mo Tu We Th Fr Sa
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

The Saturday that has a number ending in '-teen' is August 15, 1953.
