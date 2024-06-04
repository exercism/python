# Instructions

Your task is to find the exact date of a meetup, given a month, year, weekday and week.

There are five week values to consider: `first`, `second`, `third`, `fourth`, `last`, `teenth`.

For example, you might be asked to find the date for the meetup on the first Monday in January 2018 (January 1, 2018).

Similarly, you might be asked to find:

- the third Tuesday of August 2019 (August 20, 2019)
- the teenth Wednesday of May 2020 (May 13, 2020)
- the fourth Sunday of July 2021 (July 25, 2021)
- the last Thursday of November 2022 (November 24, 2022)
- the teenth Saturday of August 1953 (August 15, 1953)

## Teenth

The teenth week refers to the seven days in a month that end in '-teenth' (13th, 14th, 15th, 16th, 17th, 18th and 19th).

If asked to find the teenth Saturday of August, 1953, we check its calendar:

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

From this we find that the teenth Saturday is August 15, 1953.
