# Str Translate

```python
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    translator = AlPHABET[key:] + AlPHABET[:key]
    return text.translate(str.maketrans(AlPHABET + AlPHABET.upper(), translator + translator.upper()))
```

This approach uses the [`<str>.translate`][translate] method to solve the problem.
`translate` takes a translation table as an argument.
To create a translation table we use [str.`makestrans`][maketrans].

The approach starts with defining the a constant which holds the whole alphabets lowercase letters.
Then the function `rotate` is declared.
Then is the `translator` variable defined with the value of the `AlPHABET` constant [sliced][slicing] from the key to the end and then the `AlPHABET` constant sliced from the start to the key.

This is done so we have 2 strings which are the same but shifted by the key.
Say we have the `AlPHABET` constant with the value of `abcdefghijklmnopqrstuvwxyz` and the key is 3.
Then the `translator` variable will have the value of `defghijklmnopqrstuvwxyzabc`.

Then is the `translate` method called on the `text` argument.
The `translate` method takes a translation table as an argument.
To create a translation table we use str.`makestrans`maketrans.

The `makestrans` method takes 2 arguments.
The first argument is the string which holds the characters which should be translated.
The second argument is the string which holds the characters which the characters from the first argument should be translated to.

The first argument is the `AlPHABET` constant and the `AlPHABET` constant uppercased.
The second argument is the `translator` variable and the `translator` variable uppercased.

What the `makestrans` does is that it takes the first argument and maps it to the second argument.
It does that by creating a [dictionary], and converting the letter to [unicode][unicode].

```python
>>> str.maketrans("abc", "def")
{97: 100, 98: 101, 99: 102}
```

The `translate` method takes the dictionary created by the `makestrans` method and uses it to translate the characters in the `text` argument.

```python
>>> "abc".translate({97: 100, 98: 101, 99: 102})
'def'
```

When the loop is finished we return the result.

[maketrans]: https://docs.python.org/3/library/stdtypes.html#str.maketrans
[slicing]: https://www.w3schools.com/python/python_strings_slicing.asp
[translate]: https://docs.python.org/3/library/stdtypes.html#str.translate
[unicode]: https://en.wikipedia.org/wiki/Unicode
