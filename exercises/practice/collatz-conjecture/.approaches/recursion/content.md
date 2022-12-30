# Recursion

```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return 1 + steps(number)
```

This approach uses [concept:python/recursion]() to solve the problem.
Recursion is a programming technique where a function calls itself.
Recursion is a powerful technique, but can be more tricky.
Recursion isn't that common in Python, it is more common in functional programming languages, like: [Elixir][elixir], [Haskell][haskell], and [Clojure][clojure].

This approach starts with checking if the number is less than or equal to zero.
If it is, then it raises a [`ValueError`][value-error].

After that we check if the number is equal to one.
If it is, then we return zero.

Then we use the same ternary operator as in the [ternary operator][ternary-operator] approach.
We declare that number is equal to the result of the ternary operator.
The ternary operator checks if the number is even.
If it is, then we divide it by two.
If it isn't, then we multiply it by three and add one.

After that we return one plus the result of calling the `steps` function with the new number.
This is the recursion part.

Doing this exercise with recursion removes the need for a "counter" variable.
Since what we do is that if the number is not one we do `1 + steps(number)`.
Then that function can do the same thing.
Meaning we can get a long chain of `1 + steps(number)` until we reach one and add 0.
That will translate to something like this: `1 + 1 + 1 + 1 + 0`.

In python we can't have a function call itself more than 1000 times.

[clojure]: https://exercism.org/tracks/clojure
[elixir]: https://exercism.org/tracks/elixir
[haskell]: https://exercism.org/tracks/haskell
[recursion]: https://realpython.com/python-thinking-recursively/
[ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
