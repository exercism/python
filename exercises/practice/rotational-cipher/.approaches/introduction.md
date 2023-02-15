# Introduction

There are various ways to solve `Rotational Cipher`.
For example, you can use [ascii values][ascii], an alphabet `str`/`list`, recursion, or `str.translate`.

## General guidance

The goal of this exercise is to shift the letters in a string by a given integer key between 0 and 26.
The letter in the encrypted string is shifted for as many values (or "positions") as the value of the key.


## Approach: Using ascii values

This approach is straightforward to understand.
It uses the ascii value of the letters to rotate them within the message.
The numbers 65-91 in the ascii range represent lowercase Latin letters, while 97-123 represent uppercase Latin letters.

~~~~exercism/caution

This approach only supports the English alphabet.
Non-English alphabets are not contiguous in their ascii number ranges, and are not consistently defined across platforms.
For example, the Scandinavian letter **å** has the extended ascii value of **134**, but is used in combination with Latin-1  characters that appear in the 65-91 and 97-123 ranges.
This means that a shift for an extended ascii word containing **å** won't result in an accurate alphabet position for a Scandinavian language.

~~~~


```python
def rotate(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(letter) - 97 + key) % 26 + 97)
        else:
            result += letter
    return result
```

For more information, check out the [ascii values approach][approach-ascii-values].

## Approach: Alphabet

This approach is similar to the ascii one, but it uses the index number of each letter in a defined alphabet string.
It requires making a string for all the letters in an alphabet.
And unless two strings are used, you will have to convert individual letters from lower to upper case (or vice-versa).

The big advantage of this approach is the ability to use _any_ alphabet (_although there are some issues with combining characters in Unicode._).
Here, if we want to use the Scandinavian letter: **å**, we can simply insert it into our string where we want it:
`abcdefghijklmnopqrstuvwxyzå` and the key rotation will work correctly.


```python
# This only uses English characters
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += AlPHABET[(AlPHABET.index(letter.lower()) + key) % 26].upper()
            else:
                result += AlPHABET[(AlPHABET.index(letter) + key) % 26]
        else:
            result += letter
    return result
```

For more information, see the [Alphabet approach][approach-alphabet].

## Approach: Str translate

This approach uses the [`str.translate`][str-translate] method to create a mapping from input to shifted string instead of using the index of an alphabet string to calculate the shift.
The benefit of this approach is that it has no visible loop, making the code more concise.

~~~~exercism/note
`str.translate` **still loops over the `string`**  even if it is not visibly doing so.
~~~~


```python
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    translator = AlPHABET[key:] + AlPHABET[:key]
    return text.translate(str.maketrans(AlPHABET + AlPHABET.upper(), translator + translator.upper()))
```

For more information, check out the [Str translate approach][approach-str-translate].


## Approach: Recursion

This approach uses a recursive function.
A recursive function is a function that calls itself.
This approach can be more concise than other approaches, and may also be more readable for some audiences.

~~~~exercism/caution
Python does not have any tail-call optimization and has a default [recursion limit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit) of 1000 calls on the stack.
Calculate your base case carefully to avoid errors.

~~~~


```python
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    if text == "":
        return ""
    first_letter, rest = text[0], text[1:]
    if first_letter.isalpha():
        if first_letter.isupper():
            return AlPHABET[(AlPHABET.index(first_letter.lower()) + key) % 26].upper() + rotate(rest, key)
        else:
            return AlPHABET[(AlPHABET.index(first_letter) + key) % 26] + rotate(rest, key)
    else:
        return first_letter + rotate(rest, key)
```

For more information, read the [Recursion approach][approach-recursion].

## Benchmark

For more information on the speed of these various approaches, check out the Rotational Cipher [Performance article][article-performance].


[ascii]: https://en.wikipedia.org/wiki/ASCII
[approach-recursion]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/recursion
[approach-str-translate]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/str-translate
[approach-ascii-values]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/ascii-values
[approach-alphabet]: https://exercism.org/tracks/python/exercises/rotational-cipher/approaches/alphabet
[article-performance]: https://exercism.org/tracks/python/exercises/rotational-cipher/articles/performance
[str-translate]: https://docs.python.org/3/library/stdtypes.html?highlight=str%20translate#str.translate
