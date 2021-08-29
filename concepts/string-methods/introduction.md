# Introduction

A `str` in Python is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
These may include letters, diacritical marks, positioning characters, numbers, currency symbols, emoji, punctuation, various spaces, line breaks, and more.

Strings implement all [common sequence operations][common sequence operations] and can be iterated through using `for item in <str>` or `for index, item in enumerate(<str>)` syntax.
They can be concatenated with `+`, or via `<str>.join(<iterable>)`, split via `<str>.split(<separator>)`, and offer multiple formatting and assembly options.

To further work with strings, Python provides a rich set of [string methods][str-methods] that can assist with searching, cleaning, transforming, translating, and many other operations.
Being _immutable_, a `str` object's value in memory doesn't change; methods that appear to modify a string return a new copy or instance of that `str` object.

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
