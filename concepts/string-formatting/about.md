# About

## String Formatting in Python

The [Zen of Python][zen-of-python] asserts there should be "one _obvious_ way to do something in Python".
But when it comes to string formatting, things are a little .... _less zen_.
It can be surprising to find out that there are **four** main ways to perform string formatting in Python - each for a different scenario.
Some of this is due to Python's long history and some of it is due to considerations like internationalization or input sanitation.
We will start with the most recent additions to the string formatting toolbox and work our way backward to "old style" or "printf() style" string formatting.


## literal string interpolation:  The `f-string`

 Introduced in [Python 3.6][pep-0498], [`f-strings`][f-string] (_short for "formatted-strings"_) or [literal string interpolation][string interpolation] are a way of quickly and efficiently evaluating and formatting expressions and strings to a `str` type using the `f` (or `F`) prefix before the brackets (_like so `f'{object}'`_).
 They can be used with all enclosing string types as: single quote `'`, double quote `"` and with multi-lines and escaping triple quotes `'''` or `"""`.
 Any variables, expressions, or other types placed inside the `{}` are first evaluated, then converted to a `str`, then concatenated with any `str` outside the curly braces.

In this example, we insert two variable values in the sentence: one `str` and one `float`:

```python
>>> name = 'eighth'
>>> value = 1/8
...
# The f-string, using the two values.
# The .2f format code truncates so the value displays as 0.12.
>>> print(f'An {name} is approximately {value:.2f}.')
'An eighth is approximately 0.12.' 
```

The expressions evaluated can be almost anything.
Some of the (wide range) of possibilities that can be evaluated: `str`, `numbers`, variables, arithmetic expressions, conditional expressions, built-in types, slices, functions, lambdas, comprehensions or **any** objects with either `__str__` or `__repr__` methods defined.

Some examples:

```python
# A dictionary of key:value pairs.
>>> waves = {'water': 1, 'light': 3, 'sound': 5}

# Using the name waves in an f-string.
>>> print(f'"A dict can be represented with f-string: {waves}."')
'"A dict can be represented with f-string: {\'water\': 1, \'light\': 3, \'sound\': 5}."'

# Here, we pull a value from the dictionary by using the key
>>> print(f'Tenfold the value of "light" is {waves["light"]*10}.')
'Tenfold the value of "light" is 30.'
```

Replacement fields (_the `{}` in the f-string_) support output control mechanisms such as width, alignment, precision.
 This is the same [format specification mini-language][format-mini-language] that is used by the `str.format()` method.

A more complex example of an `f-string` that includes output control:

```python
# Assigning variables
>>> precision = 3
>>> verb = "see"
>>> the_end = ['end', 'of', 'transmission']

# Reassigning verb to 'meet'.
>>> verb = 'meet'

# This example includes a function, str, a nested f-string, an arithmetic expression, 
# precision formatting, bracket escaping and object formatting.
>>> message = f'"Have a {"NICE".lower()} day, I will {verb} you after {f"{30e8*111_000:6.{precision}e}"} light-years."{{{the_end}}}'
...
>>> print(message)
'"Have a nice day, I will meet you after 3.330e+14 light-years."{[\'end\', \'of\', \'transmission\']}'

```

There are a few limitations to be aware of.
`f-string` expressions cannot be empty, they cannot contain comments, and for Python versions earlier than Python 3.7, they cannot contain `await` or `async for` clauses:

```python
>>> print(f"An empty expression will error: {}")
SyntaxError: f-string: empty expression not allowed

>>> word = 'word'
>>> print(f"""A comment in a triple quoted f-string will error: {
    word # I chose a nice variable
}""")
SyntaxError: f-string expression part cannot include '#'
```

~~~~exercism/caution
String interpolation cannot be used together with the [GNU gettext API][gnu-gettext-api] for internationalization (I18N) and localization (L10N), so it is recommended that the `string.Template(template)` class or the `str.format()` method outlined below be used instead of an `f-string` in any "string wrapping" translation scenarios.

Also keep in mind that using expressions inside the `f-string` brackets `{}` is similar to using `eval()` or `exec()`, so it isn't very safe and should be used sparingly.
~~~~


## The `str.format()` Method

The [`str.format()`][str-format] method replaces placeholders within the string with values fed as arguments to the function.
 The placeholders are identified with named (`{price}`), numbered (`{0}` or indexed) or even empty (_positional_) placeholders `{}`.
For example:

```python
# A named placeholder and a positional placeholder.
>>> print('My text: {placeholder_1} and {}.'.format(12, placeholder_1='named placeholder'))
...
'My text: named placeholder and 12.'
```

As with `f-strings`, Pythons  `str.format()` supports a whole range of [mini language format specifier][format-mini-language] that can be used to align text, convert, etc.

The complete formatting specifier pattern is `{[<name>][!<conversion>][:<format_specifier>]}`:

- `<name>` can be a named placeholder or a number or empty.
- `!<conversion>` is optional and should be one of this three conversions: `!s` for [`str()`][str-conversion], `!r` for [`repr()`][repr-conversion] or `!a` for [`ascii()`][ascii-conversion].
By default, `str()` is used.
- `:<format_specifier>` is optional and has a lot of options, which we are [listed here][format-specifiers].

