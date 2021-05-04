# String Methods in Python

A `str` is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
These could include letters, diacritical marks, positioning characters, numbers, currecy symbols, emoji, punctuation, space and line break characters, and more.

Strings implement all [common sequence operations][common sequence operations], and can be iterated through using `for item in <string>` or `for index, item in enumerate(<string>)` syntax.
Strings can be concatenated with `+`, or via `<str>.join(<iterable>)`, split via `<str>.split(<separator>)`, and offer multiple types of formatting.

To further work with strings, Python provides a rich set of [string methods][str-methods] that can assist with searching, cleaning, transforming, translating, and many other operations.

Some of the more commonly used `str` methods include:

- Checking for prefixes/suffixes with `startswith()` and `endswith()`
- Altering string casing with methods like `upper()`, `lower()`, and `swapcase()`
- Removing leading or trailing characters from a string using `strip()`, `lstrip()`, or `rstrip()`
- Replacing substrings with the `replace()` method
- Checking for the existence of a substring with `in`

The `str` type is _immutable_, so all of these methods will return a new `str` instead of modifying the existing one.

For more information, you can check out the strings [informal tutorial][informal tutorial] or the [`str` docs][str-methods].

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[informal tutorial]: https://docs.python.org/3/tutorial/introduction.html#strings
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
