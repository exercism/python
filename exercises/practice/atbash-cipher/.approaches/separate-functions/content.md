## Approach: Separate Functions
We use `str.maketrans` to create the encoding. 
`.maketrans`/`.translate` is extremely fast compared to other methods of translation.

In `encode`, we use a [generator expression][generator expression] in `str.join`, which is more efficient - and neater - than a list comprehension.
```python
from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(text: str):
    res = "".join(c for c in text.lower() if c.isalnum()).translate(ENCODING)
    return " ".join(res[i:i+5] for i in range(0, len(res), 5))
def decode(text: str):
    return "".join(c.lower() for c in text if not c.isspace()).translate(ENCODING)
```
In `encode`, we first join together every character if the character is alphanumeric - as we use `text.lower()`, the characters are all lowercase as needed.
Then, we translate it and return a version joining every five characters with a space in between.

`decode` does the exact same thing, except it doesn't return a chunked output. 
Instead of cleaning the input by checking that it's alphanumeric, we check that it's not a whitespace character.

It might be cleaner to use helper functions:
```python
from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
def _clean(text):
    return "".join([c.lower() for c in text if c.isalnum()])
def _chunk(text):
    return " ".join(text[i:i+5] for i in range(0, len(text), 5))

def encode(text):
    return _chunk(_clean(text).translate(ENCODING))
def decode(text):
    return _clean(text).translate(ENCODING)
```
Note that checking that `c` _is_ alphanumeric achieves the same result as checking that it's _not_ whitespace, although it's not as explicit.
As this is a helper function, this is acceptable enough.

You can also make `_chunk` recursive:
```python
def _chunk(text):
    if len(text) <= 5:
        return text
    return text[:5] + " " + _chunk(text[5:])
```

[generator expression]: https://www.programiz.com/python-programming/generator