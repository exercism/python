# Quadratic-time doubly-nested loops

```python
def triplets_with_sum(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                triplets.append([a, b, c])
    return triplets
```

Because `a + b + c == n`, we only loop over `a` and `b`.
The third variable `c` is then predictable.

The above code loops over the full range of both variables.
This means the 'work' this code has to do for each additional value in `range(1, n+1)` is `n**2`.
We know enough about the problems to tighten this up a bit.

For example:
- The smallest pythagorean is (famously) `[3, 4, 5]`, so `a >= 3`
- `a + b == n - c` and `a <= b`, so `a <= (n - c) // 2`

We can also avoid, to some extent, repeating the same multiplication many times.
This gets us to the code below:


```python
def triplets_with_sum(n):
    result = []
    for c in range(5, n - 1):
        c_sq = c * c
        for a in range(3, (n - c + 1) // 2):
            b = n - a - c
            if a < b < c and a * a + b * b == c_sq:
                result.append([a, b, c])
    return result
```

We could have done a bit better.
Though not stated in the problem description, `a + b > c`, otherwise they could not form a triangle.

This means that `c <= n // 2`, reducing the iterations in the outer loop.

However, these optimizations only reduce the run time by a small factor.
They do almost nothing to make the algorithm scale to large `n`.
