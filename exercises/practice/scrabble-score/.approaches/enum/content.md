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
    return sum(Scrabble[character] for character in word.upper())
```

This approach uses an [`Enum`][enum] to define the score of each letter.
An [`Enum`][enum] (_also known as an **enumeration**_) is an object with named attributes assigned unique values.
These attributes are referred to as the enumeration _members_.
`Enum`s can be iterated over to return their members in definition order.
Values can be accessed via index syntax using the member name (_similar to how a dictionary lookup works_) .
`Enum`s are immutable, and their members function as constants.
The `enum` module was added to python standard library (_also known as stdlib_) in Python 3.4.

This approach uses an [`IntEnum`][int-enum].
An `IntEnum` is very similar to an `Enum`, but restricts assigned values to `int`s.
This allows the `IntEnum` to act as a collection of integers.
In fact, `IntEnum`s are considered subclasses of `int`s.

To use an `IntEnum` you need to first [import][import] it using: `from enum import IntEnum`.
Then you can define your `IntEnum` subclass.

The `IntEnum` subclass is defined by using the [`class`][classes] keyword, followed by the name you are using for the class, and then the `IntEnum` class you are subclassing in parenthesis:

```python
class ClassName(IntEnum):
```

Member names are declared as constants (ALL CAPS) and assigned values using the `=` operator.

This approach works by creating all the uppercase letters as members with their values being the score.
After the `IntEnum` is defined, the `score` function is defined.

The `score` function takes a word as an argument.
The `score` function uses the same [generator expression][generator-expression] as the [dictionary approach][dictionary-approach], but with a slight modification.
Instead of looking up the value in a _dictionary_, it looks up the `InEnum` class member value.

[classes]: https://docs.python.org/3/tutorial/classes.html
[enum]: https://docs.python.org/3/library/enum.html
[generator-expression]: https://peps.python.org/pep-0289/
[int-enum]: https://docs.python.org/3/library/enum.html#enum.IntEnum
[import]: https://docs.python.org/3/reference/import.html
