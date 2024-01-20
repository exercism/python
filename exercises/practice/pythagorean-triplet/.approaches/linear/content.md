# Linear-time algorithms with no nested loops


The key point with this approach is that we only loop over the variable `c` in a specific range.
Some mathematical analysis (_essentially, [solving simultaneous equations][simultaneous-equasions]_) then allows us to find valid values of `a` and `b`.

Other than that, the code syntax below is fairly mainstream across programming languages.
A related approach instead loops over `a`.

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


This second code example has no explicit `for` loop (_in Python syntax_), but the `generator-expression` and the `list-comprehension` both translate to `FOR_ITER` at the bytecode level.
  So this solution is essentially the same as the first, written in a more 'Pythonic' syntax -- but that syntax does incur a small overhead in performance.
  The performance hit is likely due to the extra instructions in the bytecode used to manage the `generator-expression` (_pausing the loop, resuming the loop, yielding results_) and then calling or unpacking the generator in the `list comprehension`.
  However, you would have to carefully profile the code to really determine the slowdown.

  With all that said, using a `generator` or `generator-expression` with or without a `list-comprehension` might be a better strategy if your code needs to process a very large number of triplets, as it avoids storing all the results in memory until they need to be returned.
  Using a `generator` or `generator-expression` by itself can also nicely set up a scenario where results are "streamed" or emitted 'on demand' for another part of the program or application.

  For more details on what these two solutions look like at the byte code level, take a look at Pythons [`dis`][dis] module.


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
- Nested functions, with the inner function able to reference variables such as `n` passed into the outer function.
- The generator expression creates `two_sides` as a lazily-evaluated iterator (_smaller memory footprint_)
- The [`walrus operator`][walrus-operator] `:=` is new in Python 3.8.
- The `is_integer()` method replaces `if D == int(D)`.
- Using `** 0.5` to calculate the square roots avoids a `math` import.


[dis]: https://docs.python.org/3/library/dis.html
[simultaneous-equasions]: https://thirdspacelearning.com/gcse-maths/algebra/simultaneous-equations/
[walrus-operator]: https://mathspp.com/blog/pydonts/assignment-expressions-and-the-walrus-operator
