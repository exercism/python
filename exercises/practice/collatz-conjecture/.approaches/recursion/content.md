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

This approach uses [concept:python/recursion]() to solve the challenge.
`Recursion` is less common as a strategy in Python than in other "fully-functional" programming languages such as [Elixir][elixir], [Haskell][haskell], and [Clojure][clojure].
While it can be powerful, it can also be trickier to implement than looping constructs.

This approach starts with checking if `number <= 0` and raising a [`ValueError`][value-error] if it is.
Next, we `return` zero if `number == 1`.
This is the [`base case`][recursion-base-case].

We then assign `number` to the same `conditional expression` as seen in the [`ternary operator`][ternary-operator] approach.
Finally, we `return` one plus the result of calling `steps()`.
This is the [`recursive case`][recursive-case], where the function calls itself with a new `number` value.

Solving this exercise in this way removes the need for a `counter` variable and the creation of a `loop`.
If `number` is not equal to one, we call `1 + steps(number)`.
Then `steps()` can execute the same code again with new values.
This makes a long chain (_or stack_) of `1 + steps(number)` — until `number == 1` and the code adds zero and exits.
That translates to something like: `1 + 1 + 1 + 1 + 0`.

Python doesn't have [tail call optimization][tail-call], so the stack of `1 + steps(number)` will continue to grow until the `base case` triggers resolution, or the code reaches the `recursion limit`.


~~~~exercism/caution
In Python, we can't have a function call itself more than 1000 times by default. 
Code that exceeds this `recursion limit` will throw a [RecursionError](https://docs.python.org/3/library/exceptions.html#RecursionError).  

While it is possible to adjust the [`recursion limit`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit), doing so risks crashing Python and may also crash your system with a [`stack overflow`](https://en.wikipedia.org/wiki/Stack_overflow).
Casually raising the limit is not recommended and seldom helps the performance situation. 
Instead, applying [memoization techniques](https://dbader.org/blog/python-memoization) or [dynamic programming strategies](https://medium.com/@conniezhou678/mastering-data-algorithms-part-18-dynamic-programming-in-python-3077c01f4a15) is a better path.
~~~~

[clojure]: https://exercism.org/tracks/clojure
[elixir]: https://exercism.org/tracks/elixir
[haskell]: https://exercism.org/tracks/haskell
[tail-call]: https://en.wikipedia.org/wiki/Tail_call
[ternary-operator]: https://exercism.org/tracks/python/exercises/collatz-conjecture/approaches/ternary-operator
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
[recursion-base-case]: https://www.geeksforgeeks.org/dsa/what-is-base-case-in-recursion/
[recursive-case]: https://inventwithpython.com/blog/how-many-recursive-cases-and-base-cases-does-recursive-function-need.html
