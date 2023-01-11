# Introduction

There are various ways to solve `palindrome-products`.
This approaches document shows 2 _common_ strategies, with one being a lot more efficient than the other.
That being said, neither approach here is considered canonical, and other "pythonic" approaches could be added/expanded on in the future.

## General guidance

The goal of this exercise is to generate the largest and smallest palindromes from a given range of numbers.

## Approach: Using ascii values

This approach is very simple and easy to understand.
it uses the ascii value of the letters to rotate them.
There the numbers 65-91 in the ascii range represent downcased letters.
While 97-123 represent upcased letters.

The reason why you might not want to do this approach is that it only supports the english alphabet.
Say we want to use the scandivanian letter: **ä**, then this approach will not work.
Since **ä** has the ascii value of 132.

```python
def rotate(text, key)
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

## Approach: Alphabet

This approach is similar to the previous one, but instead of using the ascii values, it uses the index of the letter in the alphabet.
It requires the storing of a string and unless you are using two strings you have to convert the letters from upper to lower case.

What this approach although give is the posiblity to use any alphabet.
Say we want to use the scandivanian letter: **ä**, then we just add it where we want it:
`abcdefghijklmnopqrstuvwxyzä` and it will rotate correctley around that.

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

For more information, check the [Nested for loop approach][approach-nested-for-loop].

## Approach: Str translate

This approach is similar to the previous one, but instead of using the index of the letter in the alphabet, it uses the `str.translate` method.
The benefit of this approach is that it has no visable loop, thereby the code becomes more concise.
What to note is that the `str.translate` still loops over the `string` thereby even if it is no visable loop, it doesn't mean that a method is not looping.

```python
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    translator = AlPHABET[key:] + AlPHABET[:key]
    return text.translate(str.maketrans(AlPHABET + AlPHABET.upper(), translator + translator.upper()))
```

You can read more about how to achieve this optimization in: [Nested for loop optimized][approach-nested-for-loop-optimized].

## Approach: Recursion

In this approach we use a recursive function.
A recursive function is a function that calls itself.
This approach can be more concise than other approaches, and may also be more readable for some audiences.

The reason why you might not want to use this approach is that Python has a [recursion limit][recursion-limit] with a default of 1000.

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

## Benchmark

For more information, check the [Performance article][article-performance].

[approach-nested-for-loop]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop
[approach-nested-for-loop-optimized]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop-optimized
[article-performance]: https://exercism.org/tracks/python/exercises/palindrome-products/articles/performance
