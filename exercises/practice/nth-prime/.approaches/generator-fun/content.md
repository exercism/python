# Generator Fun
The key of this approach is to not store the elements you do not need.

This is a code representation:
```python
from itertools import islice, count

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    gen = islice(filter(lambda counter: all(counter % test != 0 for test in range(2, int(counter ** 0.5) + 1)), count(2)), number)
    for _ in range(number - 1): next(gen)
    return next(gen)
```

Let's dissect it! `itertools.count` is like `range` without un upper bound - calling it returns a generator, and `for ... in count_obj` will result in an infinite loop.

Using a lambda expression, we `filter` out any numbers above two that are prime.
Doesn't this result in an infinite loop? 
No - `filter` _also_ returns a generator object (which are [evaluated lazily][generator]), so while it's too will produce values infinitely if evaluated, it doesn't hang to program at the time of instantiation.

`itertools.islice` takes in a generator object and an end count, returning a generator object which _only evalutes until that end count_. 

The next line exhausts all the values in the generator except the end, and we finally return the last element.

We can utilize the `functools.cache` decorator for greater speeds at higher values of `number`, so we take it out. The added bonus is that a very long line of code is cleant up.

```python
from itertools import islice, count
from functools import cache

@cache
def is_prime(counter):
    return all(counter % test != 0 for test in range(2, int(counter ** 0.5) + 1))

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    gen = islice(filter(is_prime, count(2)), number)
    for _ in range(number - 1): next(gen)
    return next(gen)
```

~~~~exercism/note
Note that this that not create a list anywhere, and thus is both memory and time efficient.
~~~~

Read more on `itertools` on the [Python docs][itertools].

[itertools]: https://docs.python.org/3/library/itertools.html
[generator]: https://www.programiz.com/python-programming/generator