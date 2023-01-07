# Introduction

There are various ways to solve `palindrome-products`.
This approaches document shows 2 _common_ strategies, with one being a lot more efficient than the other.
That being said, neither approach here is considered canonical, and other "pythonic" approaches could be added/expanded on in the future.

## General guidance

The goal of this exercise is to generate the largest and smallest palindromes from a given range of numbers.

## Approach: Using a nested for loop

A nested for loop is a good approach to this problem.
It is simple and easy to understand and it works.

```python
def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b >= result:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)
```

For more information, check the [Nested for loop approach][approach-nested-for-loop].

## Approach: Using a nested for loop, optimized edition

This approach is similar to the previous one, but with the addition of a few lines of code we can make it much faster.
The question then becomes _how much faster_?
Well, for some input sizes it reduces the time from **9 minutes to 0.01 seconds**.
You can read more about it in the [Performance article][article-performance].

```python
def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(max_factor, min_factor - 1,-1):
        was_bigger = False
        for number_b in range(max_factor, number_a - 1, -1):
            if number_a * number_b >= result:
                was_bigger = True
                test_value  = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
        if not was_bigger:
            break
    if result == 0:
        result = None
    return (result, answer)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        was_smaller = False
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                was_smaller = True
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
        if not was_smaller:
            break
    if result == 0:
        result = None
    return (result, answer)
```

You can read more about how to achieve this optimization in: [Nested for loop optimized][approach-nested-for-loop-optimized].

## Benchmark

For more information, check the [Performance article][article-performance].

[approach-nested-for-loop]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop
[approach-nested-for-loop-optimized]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop-optimized
[article-performance]: https://exercism.org/tracks/python/exercises/palindrome-products/articles/performance
