Python strings can be powerful. At their core, a string is an iterable of Unicode code points. There is no separate "character" type in Python. For a deep dive on what information a string is encoding (or, "how does the computer know how to translate zeroes and ones into letters?"), [this blog post is enduringly helpful][joel-on-text].

As a Python data type, strings can be manipulated by various methods, split into letters, used to join a list of strings into one string, amongst other things. The simplest way to create a string is by literally delimiting with `"` or `'` (e.g. `mystring = "astring"`); however, strings can also be written across multiple lines by using triple quotes (`"""`), or written to be used as a format string, like this: `f"{variable_will_be_interpolated_here}"`.

New strings can be created by concatenating other strings, using the `+` operator, or by using `.join()`. The `.format()` method or the format string syntax shown above are the most common way to interpolate strings. All of these methods return a new instance of a string, since a string itself is immutable.

### More about Python logging

Python has a useful [built-in logging library][logging-library], aptly named `logging`. It handles cases similar
to the ones you just finished working on, and many more. It's very often used in projects, and is worthwhile to know.

[joel-on-text]: https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
[logging-library]: https://docs.python.org/3.8/library/logging.html
