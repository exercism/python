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
    res = "".join(chr for chr in text.lower() if chr.isalnum()).translate(ENCODING)
    return " ".join(res[index:index+5] for index in range(0, len(res), 5))

def decode(text: str):
    return "".join(chr.lower() for chr in text if chr.isalnum()).translate(ENCODING)
```
Read more on this [approach here][approach-seperate-functions].

## Approach: mono-function
Notice that there the majority of the code is repetitive? 
A fun way to solve this would be to keep it all inside the `encode` function, and merely chunk it if `decode` is False:
For variation, this approach shows a different way to translate the text.
```python
from string import ascii_lowercase as asc_low
ENCODING = {chr: asc_low[id] for id, chr in enumerate(asc_low[::-1])}

def encode(text: str, decode: bool = False):
    res = "".join(ENCODING.get(chr, chr) for chr in text.lower() if chr.isalnum())
    return res if decode else " ".join(res[index:index+5] for index in range(0, len(res), 5))

def decode(text: str):
    return encode(text, True)
```
For more detail, [read here][approach-mono-function].

[approach-separate-functions]: https://exercism.org/tracks/python/exercises/atbash-cipher/approaches/separate-functions
[approach-mono-function]: https://exercism.org/tracks/python/exercises/atbash-cipher/approaches/mono-function
[generator expression]: https://www.programiz.com/python-programming/generator
