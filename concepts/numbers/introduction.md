# Introduction

Python has three different types of built-in numbers: integers ([`int`][int]), floating-point ([`float`][float]), and complex ([`complex`][complex]).
Fractions ([`fractions.Fraction`][fractions]) and Decimals ([`decimal.Decimal`][decimals]) are also available via import from the standard library.

Whole numbers including hexadecimal ([_`hex()`_][hex]), octal ([_`oct()`_][oct]) and binary ([_`bin()`_][bin]) numbers **without** decimal places are also identified as `ints`.

Python fully supports arithmetic between these different number types, and will convert narrower numbers to match their less narrow counterparts when used with the binary arithmetic operators (`+`, `-`, `*`, `/`, `//`, and `%`).


[bin]: https://docs.python.org/3/library/functions.html#bin
[complex]: https://docs.python.org/3/library/functions.html#complex
[decimals]: https://docs.python.org/3/library/decimal.html#module-decimal
[float]: https://docs.python.org/3/library/functions.html#float
[fractions]: https://docs.python.org/3/library/fractions.html
[hex]: https://docs.python.org/3/library/functions.html#hex
[int]: https://docs.python.org/3/library/functions.html#int
[oct]: https://docs.python.org/3/library/functions.html#oct
