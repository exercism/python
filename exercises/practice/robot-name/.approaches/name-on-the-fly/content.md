# Find name on the fly
We generate the name on the fly and add it to a cache or a store, checking to make sure that the generated name has not been used previously.

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
We use a `set` for the cache as it has a low access time, and because we do not need the preservation of order or the ability to access by index.

Using `choices` is one of the many ways to generate the name.
Another way might be to use `randrange` along with `zfill` for the number part, and a double `random.choice` / `random.choice` on `itertools.product` to generate the letter part.
The first is shorter, and best utilizes the Python standard library.

As we are using a `while` loop to check for the name generation, it is convenient to store the local `name` using the [walrus operator][walrus-operator].
It's also possible to find the name once before the loop, and then find it again inside the loop, but that would be an unnecessary repetition:
```python
def reset(self):
    name = self.__get_name()
    while name in cache:
        name = self.__get_name()
    cache.add(name)
    self.name = name
```
A helper method ([private][private-helper-methods] in this case) makes your code cleaner, but it's equally valid to have the code in the loop itself:
```python
def reset(self):
    while (name := ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))) in cache:
        pass
    cache.add(name)
    self.name = name
```

We call `reset` from `__init__` - it is syntactically valid to do it the other way around, but it is not considered good practice to call [dunder methods][dunder-methods] directly.

This has almost no startup time and memory, apart from declaring an empty `set`.
Note that the _generation_ time is the same as the [mass generation approach][approach-mass-name-generation], as a similar method is used.
However, as the name is generated at the time of setting/resetting, the method time itself is higher.

In the long run, if many names are generated, this is inefficient, since collisions will start being generated more often than unique names. 

[walrus-operator]: https://realpython.com/python-walrus-operator/
[private-helper-methods]: https://www.geeksforgeeks.org/private-methods-in-python/
[dunder-methods]: https://dbader.org/blog/python-dunder-methods
[approach-mass-name-generation]: https://exercism.org/tracks/python/exercises/robot-name/approaches/mass-name-generation
