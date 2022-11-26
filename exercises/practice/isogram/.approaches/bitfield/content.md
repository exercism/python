# Bitfield to keep track of used letters

```python
A_LCASE = 97
Z_LCASE = 122
A_UCASE = 65
Z_UCASE = 90


def is_isogram(phrase):
    letter_flags = 0

    for ltr in phrase:
        letter = ord(ltr)
        if letter >= A_LCASE and letter <= Z_LCASE:
            if letter_flags & (1 << (letter - A_LCASE)) != 0:
                return False
            else:
                letter_flags |= 1 << (letter - A_LCASE)
        elif letter >= A_UCASE and letter <= Z_UCASE:
            if letter_flags & (1 << (letter - A_UCASE)) != 0:
                return False
            else:
                letter_flags |= 1 << (letter - A_UCASE)
    return True

```

This solution uses the [ASCII][ascii] value of the letter to set the corresponding bit position.

Some [constants][const] are defined for readability in the function.
Python doesn't _enforce_ having real constant values, but using all uppercase letters is the naming convention for a Python constant.
It indicates that the value is not intended to be changed.

- The ASCII value for `a` is `97`.
- The ASCII value for `z` is `122`.
- The ASCII value for `A` is `65`.
- The ASCII value for `Z` is `90`.


- A [`for`][for] loop is used to iterate the characters in the input phrase.
- The [`ord()`][ord] function is used to get the ASCII value of the letter.
- The `if` statements look for a character being `a` through `z` or `A` through `Z`.

- If the lowercase letter is subtracted by `97`, then `a` will result in `0`, because `97` minus `97` equals `0`.
  `z` would result in `25`, because `122` minus `97` equals `25`.
  So `a` would have `1` [shifted left][shift-left] 0 places (so not shifted at all) and `z` would have `1` shifted left 25 places.
- If the uppercase letter is subtracted by `A`, then `A` will result in `0`, because `65` minus `65` equals `0`.
  `Z` would result in `25`, because `90` minus `65` equals `25`.
  So `A` would have `1` [shifted left][shift-left] 0 places (so not shifted at all) and `Z` would have `1` shifted left 25 places.

In that way, both a lower-cased `z` and an upper-cased `Z` can share the same position in the bit field.

So, for a thirty-two bit integer, if the values for `a` and `Z` were both set, the bits would look like

```
      zyxwvutsrqponmlkjihgfedcba
00000010000000000000000000000001
```

We can use the [bitwise AND operator][and] to check if a bit has already been set.
If it has been set, we know the letter is duplicated and we can immediately return `False`.
If it has not been set, we can use the [bitwise OR operator][or] to set the bit.
If the loop completes without finding a duplicate letter (and returning `False`), the function returns `True`.

[ascii]: https://www.asciitable.com/
[const]: https://realpython.com/python-constants/
[for]: https://realpython.com/python-for-loop/#the-python-for-loop
[ord]: https://docs.python.org/3/library/functions.html?#ord
[shift-left]: https://realpython.com/python-bitwise-operators/#left-shift
[or]: https://realpython.com/python-bitwise-operators/#bitwise-or
[and]: https://realpython.com/python-bitwise-operators/#bitwise-and
