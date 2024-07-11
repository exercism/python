# Introduction

The main challenge in solving the Pythagorean Triplet exercise is to come up with a 'fast enough' algorithm.
The problem space can easily become very large, and 'naive' or more 'brute force' solutions may time out on the test runner.

There are three reasonably common variations to this problem
1.  A [cubic time][approaches-cubic] solution, which uses highly nested loops and is non-performant.
2.  A [quadratic time][approaches-quadratic] solution, which uses one nested loop, and is reasonably easy to figure out.
3.  A [linear time][approaches-linear] solution, requiring some deeper understanding of the mathematics of finding triplets.


If those terms are unclear to you, you might like to read about [time complexity][time-complexity], and how it is  described by [asymptotic notation][asymptotic-notation].

The basic idea is to study how algorithms scale (_in CPU/GPU run time, memory usage, or other resource_) as the input parameters grow toward infinity.
In this document we will focus on run time, which is critical for this exercise.


## General guidance

The goal of `Pythagorean Triplets` is to find combinations of three numbers `[a, b, c]` satisfying a set of conditions:

1. `a < b < c`
2. `a**2 + b**2 == c**2` (_otherwise known as the [Pythagorean theorem][Pythagorean-theorem]_)
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

This is the most 'naive' or 'brute force' approach, scanning through all possible integers `<= n` that satisfy `a < b < c`.
This might be the first thing you think of when sketching out the algorithm on paper following the exercise instructions.
It is useful to see the steps of the solution and to look at the size of the problem space.

***Don't implement this in code!***

While it is a valid solution and it indeed works for small values of `n`, it becomes impossibly slow as `n` grows larger.
For any truly large values of `n`, this code might take over all the available processing power on your local computer and never complete.
For Exercism's online environment, the test suite will time out and fail.


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

Given the constraint that `a + b + c == n`, we can eliminate the innermost loop from the cubic approach and calculate `c` directly.
This gives a substantial speed advantage, allowing the tests to run to completion in a reasonable time, _locally_.

However, the Exercism online test runner will still time out with this solution.

Examining the code, it is clear that the upper bounds on the `loop` variables are far too generous, and too much work is being done.


The solution below tightens the bounds and pre-calculates `c * c` in the outer `loop`.
This gives about a 4-fold speedup, but still times out on the online test runner:


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

For bigger problems outside Exercism, there are third-party packages such as [`numpy`][numpy] or [`numba`][numba] which replace Python
loops (_versatile but relatively slow_) with routines written in C/C++, perhaps with use of the GPU.
The runtime is still proportional to `n**2`, but the proportionality constant (_which would be measured in C/C++ as opposed to Python_) may be much smaller.

Fortunately for the present discussion, mathematicians have been studying Pythagorean Triplets for centuries: see [Wikipedia][wiki-pythag], [Wolfram MathWorld][wolfram-pythag], or many other sources.

So mathematically there are much faster algorithms, at the expense of reduced readability.


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

_All clear?_ 😉

After some thoughtful mathematical analysis, there is now only a single loop!

Run time is now much faster, especially for large `n`, but a reasonable person could find it quite difficult to understand what the code is doing.

If you do things like this out in the 'real world' ***please*** document your code carefully.
It might also be helpful to choose variable names that are more descriptive to help readers understand all of the values and operations.
In a few weeks, the bare code will puzzle your future self.
People reading it for the first time are likely to struggle even more than you will.

The code above uses fairly 'generic' programming syntax.
Another submission used the same basic algorithm but in a more 'Pythonic' way:


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

Although it is important to note that this solution could have chosen a better name for the `n` parameter, and clearer formatting for the `generator-expression` and the `list-comprehension`:

```python
def triplets_with_sum(number):
    def calculate_medium(small):
         
        # We have two numbers, but need the third.
        return (number ** 2 - 2 * number * small) / (2 * (number - small))

    two_sides = (
                  (int(medium), small) for 
                  small in range(3, number // 3) if
                  
                  #Calls calculate_medium and assigns return value to variable medium 
                  small < (medium := calculate_medium(small)) and 
                  medium.is_integer()
                  )

    return [
            [small, medium, (medium ** 2 + small ** 2) ** 0.5]
            for medium, small in two_sides
            ]
```


## Which approach to use?

If we could be sure that the code only had to handle small values of `n`, a quadratic method would have the advantage of clarity.

However, the test suite goes up to 30_000, and the online test runner quickly times out.
We therefore need to accept some less readable code and use a linear-time implementation.

Full details of run-time benchmarking are given in the [Performance article][article-performance].

Overall, the results confirm the expectation that the linear-time methods are _very much_ faster.
More surprisingly, the first example of the linear implementation (_with an explicit loop_) proved slightly faster than the more 'Pythonic' code.
This is likely due to the overhead of creating and tracking the iterator for the `generator-expression`, calculating the 'expensive' `calculate_medium()` function call within that generator, and the additional 'expensive' conversions to `int()`.

[Pythagorean-theorem]: https://en.wikipedia.org/wiki/Pythagorean_theorem
[approaches-cubic]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches/cubic
[approaches-linear]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches/linear
[approaches-quadratic]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches/quadratic
[article-performance]:https://exercism.org/tracks/python/exercises/pythagorean-triplet/articles/performance
[asymptotic-notation]:  https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation
[numba]: https://numba.pydata.org/
[numpy]: https://numpy.org/
[time-complexity]: https://yourbasic.org/algorithms/time-complexity-explained/
[wiki-pythag]: https://en.wikipedia.org/wiki/Pythagorean_triple
[wolfram-pythag]: https://mathworld.wolfram.com/PythagoreanTriple.html
