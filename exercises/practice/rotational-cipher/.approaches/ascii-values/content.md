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

This approach uses [ascii values][ascii], ascii stands for American Standard Code for Information Interchange.
It is a character encoding standard for electronic communication.
It is a 7-bit code, which means that it can represent 128 different characters.
The system uses numbers to represent various characters, symbols, and other entities.

In ascii can you find all the downcased letter in the range between 97 and 123.
While the upcased letters are in the range between 65 and 91.

The reason why you might not want to do this approach is that it only supports the english alphabet.

The approach starts with defining the function `rotate`, then a variable `result` is defined with the value of an empty string.
Then is all the letters from the text argument iterated over through a [`for loop`][for-loop].
Then is checked if the letter is a letter, if it is a letter then is checked if it is a uppercased letter.

Python has a built in function called `ord` that converts a [unicode][unicode] symbol to an integer.
The unicode's first 128 characters are the same as ascii.

If it is a uppercased letter then is [`ord`][ord] used to convert the letters to an integer and is then added with the key and then subtracted with 65.
Then is the result of that [modulo (`%`)][modulo] 26 added with 65.

That is because we want to know which index in the alphabet the letter is.
And if the number is over 26 we want to make sure that it is in the range of 0-26.
So we use modulo to make sure it is in that range.
To use modulo for a range we have to make sure that it starts at zero, thereby are we subtracting the integer value of the letter with 65.
After that to get the back to a letter we add 65 and use the [`chr`][chr] method which converts an an unicode value to a letter.
After that is the new letter added to the result.

If the letter is a lowercased letter then is the same done but with the ascii value of 97 subtracted with the letter.

If the letter is not a letter then is the letter added to the result.
When the loop is finished we return the result.

[ascii]: https://en.wikipedia.org/wiki/ASCII
[chr]: https://docs.python.org/3/library/functions.html#chr
[for-loop]: https://realpython.com/python-for-loop/
[modulo]: https://realpython.com/python-modulo-operator/
[ord]: https://docs.python.org/3/library/functions.html#ord
[unicode]: https://en.wikipedia.org/wiki/Unicode
