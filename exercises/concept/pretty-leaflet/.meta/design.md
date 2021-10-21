# Design

## Goal

This concept exercise should convey a basic understanding of the various `string formatting` methods in python.

## Learning objectives

- Different types of string formatting, [when each type should be used][formatting-types] and [deferring i18n use cases for f-strings][pep501-i18n].
- "New Style" formatting with [`str.format()`][str.format]
- String interpolation, or ["f-strings"][f-strings]
- Format specification ["mini-language"][mini-language] e.g. formatting an int variable as a hexadecimal string, truncating long strings, etc.

## Out of scope

- Translation -- internationalization and localization of strings and string formats
- `str.maketrans` and [`str.translate`][str.translate]
- `gettext`

## Concepts

- new style string formatting with `str.format()`
- string interpolation via f-strings

## Prerequisites

- `basics`
- `strings`
- `loops`
- `lists`

## Representer

No changes are required.

## Analyzer

Check if the student is only using `f-strings` or `.format()` because we do not want the student to use the `%` operand and the `Template` strings.

[formatting-types]: https://realpython.com/python-string-formatting/#which-string-formatting-method-should-you-use
[pep501-i18n]: https://www.python.org/dev/peps/pep-0501/#deferring-consideration-of-possible-use-in-i18n-use-cases
[str.format]: https://docs.python.org/3/library/string.html#format-string-syntax
[f-strings]: https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
[mini-language]: https://docs.python.org/3/library/string.html#format-specification-mini-language
[str.translate]: https://docs.python.org/3/library/stdtypes.html#str.translate
