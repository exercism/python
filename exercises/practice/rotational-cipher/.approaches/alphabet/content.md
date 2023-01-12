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

The approach starts with defining the a constant which holds the whole alphabets lowercase letters.
After that the function `rotate` is declared, then a variable `result` is defined with the value of an empty string.

Then is all the letters from the text argument iterated over through a [`for loop`][for-loop].
Then is checked if the letter is a letter, if it is a letter then is checked if it is a uppercased letter.

If it is a uppercased letter then it is converted to lowe case and finds its index in the `AlPHABET` constant.
Then is the key added to the index and [modulo (`%`)][modulo] 26 is used on the result.
Then is the letter at the index found in the `AlPHABET` constant and the letter is converted to upcase.

If the letter is a lowercased letter then it does the same process but don't convert the letter to downcase and then to uppercase.

If the letter is not a letter then is the letter added to the result.
When the loop is finished we return the result.

If you only want to use english letters so could you import the alphabet instead of defining it yourself.
Since in the [`string`][string] module there is a constant called [`ascii_lowercase`][ascii_lowercase] which holds the lowercased alphabet.

```python
import string

AlPHABET = string.ascii_lowercase
```

[ascii_lowercase]: https://docs.python.org/3/library/string.html#string.ascii_letters
[for-loop]: https://realpython.com/python-for-loop/
[modulo]: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
[string]: https://docs.python.org/3/library/string.html
