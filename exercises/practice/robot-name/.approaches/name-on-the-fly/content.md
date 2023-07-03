# Find name on the fly
We generate the name on the fly and add it to a cache or a store, and checking if the generated name hasn't been used previously.

A possible way to implement this:
```python
from string import ascii_uppercase, digits
from random import choices

cache = set()


class Robot:
    def __get_name(self): 
        return ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))

    def reset(self):
        while (name := self.__get_name()) in cache:
            pass
        cache.add(name)
        self.name = name

    def __init__(self): 
        self.reset()
```
We use a `set` for the cache as it has a low access time, and we don't need the preservation of order or the ability to be indexed.

This way is merely one of the many to generate the name. 
Another way might be to use `randrange` along with `zfill` for the number part, and a double `random.choice` / `random.choice` on `itertools.product` to generate the letter part.
This is the shortest way, and best utilizes the Python standard library.

As we're using a `while` loop to check for the name generation, it's convenient to store the local `name` using the [walrus operator][walrus-operator].
It's also possible to find the name before the loop and find it again inside the loop, but that would unnecessary repetition.
A helper method ([private][private-helper-methods] in this case) makes your code cleaner, but it's equally valid to have the code in the loop itself:
```python
def reset(self):
    while (name := ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))) in cache:
        pass
    cache.add(name)
    self.name = name
```

We call `reset` from `__init__` - it's syntactically valid to do it the other way round, but it's not considered good practice to call [dunder methods][dunder-methods] directly.

This has almost no startup time and memory, apart from declaring an empty `set`.
Note that the _generation_ time is the same as the mass generation approach, as a similar method is used.
However, as the name is generated at the time of setting/resetting, the method time itself is higher.

In the long run, if many names are generated, this is inefficient, since collisions will start being generated more often than unique names. 

[walrus-operator]: https://realpython.com/python-walrus-operator/
[private-helper-methods]: https://www.geeksforgeeks.org/private-methods-in-python/
[dunder-methods]: https://dbader.org/blog/python-dunder-methods