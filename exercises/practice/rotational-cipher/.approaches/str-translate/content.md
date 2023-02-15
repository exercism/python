# Str Translate

```python
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    translator = AlPHABET[key:] + AlPHABET[:key]
    return text.translate(str.maketrans(AlPHABET + AlPHABET.upper(), translator + translator.upper()))
```

This approach uses the [`<str>.translate`][translate] method.
`translate` takes a translation table as an argument.
To create a translation table we use [`str.makestrans`][maketrans].

This approach starts with defining a constant of all the lowercase letters in the alphabet.
Then the function `rotate()` is declared.
A `translator` variable defined with the value of the `AlPHABET` constant [sliced][slicing] from the key to the end and then sliced from the start to the key.

This is done so we have 2 strings which are the same but shifted by the key value.
Say we have the `AlPHABET` constant with the value of `abcdefghijklmnopqrstuvwxyz` and the key is 3.
Then the `translator` variable will have the value of `defghijklmnopqrstuvwxyzabc`.

`str.translate` is then called on the `text` argument.
`str.translate` takes a translation table mapping start values to transformed values as an argument.
To create a translation table, `str.makestrans` is used.
`makestrans` takes 2 arguments: the first is the string to be translated, and the second is the string the first argument should be translated to.

For our solution, the first argument is the `AlPHABET` constant + the `AlPHABET` constant in uppercase.
The second argument is the `translator` variable + uppercase `translator` variable.

`str.makestrans` takes the [Unicode][unicode] values of the first argument and maps them to the corresponding Unicode values in the second argument, creating a `dict`.

```python
>>> str.maketrans("abc", "def")
{97: 100, 98: 101, 99: 102}
```

`str.translate` takes the `dict` created by `str.makestrans` and uses it to translate the characters in the `text` argument.

```python
>>> "abc".translate({97: 100, 98: 101, 99: 102})
'def'
```

Once the `str.translate` loop completes, we return the `result`.

[maketrans]: https://docs.python.org/3/library/stdtypes.html#str.maketrans
[slicing]: https://www.w3schools.com/python/python_strings_slicing.asp
[translate]: https://docs.python.org/3/library/stdtypes.html#str.translate
[unicode]: https://en.wikipedia.org/wiki/Unicode
