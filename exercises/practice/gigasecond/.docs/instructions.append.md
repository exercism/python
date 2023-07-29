# Instructions append

## Reading and Writing Long Numbers

Code is more often _read_ than it is written, and reading a big/long number within other text can be a challenge.
Here are two approaches to making numbers more readable:

1. Using underscores in Numeric Literals. `1_000_000` is more readable than `1000000`, and `10_100_201_330` is easier to scan than `10100201330`. For more information, see [PEP-0515][underscores_notation].

2. Using exponential notation or scientific notation. The e (or E) character followed by an integer represents the power of 10 by which the number preceding the e should be multiplied (_**ie:** `1e6`, 1 is multiplied by 10 raised to the power of 6, which equals `1000000`_). For more details, check out this reference on [scientific notation][scientific_notation].


## Dates and Times in Python

This exercise explores objects from Python's `datetime` module:

- [Official Python documentation on the datetime module][datetime]
- [datetime objects][datetime.datetime]
- [timedelta objects][datetime.timedelta]

[datetime.datetime]: https://docs.python.org/3.9/library/datetime.html#datetime.datetime
[datetime.timedelta]: https://docs.python.org/3.9/library/datetime.html#timedelta-objects
[datetime]: https://docs.python.org/3.9/library/datetime.html#module-datetime
[scientific_notation]: https://python-reference.readthedocs.io/en/latest/docs/float/scientific.html
[underscores_notation]: https://peps.python.org/pep-0515/#:~:text=The%20syntax%20would%20be%20the,width%20of%2010%20with%20*%20separator.
