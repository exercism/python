# Approach: Mono-function

Notice that the majority of the code is repetitive?
A fun way to solve this would be to keep it all inside the `encode()` function, and merely chunk it if `decode` is `False`:
For variation, this approach also shows a different way to translate the text.

```python
from string import ascii_lowercase as asc_low

ENCODING = {chr: asc_low[id] for id, chr in enumerate(asc_low[::-1])}

def encode(text, decode = False):
    line = "".join(ENCODING.get(chr, chr) for chr in text.lower() if chr.isalnum())
    return line if decode else " ".join(line[index:index+5] for index in range(0, len(line), 5))

def decode(text):
    return encode(text, True)
```

Here, we use a dictionary comprehension in which we reverse the ASCII lowercase digits, and enumerate through them — that is, `z` has index 0, `y` has index 1, and so on.
For each character, we set the value of `chr` in the resulting dictionary to the character at the respective index — so `z` would translate to `a`.

In the calculation of the result, we try to obtain the value of the character using `dict.get()`, which accepts a default parameter.
In this case, the character itself is the default — that is, numbers won't be found in the translation key, and thus should remain as numbers.

We use a [conditional expression (also known as a ternary operator)][conditional-expression] to check if we actually mean to decode the function, in which case we return the result as is.
If not, we chunk the result by joining every five characters with a space.

Another possible way to solve this would be to use a function that returns another function that encodes or decodes based on the outer function's parameter:

```python
from string import ascii_lowercase as asc_low

ENCODING = {chr: asc_low[id] for id, chr in enumerate(asc_low[::-1])}

def code(decode = False):
    def func(text):
        line = "".join(ENCODING.get(chr, chr) for chr in text.lower() if chr.isalnum())
        return line if decode else " ".join(line[index:index+5] for index in range(0, len(line), 5))
    return func

encode = code()
decode = code(True)
```

The logic is the same — the only change is that now we use use one function that generates two _other_ functions based on the boolean value of its parameter.

Here, we first call `code()` with no argument and set `encode` to the function that's returned, which performs encoding.
Then we call `code(True)` to get the decoding version of the function and set `decode` to that function.

After that, we can call `encode()` and `decode()` as normal, and both functions successfully perform their indended task.

[conditional-expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
