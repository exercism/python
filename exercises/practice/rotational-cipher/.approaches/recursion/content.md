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

This approach uses a very similar approach to alphabet.
And uses the same logic but instead of a loop so does this approach use [concept:python/recursion]() to solve the problem.

Recursion is a programming technique where a function calls itself.
It is a powerful technique, but can be more tricky to implement than a while loop.
Recursion isn't that common in Python, it is more common in functional programming languages, like: [Elixir][elixir], [Haskell][haskell], and [Clojure][clojure].

Solving this exercise with recursion removes the need for a "result" variable and the instantiation of a `loop`.
If the number is not equal to one, we call `<letter> + rotate(rest)`.
Then the `rotate` function can execute the same code again with new values.
Meaning we can get a long chain or stack of `<letter> + rotate(rest)` until the rest variable is exhausted and then the code adds `""`.
That translates to something like this: `<letter> + <letter> + <letter> + <letter> + ""`.

In Python, we can't have a function call itself more than 1000 times by default.
Code that exceeds this recursion limit will throw a [RecursionError][recursion-error].
While it is possible to adjust the [recursion limit][recursion-limit], doing so risks crashing Python and may also crash your system.
Casually raising the recursion limit is not recommended.

[clojure]: https://exercism.org/tracks/clojure
[elixir]: https://exercism.org/tracks/elixir
[haskell]: https://exercism.org/tracks/haskell
[recursion]: https://realpython.com/python-thinking-recursively/
[recursion-error]: https://docs.python.org/3/library/exceptions.html#RecursionError
[recursion-limit]: https://docs.python.org/3/library/sys.html#sys.setrecursionlimit
