## Approach: Mono-function
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
To explain the translation: we use a `dict` comprehension in which we reverse the ASCII lowercase digits, and enumerate through them - that is, `z` is 0, `y` is 1, and so on. 
We access the character at that index and set it to the value of `c` - so `z` translates to `a`.

In the calculation of the result, we try to obtain the value of the character using `dict.get`, which accepts a default parameter. 
In this case, the character itself is the default - that is, numbers won't be found in the translation key, and thus should remain as numbers.

We use a [ternary operator][ternary-operator] to check if we actually mean to decode the function, in which case we return the result as is. 
If not, we chunk the result by joining every five characters with a space.

Another possible way to solve this would be to use a function that returns a function that encodes or decodes based on the parameters:
```python
from string import ascii_lowercase as alc

lowercase = {chr: alc[id] for id, chr in enumerate(alc[::-1])}

def code(decode=False):
    def func(text):
        line = "".join(lowercase.get(chr, chr) for chr in text.lower() if chr.isalnum())
        return line if decode else " ".join(line[index:index+5] for index in range(0, len(line), 5))
    return func

    
encode = code()
decode = code(True)
```
The logic is the same - we've instead used one function that generates two _other_ functions based on the boolean value of its parameter.
`encode` is set to the function that's returned, and performs encoding.
`decode` is set a function that _decodes_.

[ternary-operator]: https://www.tutorialspoint.com/ternary-operator-in-python
[decorator]: https://realpython.com/primer-on-python-decorators/