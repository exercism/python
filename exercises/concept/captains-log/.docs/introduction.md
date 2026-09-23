# Introduction

Many programs need (apparently) random values to simulate real-world events.

Common, familiar examples include:
- A coin toss: a random value from `('H', 'T')`.
- The roll of a die: a random integer from 1 to 6.
- Shuffling a deck of cards: a random ordering of a card list.
- The creation of trees and bushes in a 3-D graphics simulation.

Generating _truly_ random values with a computer is a [surprisingly difficult technical challenge][truly-random], so you may see these results referred to as "pseudorandom".

In practice, a well-designed library like the [`random`][random] module in the Python standard library is fast, flexible, and gives results that are amply good enough for most applications in modelling, simulation and games.

For this brief introduction, we show the four most commonly used functions from the module.
We encourage you to explore the full [`random`][random] documentation, as there are many tools and options.


~~~~exercism/caution

The `random` module should __NOT__ be used for security and cryptographic applications!!

Instead, Python provides the [`secrets`][secrets] module.
This is specially optimized for cryptographic security.
Some of the prior issues and reasons for creating the secrets module can be found in [PEP 506][PEP 506].

[secrets]: https://docs.python.org/3.11/library/secrets.html#module-secrets
[PEP 506]: https://peps.python.org/pep-0506/
~~~~


Before you can utilize the tools in the `random` module, you must first import it:

```python
>>> import random

# Choose random integer from a range
>>> random.randrange(1000)
360

>>> random.randrange(-1, 500)
228

>>> random.randrange(-10, 11, 2)
-8

# Choose random integer between two values (inclusive)
>>> random.randint(5, 25)
22

```

To avoid typing the name of the module, you can import specific functions by name:

```python
>>> from random import choice, choices

# Using choice() to pick Heads or Tails 10 times
>>> tosses = []
>>> for side in range(10):
>>>    tosses.append(choice(['H', 'T']))    

>>> print(tosses)
['H', 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'H']


# Using choices() to pick Heads or Tails 8 times
>>> picks = []
>>> picks.extend(choices(['H', 'T'], k=8))
>>> print(picks)
['T', 'H', 'H', 'T', 'H', 'H', 'T', 'T']
```

## `randrange()` and `randint()`

Shown in the first example above, the `randrange()` function has three forms:

1. `randrange(stop)` gives an integer `n` such that `0 <= n < stop`
2. `randrange(start, stop)` gives an integer `n` such that `start <= n < stop`
3. `randrange(start, stop, step)` gives an integer `n` such that `start <= n < stop`
    and `n` is in the sequence `start, start + step, start + 2*step...`

For the most common case where `step == 1`, `randint(a, b)` may be more convenient and readable.
Possible results from `randint()` _include_ the upper bound, so `randint(a, b)` is the same as using `randrange(a, b+1)`.



## `choice()` and `choices()`

These two functions assume that you are starting from some [sequence][sequence-types], or other container.
This will typically be a `list`, or with some limitations a `tuple` or a `set` (_a `tuple` is immutable, and `set` is unordered_).

The `choice()` function will return one entry chosen at random from a given sequence, and `choices()` will return `k` number of entries chosen at random from a given sequence.

In the examples shown above, we assumed a fair coin with equal probability of heads or tails, but weights can also be specified.

For example, if a bag contains 10 red balls and 15 green balls, and we would like to pull one out at random:


```python
>>> random.choices(['red', 'green'], [10, 15])
['red']
```

## `random()` and `uniform()`

For integers, `randrange()` and `randint()` are used when all probabilities are equal. This is called a `uniform` distributuion.

There are floating-point equivalents to `randrange()` and `randint()`.

__`random()`__ gives a `float` value `x` such that `0.0 <= x < 1.0`.

__`uniform(a, b)`__ gives `x` such that `a <= x <= b`.

```python
>>> [round(random.random(), 3) for n in range(5)]
[0.876, 0.084, 0.483, 0.22, 0.863]

>>> [round(random.uniform(2, 5), 3) for n in range(5)]
[2.798, 2.539, 3.779, 3.363, 4.33]
```



[random]: https://docs.python.org/3/library/random.html
[sequence-types]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[truly-random]: https://www.malwarebytes.com/blog/news/2013/09/in-computers-are-random-numbers-really-random