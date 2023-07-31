## Approach: Separate Functions
We use `str.maketrans` to create the encoding. 
`.maketrans`/`.translate` is extremely fast compared to other methods of translation.
If you're interested, [read more][str-maketrans] about it.

In `encode`, we use a [generator expression][generator-expression] in `str.join`, which is more efficient - and neater - than a list comprehension.
```python
from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(text: str):
    res = "".join(chr for chr in text.lower() if chr.isalnum()).translate(ENCODING)
    return " ".join(res[index:index+5] for index in range(0, len(res), 5))

def decode(text: str):
    return "".join(chr.lower() for chr in text if chr.isalnum()).translate(ENCODING)
```
In `encode`, we first join together every character if the character is alphanumeric - as we use `text.lower()`, the characters are all lowercase as needed.
Then, we translate it and return a version joining every five characters with a space in between.

`decode` does the exact same thing, except it doesn't return a chunked output. 
Instead of cleaning the input by checking that it's alphanumeric, we check that it's not a whitespace character.

It might be cleaner to use helper functions:
```python
from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
def clean(text):
    return "".join([chr.lower() for chr in text if chr.isalnum()])
def chunk(text):
    return " ".join(text[index:index+5] for index in range(0, len(text), 5))

def encode(text):
    return chunk(clean(text).translate(ENCODING))

def decode(text):
    return clean(text).translate(ENCODING)
```
Note that checking that `chr` _is_ alphanumeric achieves the same result as checking that it's _not_ whitespace, although it's not as explicit.
As this is a helper function, this is acceptable enough.

You can also make `chunk` recursive:
```python
def chunk(text):
    if len(text) <= 5:
        return text
    return text[:5] + " " + chunk(text[5:])
```

[generator-expression]: https://www.programiz.com/python-programming/generator
[str-maketrans]: https://www.programiz.com/python-programming/methods/string/maketrans