# Introduction
Atbash cipher in Python can be solved in many ways.  

## General guidance
The first thing is to have a "key" mapping - possibly in a `dict` or `str.maketrans`, otherwise the value would have to be calculated on the fly.
Then, you have to "clean" up the string to be encoded by removing numbers/whitespace.
Finally, you break it up into chunks of five before returning it.

For decoding, it's similar - clean up (which automatically joins the chunks) and translate using the _same_ key - the realization that the same key can be used is crucial in solving this in an idiomatic manner.

## Approach: separate functions
We use `str.maketrans` to create the encoding. 
In `encode`, we use a [generator expression][generator expression] in `str.join`.
```python
from string import ascii_lowercase
ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

def encode(text: str):
    res = "".join(c for c in text.lower() if c.isalnum()).translate(ENCODING)
    return " ".join(res[i:i+5] for i in range(0, len(res), 5))
def decode(text: str):
    return "".join(c.lower() for c in text if c.isalnum()).translate(ENCODING)
```
Read more on this [approach here][approach-seperate-functions].

## Approach: mono-function
Notice that there the majority of the code is repetitive? 
A fun way to solve this would be to keep it all inside the `encode` function, and merely chunk it if `decode` is False:
For variation, this approach shows a different way to translate the text.
```python
from string import ascii_lowercase as asc_low
ENCODING = {c: asc_low[i] for i, c in enumerate(asc_low[::-1])}

def encode(text: str, decode: bool = False):
    res = "".join(ENCODING.get(c, c) for c in text.lower() if c.isalnum())
    return res if decode else " ".join(res[i:i+5] for i in range(0, len(res), 5))

def decode(text: str):
    return encode(text, True)
```
For more detail, [read here][approach-mono-function].

[approach-separate-functions]: https://exercism.org/tracks/python/exercises/atbash-cipher/approaches/separate-functions
[approach-mono-function]: https://exercism.org/tracks/python/exercises/atbash-cipher/approaches/mono-function
[generator expression]: https://www.programiz.com/python-programming/generator
