# Introduction

Down at the hardware level, transistors can only be on or off: two states that we traditionally represent with `1` and `0`.
These are the [`binary digits`][binary-digits], abbreviated as [`bits`][bits].
Awareness of `bits` and `binary` is particularly important for systems programmers working in low-level languages.

However, for most of the history of computing the programming priority has been to find increasingly sophisticated ways to _abstract away_ this binary reality.


In Python (and many other [high-level programming languages][high-level-language]), we work with `int`, `float`, `string` and other defined _types_, up to and including audio and video formats.
We let the Python internals take care of (eventually) translating everything to bits.


Nevertheless, using [bitwise-operators][python-bitwise-operators] and [bitwise operations][python-bitwise-operations] can sometimes have significant advantages in speed and memory efficiency, even in a high-level language like Python.

[high-level-language]: https://en.wikipedia.org/wiki/High-level_programming_language
[binary-digits]: https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:digital-information/xcae6f4a7ff015e7d:binary-numbers/v/the-binary-number-system
[bits]: https://en.wikipedia.org/wiki/Bit
[python-bitwise-operations]: https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
[python-bitwise-operators]: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
