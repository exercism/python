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
It is a powerful technique, but can be more tricky to implement than a while loop.
Recursion isn't that common in Python, it is more common in functional programming languages, like: [Elixir][elixir], [Haskell][haskell], and [Clojure][clojure].

This approach starts with checking if the number is less than or equal to zero.
If it is, then it raises a [`ValueError`][value-error].

After that, we check if the number is equal to one.
If it is, then we return zero.

We then use the same conditional expression/ternary operator as the [ternary operator][ternary-operator] approach does.
We assign **number** to the result of the conditional expression.
The expression checks if the number is even.
If the number is even, we divide it by two.
If it isn't, we multiply it by three and add one.

After that, we `return` one plus the result of calling the `steps` function with the new number value.
This is the recursion part.

Solving this exercise with recursion removes the need for a "counter" variable and the instantiation of a `loop`.
If the number is not equal to one,  we call `1 + steps(number)`.
Then the `steps` function can execute the same code again with new values.
Meaning we can get a long chain or stack of `1 + steps(number)` until the number reaches one and the code adds 0.
That translates to something like this: `1 + 1 + 1 + 1 + 0`.

Python doesn't have [tail call optimization][tail-call].
Which means that the stack of `1 + steps(number)` will grow until it reaches the recursion limit.

~~~~exercism/caution
In Python, we can't have a function call itself more than 1000 times by default.
Code that exceeds this recursion limit will throw a  [RecursionError](https://docs.python.org/3/library/exceptions.html#RecursionError).
While it is possible to adjust the [recursion limit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit), doing so risks crashing Python and may also crash your system.
Casually raising the recursion limit is not recommended.
~~~~

[clojure]: https://exercism.org/tracks/clojure
[elixir]: https://exercism.org/tracks/elixir
[haskell]: https://exercism.org/tracks/haskell
[recursion]: https://realpython.com/python-thinking-recursively/
[tail-call]: https://en.wikipedia.org/wiki/Tail_call
[ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
