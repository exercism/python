# Enum

```python
from enum import IntEnum

class Scrabble(IntEnum):
    A = E = I = O = U = L = N = R = S = T = 1
    D = G = 2
    B = C = M = P = 3
    F = H = V = W = Y = 4
    K = 5
    J = X = 8
    Q = Z = 10

def score(word):
    return sum(Scrabble[char.upper()] for char in word)
```

This approach uses an [`enum`][enum] to define the score of each letter.
An `enum` or known as a enumerations is sets of named constant and is immutable.
`enum` was added to python standard library also known as stdlib in python 3.4.

This approach uses an [`intEnum`][int-enum] it works very similar to a normal `enum` but it has the added benefit that the values are integers.
Thereby acts like integers.

To use an `intEnum` you need to [import][import] it using: `from enum import IntEnum`.
Then you can define the `enum` class.

The `enum` class is defined by using the [`class`][classes] keyword.
Then you need to specify the name of the class.

After that is constant declared by giving the constant capital letters and the value is assigned by using the `=` operator.
This approach works by giving all the letters as constants and then value of the constant is the score of the letter.
After the `enum` is defined, the `score` function is defined.

The `score` function takes a word as a parameter.
And uses the same [generator expression][generator-expersion] as the [dictionary approach][dictionary-approach].
But instead of looking up the value in a dictionary it looks it up in the `enum` class.

[classes]: https://docs.python.org/3/tutorial/classes.html
[enum]: https://docs.python.org/3/library/enum.html
[generator-expersion]: https://peps.python.org/pep-0289/
[int-enum]: https://docs.python.org/3/library/enum.html#enum.IntEnum
[import]: https://docs.python.org/3/reference/import.html
