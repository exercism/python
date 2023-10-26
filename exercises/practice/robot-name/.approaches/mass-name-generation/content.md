# Mass Name Generation
We'd first have to generate all the possible names, shuffle them, and then use `next` (the simplest way) or maintain a `current_index` and get the name.
Note that selecting randomly from the list of all names would be incorrect, as there's a possibility of the name being repeated.

Here's a possible way to do it:

```python
from itertools import product
from random import shuffle
from string import ascii_uppercase

letter_pairs = (''.join(p) for p in product(ascii_uppercase, ascii_uppercase))
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

The first few lines of the mass name generation uses [`itertools.product`][itertools-product].
The resultant code is a simplification of:
```python
letter_pairs = (''.join((l1, l2)) for l1 in ascii_uppercase for l2 in ascii_uppercase)
numbers = (str(i).zfill(3) for i in range(1000))
names = [l + n for l in letter_pairs for n in numbers]
```

After the name generation, the names are shuffled - using the [default `seed`][random-seed] in the `random` module (the current timestamp). 
When the tests reseed `random`, this has no effect as the names were shuffled before that.

We then set `NAMES` to the iterable of names, and in `reset`, set the robot's name to the  `next(name)`. 
If you'd like, read more on [`iter` and `next`][iter-and-next].

Unlike the on the fly approach, this has a relatively short "generation" time, because we're merely giving the `next` name instead of generating it.
However, this has a huge startup memory and time cost, as 676,000 strings have to be calculated and stored. 
For an approximate calculation, 676,000 strings * 5 characters / string * 1 byte / character gives 3380000 bytes or 3.38 MB of RAM - and that's just the memory aspect of it.
Sounds small, but it's relatively very expensive at the beginning.

Thus, this approach is inefficient in cases where only a small number of names are needed _and_ the time to set/reset the robot isn't crucial.

[random-seed]: https://docs.python.org/3/library/random.html#random.seed
[iter-and-next]: https://www.programiz.com/python-programming/methods/built-in/iter
[itertools-product]: https://www.hackerrank.com/challenges/itertools-product/problem
