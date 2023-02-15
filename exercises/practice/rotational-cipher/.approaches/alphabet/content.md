# Alphabet

```python
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

The approach starts with defining the constant `ALPHABET` which is a string of all lowercase letters.
The function `rotate()` is then declared, and a variable `result` is defined as an empty string.

The text argument is then iterated over via a [`for loop`][for-loop].
Each element is checked to make sure it is a letter, and subsequently checked if it is uppercase or lowercase.
Uppercase letters are converted to lowercase.
Then the index of each letter is found in the `AlPHABET` constant.
The numeric key value is added to the letter index and [modulo (`%`)][modulo] 26 is used on the result.
Finally, the new number is used as an index into the `AlPHABET` constant, and the resulting letter is converted back to uppercase.

Lowercase letters follow the same process without the conversion steps.

If the element is not a letter (for example, space or punctuation) then it is added directly to the result string.
The result string is returned once the loop finishes.

If only English letters are needed, the constant [`string.ascii_lowercase`][ascii_lowercase] can be imported from the [`string`][string] module.

```python
from string import ascii_lowercase

AlPHABET = ascii_lowercase
```

[ascii_lowercase]: https://docs.python.org/3/library/string.html#string.ascii_letters
[for-loop]: https://realpython.com/python-for-loop/
[modulo]: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
[string]: https://docs.python.org/3/library/string.html
