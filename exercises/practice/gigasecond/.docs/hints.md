# Hints

## General

- Your code should parse a datetime object, add a gigasecond's worth of time to it, and then return the result as a datetime object.

- If you're having trouble, remember to take a look at the provided test cases under the Tests tab. These will help you figure out what the expected inputs and outputs of your function(s) should be.

## Reading long numbers

Most of the time, code is read rather than written, and writing a big number can be a challenge to read.

Here are two approaches to making big numbers more readable:

### Approach: Underscores in Numeric Literals

`_` can accept as a thousands operator

**ie:** 1\*000_000 is far more readable than 1000000

For more information check [reference][underscores_notation].

### Approach: Exponential notation or scientific notation

The e (or E) character followed by an integer represents the power of 10 by which the number preceding the e should be multiplied.

**ie:** `1e6`, 1 is multiplied by 10 raised to the power of 6, which equals `1000000`

For more information check [reference][scientific_notation].

[underscores_notation]: https://peps.python.org/pep-0515/#:~:text=The%20syntax%20would%20be%20the,width%20of%2010%20with%20*%20separator.
[scientific_notation]: https://python-reference.readthedocs.io/en/latest/docs/float/scientific.html
