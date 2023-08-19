# Introduction
Robot Name in Python is an interesting exercise for practising randomness.

## General Guidance
Two ways immedietely come to mind: generate all the possible names and then return them sequentially, or generate a random name and ensure that it's not been previously used.

Randomness can be a little, well, random, so **it's very easy to have an incorrect solution and still pass the tests**. It's strongly recommended to submit your solution for Code Review.

## Approach: mass name generation
We'd first have to generate all the possible names, shuffle them, and then use `next` (the simplest way) or maintain a `current_index` and get the name.
Here's a possible way to do it:

```python
from itertools import product
from random import shuffle
from string import ascii_uppercase as letters

letter_pairs = (''.join(p) for p in product(letters, letters))
numbers = (str(i).zfill(3) for i in range(1000))
names = [l + n for l, n in product(letter_pairs, numbers)]
shuffle(names)
NAMES = iter(names)
class Robot(object):
    def __init__(self):
        self.reset()
    def reset(self):
        self.name = next(NAMES)
```
Note that selecting randomly from the list of all names would be incorrect, as there's a possibility of the name being repeated.
For more detail and explanation of the code, [read here][approach-mass-name-generation].

## Approach: name on the fly
Another approach is to generate the name on the fly and add it to a cache or a store, and checking if the generated name hasn't been used previously.


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

For more detail and different ways to implement this, [read here][approach-name-on-the-fly].

[approach-name-on-the-fly]: https://exercism.org/tracks/python/exercises/robot-name/approaches/name-on-the-fly
[approach-mass-name-generation]: https://exercism.org/tracks/python/exercises/robot-name/approaches/mass-name-generation
