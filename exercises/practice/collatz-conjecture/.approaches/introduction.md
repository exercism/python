# Introduction

There are various approaches to solving the Collatz Conjecture exercise in Python.
You can for example use a while loop or a recursive function.
You can also solve it by using if and else statements or the ternary operator.

## General guidance

The key to this exercise is to check if the number and then do the correct operation.
Under this process you are supposed to count how many steps it takes to get to one.

## Approach: If/Else

This is a good way to solve the exercise, it is easy to understand and it is very readable.
The reason why you might not want to use this approach is because it is longer than the other approaches.

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

For more information, check the [if/else approach][approach-if-else].

## Approach: Ternary operator

In this approach we use the ternary operator.
It allows us to write a one-line if and else statement.
This makes the code more concise.

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

For more information, check the [Ternary operator approach][approach-ternary-operator].

## Approach: Recursive function

In this approach we use a recursive function.
A recursive function is a function that calls itself.
The reason why you want to use this approach is because it is more concise than the other approaches.
Since it doesn't need a counter variable.

The reason why you might not want to use this approach is that python has a limit on how many times a function can call itself.
This limit is 1000 times.

```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return 1 + steps(number)
```

For more information, check the [Recursion approach][approach-recursion].

## Benchmarks

To get a better understanding of the performance of the different approaches, we have created benchmarks.
For more information, check the [Performance article][performance-article].

[approach-if-else]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/if-else
[approach-recursion]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/recursion
[approach-ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[performance-article]: https://exercism.org/tracks/python/exercises/collatz-conjecture/articles/performance
