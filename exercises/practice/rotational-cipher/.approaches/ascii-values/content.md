# Ascii

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

This approach uses [ascii values][ascii].
ASCII stands for **A**merican **S**tandard **C**ode for **I**nformation **I**nterchange.
It is a 7-bit character encoding standard for electronic communication first described in 1969, becoming a formal standard in 2015.
It uses numbers to represent 128 different entities including carriage returns, whitespace characters, box characters, alphabetic characters, punctuation, and the numbers 0-9.

In ascii, all the lowercase English letters appear between 97 and 123.
While the uppercase letters are in the range between 65 and 91.

~~~~exercism/caution

This approach only supports the English alphabet.
Non-English alphabets are not contiguous in their ascii number ranges, and are not consistently defined across platforms.
For example, the Scandinavian letter **å** has the extended ascii value of **134**, but is used in combination with Latin-1  characters that appear in the 65-91 and 97-123 ranges.
This means that a shift for an extended ascii word containing **å** won't result in an accurate alphabet position for a Scandinavian language.

~~~~

The approach starts with defining the function `rotate()`, with a variable `result` is assigned to an empty string.
The elements of the text argument are then iterated over using a [`for loop`][for-loop].
Each element is checked to see if it is a letter, and if it is a lower or uppercase letter.

Python has a builtin function called `ord` that converts a [unicode][unicode] symbol to an integer representation.
Unicode's first 128 code points have the same numbers as their ascii counterparts.

If the element is an uppercase letter, [`ord`][ord] is used to convert the letter to an integer.
The integer is added to the numeric key and then 65 is subtracted from the total.
Finally, the result is [modulo (%)][modulo] 26 to put the value within the 0-26 range, and 65 is added back.

This is because we want to know which letter of the alphabet the number will become.
If the new number is over 26 we want to make sure that it "wraps around" to remain in the range of 0-26.
To properly use modulo for a range we have to make sure that it starts at zero, so we subtract 65.
To get back to a letter in the ascii range we add 65 and use the [`chr`][chr] method to convert the value to a letter.

The process is the same for a lowercase letter, but with 97 subtracted/added to put the letter in the lowercase ascii range of 97 - 123.

Any element that is not a letter (_whitespace or punctuation_) is added directly to the result string.
When all the elements have been looped over, the full result is returned.

[ascii]: https://en.wikipedia.org/wiki/ASCII
[chr]: https://docs.python.org/3/library/functions.html#chr
[for-loop]: https://realpython.com/python-for-loop/
[modulo]: https://realpython.com/python-modulo-operator/
[ord]: https://docs.python.org/3/library/functions.html#ord
[unicode]: https://en.wikipedia.org/wiki/Unicode
