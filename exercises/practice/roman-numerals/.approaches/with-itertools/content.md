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

TODO - well, it would be, right?


[starmap]: https://docs.python.org/3/library/itertools.html#itertools.starmap
[pep8]: https://peps.python.org/pep-0008/#programming-recommendations
