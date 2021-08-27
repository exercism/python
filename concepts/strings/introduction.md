# Introduction

A `str` in Python is an [immutable sequence][text sequence] of [Unicode code points][unicode code points].
These could include letters, diacritical marks, positioning characters, numbers, currency symbols, emoji, punctuation, space and line break characters, and more.

Strings implement all [common sequence operations][common sequence operations], and can be iterated through using `for item in <string>` or `for index, item in enumerate(<string>)` syntax.

Strings can be concatenated with `+`, or via `<str>.join()`, split via `<str>.split(<separator>)`, and offer multiple types of formatting, interpolation, and templating.

Being immutable, a `str` object's value in memory doesn't change; methods that appear to modify a string return a new copy or instance of `str`.

For a deep dive on what information a string encodes (or, _"how does a computer know how to translate zeroes and ones into letters?"_), [this blog post is enduringly helpful][joel-on-text].
The Python docs also provide a very detailed [unicode HOWTO][unicode how-to] that discusses Pythons support for the Unicode specification in the `str`, `bytes` and `re` modules, considerations for locales, and some common issues with encoding and translation.


[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[joel-on-text]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
[text sequence]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[unicode code points]: https://stackoverflow.com/questions/27331819/whats-the-difference-between-a-character-a-code-point-a-glyph-and-a-grapheme
[unicode how-to]: https://docs.python.org/3/howto/unicode.html
