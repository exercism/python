# Cubic-time triply-nested loops

```python
def triplets_with_sum(n):
    triplets = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if a**2 + b**2 == c**2 and a + b + c == n:
                    triplets.append([a, b, c])
    return triplets
```

The strategy in this case is to scan through all three variables and test them in the innermost loop.
But the innermost loop will test all variables _every time_ the enclosing loop iterates.
And the enclosing loop up will iterate through all of its range _every time_ the outermost loop iterates.

So the 'work' this code has to do for each additional value in `range(1, n+1)` is `n**3`.

This gives code that is simple, clear, ...and so slow as to be useless for all but the smallest values of `n`.

We could tighten up the bounds on loop variables: for example, `a` is the smallest integer of a triplet that sums to `n`, so inevitably `a < n //3`.

However, this is not nearly enough to rescue an inappropriate algorithm.
