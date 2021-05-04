# Introduction

A `str` in Python is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
These could include letters, diacritical marks, positioning characters, numbers, currecy symbols, emoji, punctuation, space and line break characters, and more.

Strings implement all [common sequence operations][common sequence operations], and can be iterated through using `for item in <string>` or `for index, item in enumerate(<string>)` syntax.
Strings can be concatenated with `+`, or via `<str>.join()`, split via `<str>.split(<separator>)`, and offer multiple types of formatting.
To further work with strings, Python provides a rich set of [string methods][str-methods] that can assist with searching, cleaning, transforming, translating, and many other operations.

Being immutable, a `str` object's value in memory doesn't change; methods that appear to modify a string return a new copy or instance of `str`.

[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
