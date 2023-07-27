# Instructions append

## Dates and Times in Python

This exercise explores objects from Python's `datetime` module:

- [Official Python documentation on the datetime module][datetime]
- [datetime objects][datetime.datetime]
- [timedelta objects][datetime.timedelta]

## Reading long numbers

Most of the time, code is read rather than written, and writing a big number can be a challenge to read.

Here are two approaches to making big numbers more readable:

### Approach: Underscores in Numeric Literals

`_` can accept as a thousands operator

**ie:** `1_000_000` is far more readable than `1000000`

For more information check [reference][underscores_notation].

### Approach: Exponential notation or scientific notation

The e (or E) character followed by an integer represents the power of 10 by which the number preceding the e should be multiplied.

**ie:** `1e6`, 1 is multiplied by 10 raised to the power of 6, which equals `1000000`

For more information check [reference][scientific_notation].

[datetime]: https://docs.python.org/3.9/library/datetime.html#module-datetime
[datetime.datetime]: https://docs.python.org/3.9/library/datetime.html#datetime.datetime
[datetime.timedelta]: https://docs.python.org/3.9/library/datetime.html#timedelta-objects
[underscores_notation]: https://peps.python.org/pep-0515/#:~:text=The%20syntax%20would%20be%20the,width%20of%2010%20with%20*%20separator.
[scientific_notation]: https://python-reference.readthedocs.io/en/latest/docs/float/scientific.html
