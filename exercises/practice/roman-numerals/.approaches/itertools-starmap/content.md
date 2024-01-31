# With `itertools.starmap()`

```python
from itertools import starmap

def roman(number: int) -> str:
    orders = [(1000, "M  "), (100, "CDM"), (10, "XLC"), (1, "IVX")] 
    options = lambda I, V, X: ["", I, I * 2, I * 3, I + V, V, V + I, V + I * 2, V + I * 3, I + X]
    compute = lambda n, chars: options(*chars)[number % (n * 10) // n]
    return "".join(starmap(compute, orders))
```

This approach is certainly concise and ingenious, though it takes functional programming to a level that some Python programmers might consider a little cryptic.

The [`itertools.starmap()`][starmap] method is a variant of `map()` that takes its argument parameters pre-zipped in tuples.
It has the signature `starmap(f: function, i: iter) -> iter`.

## Linting

One issue with this code is the use of named lambdas.
This is discouraged by [PEP-8][pep8], and linters will complain about it.

The underlying reason is that lambdas are intended to be anonymous functions embedded within other expressions.
Internally, they are all given the same name `<lambda>`, which can greatly complicate debugging.
Their use is a particular bugbear of the Python track maintainer.

We can refactor the code to satisfy the linter by using named `def` statements, and lowercase argument names. 
Type hints are also added for documentation:

```python
from itertools import starmap


def roman(number: int) -> str:
    def options(i: str, v: str, x: str):
        return ["", i, i * 2, i * 3, i + v, v, v + i, v + i * 2, v + i * 3, i + x]

    def compute(n: int, chars: str) -> iter:
        return options(*chars)[number % (n * 10) // n]

    orders = [(1000, "M  "), (100, "CDM"), (10, "XLC"), (1, "IVX")]
    return "".join(starmap(compute, orders))
```

## Analysis

The central concept is that Roman letters are defined for 1, 5 and 10, times various powers of 10.

`orders` is relatively straightforward: a list of tuples, with each tuple containing the powers of 10 and (as far as possible) the letters for that number times (1, 5, 10). 
Roman numerals for 5,000 and 10,000 are not defined, so are replaced here by spaces.

The `options()` function just takes the three letters from one of these tuples and returns a list of numerals that can be constructed from them.
For example, the 10 to 90 range:

```python
options('X', 'L', 'C')
# => ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
```

There is no zero, so that is replaced by an empty string.

The `compute()` function takes a tuple from `orders` plus the top-level parameter `number`, and converts the appropriate decimal digit to its Roman equivalent, returning an `iterator`.
For example the first digit of 723:

```python
number = 723
[x for x in compute(100, "CDM")]
# => ['D', 'C', 'C']
```

The `starmap()` function ties `orders`, `options()` and `compute` together, splitting up strings and tuples as necessary to give each function the parameters it needs.
Again, an iterator is returned:

```python
number = 723
[x for x in starmap(compute, orders)]
# => ['', 'DCC', 'XX', 'III']
```

Finally, `''.join()` converts this iterator to a single string that can be returned as the desired answer.

Once we get past the deliberate obfuscation, it is quite an elegant approach. 
Though perhaps not the most idiomatic Python.

## Credit

We owe this approach to @MAPKarrenbelt, who must have had fun with it.

[starmap]: https://docs.python.org/3/library/itertools.html#itertools.starmap
[pep8]: https://peps.python.org/pep-0008/#programming-recommendations
