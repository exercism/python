## String Formatting in Python

The [Zen of Python][zen-of-python] asserts there should be "one _obvious_ way to do something in Python". But when it comes to string formatting, things are a little .... _less zen_. It can be surprising to find out that there are **four** main ways to perform string formatting in Python - each for a different scenario.

# literal string interpolation. f-string

Literal string interpolation or **f-string** is a way of quickly and efficiently formatting and evaluating expressions to `str` using the `f` (or `F`) prefix before the brackets, like so `f'{object}'`. It can be used with all enclosing string types as: single quote `'`, double quote `"` and with multi-lines and escaping triple quotes `'''` or `"""`.

In this example, we insert two variable values in the sentence: one `str` and one `float`:

```python
>>> name, value = 'eighth', 1/8
>>> f'An {name} is approximately {value:.2f}.'
'An eighth is approximately 0.12.' # .2f truncates so it displays 0.12.
```

The expressions evaluated can be almost anything, to mention some of the possibilities that can be evaluated: `str`, numbers, variables, arithmetic expressions, conditional expressions, built-in types, slices, functions or any objects with either `__str__` or `__repr__` methods defined. Some examples:

```python
>>> waves = {'water': 1, 'light': 3, 'sound': 5}

>>> f'"A dict can be represented with f-string: {waves}."'
'"A dict can be represented with f-string: {\'water\': 1, \'light\': 3, \'sound\': 5}."'

>>> f'Tenfold the value of "light" is {waves["light"]*10}.'
'Tenfold the value of "light" is 30.'
```

f-string supports control mechanisms such as width, alignment, precision that are described for the `.format()` method.

An advanced example of f-string:

```python
>>> precision, verb, the_end = 3, "see", ['end', 'of', 'transmission']
>>> verb = 'meet'
>>> f'"Have a {"NICE".lower()} day, I will {verb} you after {f"{30e8*111_000:6.{precision}e}"} light-years."{{{the_end}}}'
'"Have a nice day, I will meet you after 3.330e+14 light-years."{[\'end\', \'of\', \'transmission\']}'
# This example includes a function, str, nested f-string, arithmetic expression, precision, bracket escaping and object formatting.
```

There is a couple of limitations to be aware of: f-string expressions can't be empty and cannot contain comments:

```python
>>> f"An empty expression will error: {}"
SyntaxError: f-string: empty expression not allowed

>>> word = 'word'
>>> f"""A comment in a triple quoted f-string will error: {
    word # I chose a nice variable
}"""
SyntaxError: f-string expression part cannot include '#'
```

String interpolation cannot be used together with the GNU gettext API for internationalization (I18N) and localization (L10N), so `str.format()` needs to be used instead of an `f-string` in translation scenarios. Keep in mind that using an expression inside the brackets `{}` is similar to using `eval()` or `exec()`, so it isn't very safe and should be used sparingly.

# str.format() method

The [`str.format()`][str-format] allows to replace placeholders with values, the placeholders are identified with named indexes `{price}` or numbered indexes `{0}` or empty placeholders `{}`. The values are specified as parameters in the `format()` method.

Example:

```python
>>> 'My text: {placeholder1} and {}.'.format(12, placeholder1='value1')
'My text: value1 and 12.'
```

Python `.format()` supports a whole range of [mini language format specifier][format-mini-language] that can be used to align text, convert, etc.

The complete formatting specifier pattern is `{[<name>][!<conversion>][:<format_specifier>]}`:

- `<name>` can be a named placeholder or a number or empty.
- `!<conversion>` is optional and should be one of this three conversions: `!s` for [`str()`][str-conversion], `!r` for [`repr()`][repr-conversion] or `!a` for [`ascii()`][ascii-conversion]. By default, `str()` is used.
- `:<format_specifier>` is optional and has a lot of options, which we are [listed here][format-specifiers].

Example of conversions for a diacritical letter:

```python
>>> '{0!s}'.format('ë')
'ë'
>>> '{0!r}'.format('ë')
"'ë'"
>>> '{0!a}'.format('ë')
"'\\xeb'"

>>> 'She said her name is not {} but {!r}.'.format('Chloe', 'Zoë')
"She said her name is not Chloe but 'Zoë'."
```

Example of format specifiers:

```python
>>> "The number {0:d} has a representation in binary: '{0: >8b}'.".format(42)
"The number 42 has a representation in binary: '  101010'."
```

More examples at the end of [this documentation][summary-string-format]. `str.format()` should be used together with the [GNU gettext API][gnu-gettext-api] for internationalization (I18N) and localization (L10N) in translation scenarios.

## The `%` operator

The `%` operator comes from the C language and it allows to use positional arguments to build a `str`.

This method is now superseded by the `.format()` method, which is why the nickname of `%` is The _'Old Style'_. It can be still found is python 2 or legacy code. The `%` operator is usually avoided because less efficient, fewer options are available and any placeholder-argument mismatch can raise an exception. This operator is similar to [`printf()`][printf-style-docs].

```python
>> name = "Anna-conda"
>> "The snake's name is %s." % name
"The snake's name is Anna-conda."
```

The `%` operator substitutes at runtime the placeholder `%s` with the variable `name`. If you want to add multiple variables to a string you would need a [tuple][tuples] containing one object per placeholder after the `%`.

## Template strings

`Template` is a module from the `string` standard library, which is always shipped with Python. It is simpler but also less capable than the options mentioned before, but can be sometimes enough to build a nice `str`.

```python
>> from string import Template
>> template_string = Template("The snake called `$snake_name` has escaped!")
>> template_string.substitute(snake_name=name)
'The snake called `Anna-conda` has escaped'
```

More information about `Template` string can be found in the Python [documentation][template-string].

## How to choose which formatting method to use?

1. The `f-string` is the newest and easiest to read, it should be preferred when using Python 3.6+.
2. Then `.format()` is versatile, very powerful and compatible with most versions of Python.
3. `Template string` can be used to mitigate risks when inputs from users need to be handled, for simplicity or multiple substitutions.
4. The `%` operator is not supported in some of the new distributions of Python, it is mostly used for compatibility with old code. This operator can lead to issues displaying non-ascii characters and has less functionalities than other methods.

If you want to go further: [all about formatting][all-about-formatting].

[zen-of-python]: https://www.python.org/dev/peps/pep-0020/
[f-string]: https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36
[str-format]: https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat
[format-mini-language]: https://docs.python.org/3/library/string.html#format-specification-mini-language
[str-conversion]: https://www.w3resource.com/python/built-in-function/str.php
[repr-conversion]: https://www.w3resource.com/python/built-in-function/repr.php
[ascii-conversion]: https://www.w3resource.com/python/built-in-function/ascii.php
[format-specifiers]: https://www.python.org/dev/peps/pep-3101/#standard-format-specifiers
[summary-string-format]: https://www.w3schools.com/python/ref_string_format.asp
[printf-style-docs]: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
[tuples]: https://www.w3schools.com/python/python_tuples.asp
[template-string]: https://docs.python.org/3/library/string.html#template-strings
[all-about-formatting]: https://realpython.com/python-formatted-output
[gnu-gettext-api]: https://docs.python.org/3/library/gettext.html
