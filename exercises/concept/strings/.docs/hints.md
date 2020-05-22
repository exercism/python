## General

- The [Python documentation for `str`][python-str-doc] has an overview of the Python `str` type.

## 1. Get message from a log line

- Strings in Python have [lots of convenient instance methods][str-type-methods] for cleaning, splitting, manipulating, and creating new strings. Extracting values from a string could be done by splitting it based on a substring, for example.

## 2. Get log level from a log line

- Strings also have methods that help convert letters from lower to uppercase and vice-versa.

## 3. Reformat a log line

Strings are immutable, but can be combined together to make new strings, or have elements replaced. This goal can be accomplished by using string methods, or operators like `+` or `+=` (which are overloaded to work with strings).
Python also has a concept of string formatting, like many other languages.

- The [`str.join()`][str-join] method is useful to join an iterable of strings into one string by interspersing them with a common value, e.g. `":".join("abcde")` would create `"a:b:c:d:e"`.
- [`str.format()`][str-format] is an idiomatic way to do string interpolation in Python (inserting one or more string value(s) into another).
- [Format strings][format-str] are another convenient way to interpolate values into a string. This strategy is particularly useful when more than one named variable needs to be inserted into a final output.

[python-str-doc]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[str-type-methods]: https://docs.python.org/3/library/stdtypes.html#str
[str-join]: https://docs.python.org/3/library/stdtypes.html#str.join
[str-format]: https://docs.python.org/3/library/stdtypes.html#str.format
[format-str]: https://docs.python.org/3/library/string.html#formatstrings
