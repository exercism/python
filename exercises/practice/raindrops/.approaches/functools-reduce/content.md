# Use functools.reduce()


```python
from functools import reduce

def convert(number):
    sounds = ('Pling','Plang','Plong')
    factors = ((number % factor) == 0 for factor in (3,5,7)) #1 if no remainder, 0 if a remainder.
    result = reduce(lambda sound, item : sound + (item[0] * item[1]), zip(sounds, factors), '')
    
    return result or str(number)
```

This is essentially the same strategy as the [itertools.compress()][approach-itertools-compress] approach, but uses [`functools.reduce`][functools-reduce] with a [`lambda` expression][lambda] and string multiplication as a kind of mask.

The factors are calculated and then [`zip()`ed][zip] with the sounds into `tuples`.
Each string (_position 0 in the `tuple`_) is multiplied by the 'factor' (_a 1 if there is no remainder and a 0 if there is a remainder_).
The result is then 'reduced' to a combined result string with an empty string as an initializer.
If the result is empty, the number as a string is returned instead.

This is an interesting use of `functools.reduce()`, but not necessarily the most readable way to solve this exercise.
Importing `functools` adds overhead and separating the sounds from the factors risks errors as the factor list expands.
The syntax of `reduce()` also obfuscates string creation/concatenation.
Unless the team maintaining this code is comfortable with `functools.reduce()`, this might be better re-written using `join()`:


```python
def convert(number):
    sounds = ('Pling','Plang','Plong')
    factors = ((number % factor) == 0 for factor in (3,5,7))
    result = ''.join((item[0] * item[1]) for item in zip(sounds, factors))
    
    return result or str(number)
```

[lambda]: https://dbader.org/blog/python-lambda-functions
[functools-reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[approach-itertools-compress]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/itertools-compress
[zip]: https://docs.python.org/3/library/functions.html#zip
