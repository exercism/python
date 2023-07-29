# Hints

## General

- Your function should parse the passed-in [datetime object][datetime], add a gigasecond's worth of time to it, and then return the result.

- If you're having trouble, remember to take a look at the provided test cases under the Tests tab. These will help you figure out what the expected inputs and outputs of your function(s) should be.

- Most of the time, code is read rather than written, and a big number can be a challenge to read. Here are a couple of approaches to making big numbers in your code more readable:

  - Using underscores (`_`) in numeric literals can help offset thousands, hundred-thousands, millions, etc. (_**ie:** `1_000_000` or `10_100_201_330` is far more readable than `1000000` or `10100201330`._) See [PEP-0515][underscores_notation] for more information.

   - Scientific notation can be more compact and easier to scan when there are very large numbers (_**ie:** `1e6`, 1 is multiplied by 10 raised to the power of 6, which equals `1000000`_). For more information, see this reference on [scientific notation][scientific_notation].

[datetime]: https://docs.python.org/3.9/library/datetime.html#datetime.datetime
[scientific_notation]: https://python-reference.readthedocs.io/en/latest/docs/float/scientific.html
[underscores_notation]: https://peps.python.org/pep-0515/#:~:text=The%20syntax%20would%20be%20the,width%20of%2010%20with%20*%20separator.
