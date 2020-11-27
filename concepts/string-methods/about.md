## String Methods in Python

A string (`str`) in Python is a sequence of Unicode code points which
include letters, numbers, symbols, punctuation, etc. Strings
implement all of the [common sequence operations](https:/docs.python.org/3/library/stdtypes.html#typesseq-common),
along with iteration using the `for item in <string>` syntax.

Python provides a number of useful methods that you can use to manipulate
strings. These string methods can be used for cleaning, splitting, translating,
or otherwise working with the `str` type. New strings can be created based
on method arguments, and/or additional information can be returned. Strings
can be concatenated using the `+` operator or with `str.join()`.

Some of the more commonly used methods include:

- Checking for prefixes/suffixes with `startwith()` and `endswith()`
- Altering string casing with methods like `upper()`, `lower()`, and `swapcase()`
- Removing leading or trailing characters from a string using `strip()`, `lstrip()`, or `rstrip()`
- Replacing substrings with the `replace()` method
- Checking for the existence of a substring with `in`
- Concatenating strings with the `+` operator or `str.join()`

The `str` type is _immutable_, so all of these methods will return a new `str` instead of modifying the existing one.

For more information, you can check out the
[official documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).
