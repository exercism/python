# Dictionary

```python
LETTER_SCORES = {
    'A': 1,
    'E': 1,
    'I': 1,
    'O': 1,
    'U': 1,
    'L': 1,
    'N': 1,
    'R': 1,
    'S': 1,
    'T': 1,
    'D': 2,
    'G': 2,
    'B': 3,
    'C': 3,
    'M': 3,
    'P': 3,
    'F': 4,
    'H': 4,
    'V': 4,
    'W': 4,
    'Y': 4,
    'K': 5,
    'J': 8,
    'X': 8,
    'Q': 10,
    'Z': 10
}

def score(word):
    return sum(LETTER_SCORES[letter.upper()] for letter in word)
```

The code starts with initializing a constant that is a [dictionary][dictionary] there each letter is a key and their respective score as a value.
Then a function is defined that takes a word as an argument.

The function returns the built in function [`sum`][sum] that takes a [generator expression][generator-expersion] that iterates over the letters in the word.
What a generator expression does is that it generates the values on the fly.
Meaning that it doesn't have to use a lot of memory since it uses the last value and generates the next value.

Under the generation a letter is given from the string, then it is converted to upcase, and then being looked up at inside of the dictionary and the value is returned.

There is also a very similar approach that uses a dictionary transposition.
Although that approach requires more computational calculation therefore is this approach more efficient.

[dictionary]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[generator-expersion]: https://peps.python.org/pep-0289/
[sum]: https://docs.python.org/3/library/functions.html#sum
