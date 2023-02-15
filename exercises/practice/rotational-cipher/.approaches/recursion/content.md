# Recursion

```python
AlPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    if text == "":
        return ""
    first_letter, rest = text[0], text[1:]
    if first_letter.isalpha():
        if first_letter.isupper():
            return AlPHABET[(AlPHABET.index(first_letter.lower()) + key) % 26].upper() + rotate(rest, key)
        else:
            return AlPHABET[(AlPHABET.index(first_letter) + key) % 26] + rotate(rest, key)
    else:
        return first_letter + rotate(rest, key)
```

This approach uses the same logic as that of the `alphabet` approach, but instead of a `loop`, [concept:python/recursion]() is used to parse the text and solve the problem.

[Recursion][recursion] is a programming technique where a function calls itself.
It is powerful, but can be more tricky to implement than a `while loop` or `for loop`.
Recursive techniques are more common in functional programming languages like [Elixir][elixir], [Haskell][haskell], and [Clojure][clojure] than they are in Python.

Solving this exercise with recursion removes the need for a `result` variable and the instantiation of a `loop`.
If the number is not equal to one, we call `<letter> + rotate(rest)`.
Then the `rotate` function can execute the same code again with new values.
We can build a long chain or "stack" of `<letter> + rotate(rest)` calls until the `rest` variable is exhausted and the code adds `""`.
That translates to something like this: `<letter> + <letter> + <letter> + <letter> + ""`.


~~~~exercism/note
By default, we can't have a function call itself more than 1000 times.
Code that exceeds this recursion limit will throw a [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError).
While it is possible to [adjust the recursion limit](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit), doing so risks crashing Python and may also crash your system.
Casually raising the recursion limit is not recommended.

~~~~

[clojure]: https://exercism.org/tracks/clojure
[elixir]: https://exercism.org/tracks/elixir
[haskell]: https://exercism.org/tracks/haskell
[recursion]: https://realpython.com/python-thinking-recursively/
