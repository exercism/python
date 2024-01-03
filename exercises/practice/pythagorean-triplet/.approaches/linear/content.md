# Linear-time algorithms with no nested loops

```python
from math import sqrt

def triplets_with_sum(n):
    N = float(n)
    triplets = []
    for c in range(int(N / 2) - 1, int((sqrt(2) - 1) * N), -1):
        D = sqrt(c ** 2 - N ** 2 + 2 * N * c)
        if D == int(D):
            triplets.append([int((N - c - D) / 2), int((N - c + D) / 2), c])
    return triplets
```

The key point with this approach is that we only loop over the variable `c`.
Some mathematical analysis (essentially, solving simultaneous equations) then allows us to find valid values of `a` and `b`.

Other than that, the code syntax above is fairly mainstream.

A related approach instead loops over `a`.
The code below has no explicit `for` loop, but the comprehensions do essentially the same thing in a more Pythonic way.

```python
def triplets_with_sum(n):
    def calculate_medium(small):
        return (n ** 2 - 2 * n * small) / (2 * (n - small))

    two_sides = ((int(medium), small) for small in range(3, n // 3)
                 if small < (medium := calculate_medium(small))
                 and medium.is_integer())

    return [[small, medium, (medium ** 2 + small ** 2) ** 0.5]
            for medium, small in two_sides]
```

Some implementation details to notice:
- Nested functions, with the inner function able to reference variables such as `n` in the outer function.
- The first comprehension creates `two_sides` as a lazily-evaluated iterator.
- The [`walrus operator`][walrus-operator] `:=` is new in Python 3.8.
- The `is_integer()` method replaces `if D == int(D)`.
- Using `** 0.5` to calculate the square roots avoids a `math` import.

# _Bethany_, this is your submission
Is there anything else you want to say about it?

[walrus-operator]: https://mathspp.com/blog/pydonts/assignment-expressions-and-the-walrus-operator