Example of conversions for a diacritical letter:

```python
# Fills in the object at index zero, converted to a string.
>>> print('An e with an umlaut: {0!s}'.format('ë'))
An e with an umlaut: ë
...

# Fills in the object at index zero, converted to a repr.
>>> print('An e with an umlaut object representation: {0!r}'.format('ë'))
An e with an umlaut object representation: 'ë'

...

# Fills in the object at index zero, converted to ascii
>>> print('An e with an umlaut converted into ascii: {0!a}'.format('ë'))
An e with an umlaut converted into ascii: '\xeb'

...

# Fills in the object in the first position.
# Then fills in the object in the second position formatted as a repr
>>> print('She said her name is not {} but {!r}.'.format('Chloe', 'Zoë'))
"She said her name is not Chloe but 'Zoë'."
```

Example of using format specifiers:

```python
# Formats the object at index 0 as a decimal with zero places, 
# then as a right-aligned binary number in an 8 character wide field.
>>> print("The number {0:d} has a representation in binary: '{0: >8b}'.".format(42))
The number 42 has a representation in binary: '  101010'.
```

More examples are shown at the end of [this documentation][summary-string-format].


## `%` Formatting, or `printf()` Style Formatting

Use of the `%` operator for formatting is the oldest method of string formatting in Python.
It comes from the C language and allows the use of positional arguments to build a `str`.

This method has been superseded by both `f-strings` and `str.format()`, which is why the nickname for `%` formatting is _'Old Style'_.
It can be still found in python 2 and/or legacy code.
While using this method will work in Python 3.x, `%` formatting is usually avoided because it can be error-prone, is less efficient, has fewer options available, and any placeholder-argument mismatch can raise an exception.
 Using the `%` operator is similar to [`printf()`][printf-style-docs], so it is also sometimes called _printf formatting_.


```python
# Assigning a variable.
>> name = "Anna-conda"

# Building a string using %
>> print("The snake's name is %s." % name)
...
"The snake's name is Anna-conda."
```

In the example above, the `%` operator substitutes the placeholder `%s` with the variable `name` at runtime.
If you want to add multiple variables to a string, you need to supply a [tuple][tuples] containing one object per placeholder after the `%`:

```python
# Assigning variables
>>> name = "Billy the Kid"
>>> fruit = "grapes"

# Building a string using %
>>> print("Surprisingly, %ss favorite snack was %s." %(name, fruit))
Surprisingly, Billy the Kids favorite snack was grapes.
```


## Template Strings

[`string.Template()`][string.Template()] is a class from the `string` module (_as opposed to the built-in `str` type_), which is part of the Python standard library, but has to be imported for use.
Template strings support `$`-based substitution and are much simpler and less capable than the other options mentioned here, but can be very useful for when complicated internationalization is needed, or outside inputs need to be sanitized.


```python
>> from string import Template

>>> snake_name = "Anna-Conda"

# Creating a Template() with placeholder text
>> template_string = Template("The snake called `$snake_name` has escaped!")

# Calling .substitute() to replace the placeholder with a value.
>> template_string.substitute(snake_name=name)
'The snake called `Anna-Conda` has escaped!'
```

More information about `Template` string can be found in the Python [documentation][template-string].


## How Do You Choose which Formatting Method to Use?

With all these options and mini-languages, how do you decide what to reach for when formatting Python strings?
A few quick guidelines:

1. `f-strings` are the newest and easiest to read.
If you don't need to internationalize, they should be the Python 3.6+ preferred method.
2. `str.format()` is versatile, very powerful and compatible with both `gnu gettext` and most versions of Python.
3. If simplicity, safety, and/or heavy internationalization is what you need, `string.Template()` can be used to mitigate risks when inputs from users need to be handled, and for wrapping translation strings.
4. The `%` operator is not supported in some newer distributions of Python and should mostly be used for compatibility with old code.
`%` formatting` can lead to issues displaying non-ascii and unicode characters and has more errors and less functionality than other methods.

If you want to go further: [all about formatting][all-about-formatting] and [Python String Formatting Best Practices][formatting best practices] are good places to start.

[all-about-formatting]: https://realpython.com/python-formatted-output
[ascii-conversion]: https://www.w3resource.com/python/built-in-function/ascii.php
[f-string]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
[format-mini-language]: https://docs.python.org/3/library/string.html#format-specification-mini-language
[format-specifiers]: https://www.python.org/dev/peps/pep-3101/#standard-format-specifiers
[formatting best practices]: https://realpython.com/python-string-formatting/
[pep-0498]: https://peps.python.org/pep-0498
[printf-style-docs]: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
[repr-conversion]: https://www.w3resource.com/python/built-in-function/repr.php
[str-conversion]: https://www.w3resource.com/python/built-in-function/str.php
[str-format]: https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat
[string interpolation]: https://en.wikipedia.org/wiki/String_interpolation
[string.Template()]: https://docs.python.org/3/library/string.html#template-strings
[summary-string-format]: https://www.w3schools.com/python/ref_string_format.asp
[template-string]: https://docs.python.org/3/library/string.html#template-strings
[tuples]: https://www.w3schools.com/python/python_tuples.asp
[zen-of-python]: https://www.python.org/dev/peps/pep-0020/
