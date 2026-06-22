# Introduction

There are multiple idiomatic approaches to solving the Collatz Conjecture exercise in Python.
You can, for example, use a `while loop` or a `recursive` function.
You can also solve the exercise by using `if`/`else` statements or the `ternary operator`.

## General guidance

The key to this exercise is to check if the number is even or odd and then perform the correct operation.
Under this process (_if the data is not [pathological][collatz-pathological]_), the result will settle at 1.
Your task is to count how many steps it takes to get there.


## Approach: If/Else

This is a good way to solve the exercise, it is easy to understand and it is very readable.
The reason why you might _not_ want to use this approach is because it is more verbose than other approaches.


```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        counter += 1
    return counter
```

For more information, check out the [if/else approach][approach-if-else].


## Approach: Ternary operator

In this approach we replace the `if`/`else` multi-line construction with a [conditional expression][conditional-expression], sometimes called a _ternary operator_.
This syntax allows us to write a one-line `if`/`else` check, making the code more concise:


```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        counter += 1
    return counter
```

For more information, read the [Ternary operator approach][approach-ternary-operator].


## Approach: Recursive function

In this approach we use a `recursive function`.
A recursive function is a function that calls itself.
This approach can be more concise than other approaches, but may or may not be more readable for some audiences.

You might not want to use this approach due to Python's [`recursion` limit][recursion-limit], which has a default of 1000 stack frames.
While the current tests for this exercise all have input that is easily calculated in under the `recursion` limit, this is not true for arbitrary numbers.
To make this approach work with large numbers of steps, techniques such as memoization may need to be employed.


```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return 1 + steps(number)
```

For more information, check out the [`recursion` approach][approach-recursion].


## Benchmarks

To get a better understanding of the performance of the different approaches, we have created a small benchmarking application.
For more information on timings, check out the [Performance article][performance-article].

[approach-if-else]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/if-else
[approach-recursion]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/recursion
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[collatz-pathological]: https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/
[conditional-expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
[performance-article]: https://exercism.org/tracks/python/exercises/collatz-conjecture/articles/performance
[recursion-limit]: https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
