# Introduction

The main challenge in solving the Pythagorean Triplet exercise is to use a fast enough algorithm.
The problem can easily become very large, and simple solutions may time out on the test runner.

There are three reasonably common solutions to this problem
- a [cubic time][approaches-cubic] solution, which is fairly obvious
- a [quadratic time][approaches-quadratic] solution, which is reasonably easy to find
- a [linear time][approaches-linear] solution, requiring some deeper understanding of the mathematics

If those terms are unclear to you, you might like to read about [time complexity][time-complexity].

The basic idea is to study how algorithms scale (in run time, memory usage, or whatever) as the input parameter becomes very large. 
In this document we will focus on run time, which is critical for this exercise.

## General guidance

The goal of the Pythagorean Triplets exercise is to find combinations of three numbers `[a, b, c]` satisfying a set of conditions:
1. `a < b < c`
2. `a**2 + b**2 == c**2`
3. `a + b + c == n`, where `n` is supplied as a parameter to the function.

For a given `n`, the solution should include all valid triplets as a list of lists.

## Approach: Cubic time solution with 3-deep nested loops

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

This is the most naive approach, scanning through all possible integers `<= n` that satisfy `a < b < c`.

***Don't do this!*** 

It works for small values of `n`, but becomes impossibly slow as `n` grows larger.
The test suite will not complete within any reasonable time limit.

## Approach: Quadratic time solution with 2-deep nested loops

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

Given the constraint that `a + b + c == n`, we can eliminate the innermost loop and calculate `c` directly.
This gives a substantial speed advantage, allowing the tests to run to completion in a reasonable time, locally.

However, the Exercism test runner will still time out.

Examining the code. it is clear that the upper bounds on loop variables are far too generous.

The solution below tightens the bounds and pre-calculates `c * c` in the outer loop.
This gives about a 4-fold speedup, but still times out on the test runner.

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

If a quadratic-time algorithm was the best available option, there are other ways to squeeze out small performance gains.

For bigger problems outside Exercism, there are third-party packages such as `numpy` or `numba` which replace Python 
loops (versatile but relatively slow) with routines written in C/C++, perhaps with use of the GPU.
Runtime is still proportional to `n**2`, but the proportionality constant may be much smaller. 

Fortunately for the present discussion, mathematicians have been studying Pythagorean Triplets for centuries: see [Wikipedia][wiki-pythag], [Wolfram MathWorld][wolfram-pythag], or many other sources.

There are much faster algorithms, at the expense of reduced readability.

## Linear time solutions

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

All clear?

After some thoughtful mathematical analysis, there is now only a single loop.

Run time is now much faster, especially for large `n`, but a reasonable person could find it difficult to understand what the code is doing.

If you do things like this out in the real world ***please*** document your code carefully.
In a few weeks, the bare code will puzzle even yourself, and people seeing for the first time are likely to struggle.

The code above uses fairly mainstream syntax. Another submission used the same basic algorithm but in a more pythonic way:

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

## Which approach to use?

If we could be sure that the code only had to handle small values of `n`, a quadratic method would have the advantage of clarity.

However, the test suite goes up to 30_000, and the online test runner times out.
We need to accept some less readable code and use a linear-time implementation.

Full details of run-time benchmarking are given in the [Performance article][article-performance].

Overall, the results confirm the expectation that the linear-time methods are very much faster.
More surprisingly, the first example (with an explicit loop) proved slightly faster than the more Pythonic code.

[approaches-cubic]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches/cubic
[approaches-quadratic]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches/quadratic
[approaches-linear]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches/linear
[time-complexity]:  https://en.wikipedia.org/wiki/Time_complexity
[article-performance]:https://exercism.org/tracks/python/exercises/pythagorean-triplet/articles/performance
[wiki-pythag]: https://en.wikipedia.org/wiki/Pythagorean_triple
[wolfram-pythag]: https://mathworld.wolfram.com/PythagoreanTriple.html

