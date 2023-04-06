# Bit field

```python
A_LCASE = 97
A_UCASE = 65
ALL_26_BITS_SET = 67108863


def is_pangram(sentence):
    letter_flags = 0
    for letter in sentence:
        if 'a' <= letter <= 'z':
            letter_flags |= 1 << ord(letter) - A_LCASE
        elif 'A' <= letter <= 'Z':
            letter_flags |= 1 << ord(letter) - A_UCASE
    return letter_flags == ALL_26_BITS_SET

```

This solution uses the [ASCII][ascii] value of the letter to set the corresponding bit position.
First, some [constant][const] values are set.

```exercism/note
Python doesn't _enforce_ having real constant values,
but using all uppercase letters is the naming convention for a Python constant.
It indicates that the value is not intended to be changed.
```

These values will be used for readability in the body of the `is_pangram` function.
The ASCII value for `a` is `97`.
The ASCII value for `A` is `65`.
The value for all of the rightmost `26` bits being set is `67108863`.

- The [`for` loop][for-loop] loops through the characters of the `sentence`.
- Each letter is tested for being `a` through `z` or `A` through `Z`.
- If the lowercased letter is subtracted by `a`, then `a` will result in `0`, because `97` minus `97`  equals `0`.
`z` would result in `25`, because `122` minus `97` equals `25`.
So `a` would have `1` [shifted left][shift-left] 0 places (so not shifted at all) and `z` would have `1` shifted left 25 places.
- If the uppercased letter is subtracted by `A`, then `A` will result in `0`, because `65` minus `65`  equals `0`.
`Z` would result in `25`, because `90` minus `65` equals `25`.
So `A` would have `1` [shifted left][shift-left] 0 places (so not shifted at all) and `Z` would have `1` shifted left 25 places.

In that way, both a lower-cased `z` and an upper-cased `Z` can share the same position in the bit field.

So, for a thirty-two bit integer, if the values for `a` and `Z` were both set, the bits would look like

```
      zyxwvutsrqponmlkjihgfedcba
00000010000000000000000000000001
```

We can use the [bitwise OR operator][or] to set the bit.
After the loop completes, the function returns `True` if the `letter_flags` value is the same value as when all of the rightmost  `26` bits are set,
which is `67108863`.

Although this approach is usually very fast in some other languages, it is comparatively slow in Python.

[ascii]: https://www.asciitable.com/
[const]: https://realpython.com/python-constants/
[for-loop]: https://wiki.python.org/moin/ForLoop
[shift-left]: https://realpython.com/python-bitwise-operators/#left-shift
[or]: https://realpython.com/python-bitwise-operators/#bitwise-or
