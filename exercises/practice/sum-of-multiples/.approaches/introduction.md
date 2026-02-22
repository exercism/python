# Introduction

<!-- TODO write a proper introduction -->

Several possible approaches to this exercise:

- filter for multiples
- generate multiples and
  - gather & de-duplicate, e.g. using `set().union`
  - merge the multiple-generators into one
- spot the repeating pattern


## Approach: `filter` for multiples

```python
def sum_of_multiples(limit, factors):
    return sum(filter(
        lambda n: any(n % f == 0 for f in factors if f != 0),
        range(limit)
    ))
```

Probably the most straightforward way of solving this problem is to

1. look at every individual integer between `0` and `limit`,
2. check that it is a multiple of any of the given `factors`, and
3. add it to the sum when it is.

An important advantage of this approach is that it is very easy to understand.
However, it suffers from potentially performing a lot of unnecessary work, for example when all `factors` are large, or when there are no `factors` at all.

[Read more about this approach][filter-for-multiples].


<!-- TODO improve section title -->
## Approach: generate & gather multiples

```python
def sum_of_multiples(limit, factors):
    multiples = (range(0, limit, f) for f in factors if f != 0)
    return sum(set().union(*multiples))
```

Egregious memory occupancy when multiples are many.

...


<!-- TODO improve section title -->
## Approach: merge the multiple-generators into one

```python
# NOTE This is a sketch (but it does work)
def sum_of_multiples(limit, factors):
    generators = [range(0, limit, f) for f in factors if f != 0]
    while len(generators) > 1:
        generators = [
            merge(g, g_)
            for g, g_ in zip_longest(generators[0::2], generators[1::2], fillvalue=())
        ]
    all_multiples, *_ = generators + [()]
    return sum(all_multiples)


def merge(gen1, gen2):
    """Merge two sorted-without-duplicates iterables
    into a single sorted-without-duplicates generator.
    """
    return sorted({*gen1, *gen2})  # FIXME this is CHEATING
```

This is supposed to use very little memory.

...


<!-- TODO: improve section title -->
## Approach: spot the repeating pattern

```python
# NOTE this too is but a sketch (that nevertheless works)
def sum_of_multiples(limit, factors):
    (*factors,) = filter(lambda f: f != 0, factors)
    N = lcm(*factors)
    is_multiple = lambda n: any(n % f == 0 for f in factors)
    multiples_up_to_lcm = [n for n in range(1, N + 1) if is_multiple(n)]
    q, r = divmod(limit - 1, N)
    return (
        q * (q - 1) // 2 * N * len(multiples_up_to_lcm)
        + q * sum(multiples_up_to_lcm)
        + sum(q * N + m for m in takewhile(lambda m: m <= r, multiples_up_to_lcm))
    )
```

```text
assuming:    limit = 22    multiples = [2, 3]
the task is to sum the lower 4 below rows

| 1  2  3  4  5  6| 7  8  9 10 11 12|13 14 15 16 17 18|19 20 21
|    2  3  4     6|    6  6  6     6|    6  6  6     6|    6  6
|                 |    2  3  4     6|    6  6  6     6|    6  6
|                 |                 |    2  3  4     6|    6  6
|                 |                 |                 |    2  3

We see
  3  copies of  - 2 3 4 - 6
  0+1+2 = 3×(3-1)/2 = 3  copies of  - 6 6 6 - 6
  3  copies of  - 6 6
  1  copy   of  - 2 3
```

<!-- TODO properly explain this stuff -->

This approach saves on a lot of iteration, but is still vulnerable to excessive memory use.
Fortunately it can be combined with the generator merging approach.

...



[filter-for-multiples]: https://exercism.org/tracks/python/exercises/sum-of-multiples/approaches/filter-for-multiples "Approach: filter for multiples"
