# About

Many programs need (apparently) random values to simulate real-world events.

Common, familiar examples include:
- A coin toss: a random value from `('H', 'T')`.
- The roll of a die: a random integer from 1 to 6.
- Shuffling a deck of cards: a random ordering of a card list.

Generating truly random values with a computer is a [surprisingly difficult technical challenge][truly-random], so you may see these results referred to as "pseudorandom".

In practice, a well-designed library like the [`random`][random] module in the Python standard library is fast, flexible, and gives results that are amply good enough for most applications in modelling, simulation and games.

The rest of this page will list a few of the most common functions in `random`.
We encourage you to explore the full `random` documentation, as there are many more options than what we cover here.



~~~~exercism/caution

The `random` module should __NOT__ be used for security and cryptographic applications.

Instead, Python provides the [`secrets`][secrets] module.
This is specially optimized for cryptographic security.
Some of the prior issues and reasons for creating the secrets module can be found in [PEP 506][PEP 506].

[secrets]: https://docs.python.org/3.11/library/secrets.html#module-secrets
[PEP 506]: https://peps.python.org/pep-0506/
~~~~



## Importing

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


## Creating random integers

The `randrange()` function has three forms, to select a random value from `range(start, stop, step)`:
  1.  `randrange(stop)` gives an integer `n` such that `0 <= n < stop`
  2.   `randrange(start, stop)` gives an integer `n` such that `start <= n < stop`
  3.  `randrange(start, stop, step)` gives an integer `n` such that `start <= n < stop` and `n` is in the sequence `start, start + step, start + 2*step...`

For the common case where `step == 1`, the `randint(a, b)` function may be more convenient and readable.
Possible results from `randint()` _include_ the upper bound, so `randint(a, b)` is the same as using `randrange(a, b+1)`:

```python
>>> import random

# Select one number at random from the range 0, 499
>>> random.randrange(500)
219

# Select 10 numbers at random between 0 and 9 two steps apart.
>>> numbers = []
>>> for integer in range(10):
>>>    numbers.append(random.randrange(0, 10, 2))
>>> print(numbers)
[2, 8, 4, 0, 4, 2, 6, 6, 8, 8]

# roll a die
>>> random.randint(1, 6)  
4
```



## Working with sequences

The functions in this section assume that you are starting from some [sequence][sequence-types], or other container.


This will typically be a `list`, or with some limitations a `tuple` or a `set` (_a `tuple` is immutable, and `set` is unordered_).



### `choice()` and `choices()`

The `choice()` function will return one entry chosen at random from a given sequence.
At its simplest, this might be a coin-flip:

```python
# This will pick one of the two values in the list at random 5 separate times 
>>> [random.choice(['H', 'T']) for _ in range(5)]
['T', 'H', 'H', 'T', 'H']

We could accomplish essentially the same thing using the `choices()` function, supplying a keyword argument with the list length:


```python
>>> random.choices(['H', 'T'], k=5)
['T', 'H', 'T', 'H', 'H']
```


In the examples above, we assumed a fair coin with equal probability of heads or tails, but weights can also be specified.
For example, if a bag contains 10 red balls and 15 green balls, and we would like to pull one out at random:

```python
>>> random.choices(['red', 'green'], [10, 15])
['red']
```



### `sample()`

The `choices()` example above assumes what statisticians call ["sampling with replacement"][sampling-with-replacement].
Each pick or choice has **no effect** on the probability of future choices, and the distribution of potential choices remains the same from pick to pick.


In the example with red and green balls: after each choice, we _return_ the ball to the bag and shake well before the next pick.
This is in contrast to a situation where we pull out a red ball and _it stays out_.
Not returning the ball means there are now fewer red balls in the bag, and the next choice is now _less likely_ to be red.

To simulate this "sampling without replacement", the random module provides the `sample()` function.
The syntax of `sample()` is similar to `choices()`, except it adds a `counts` keyword parameter:


```python
>>> random.sample(['red', 'green'], counts=[10, 15], k=10)
['green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red', 'green']
```

Samples are returned in the order they were chosen.



### `shuffle()`

Both `choices()` and `sample()` return new lists when `k > 1`.
In contrast, `shuffle()` randomizes the order of a list _**in place**_, and the original ordering is lost:

```python
>>> my_list = [1, 2, 3, 4, 5]
>>> random.shuffle(my_list)
>>> my_list
[4, 1, 5, 2, 3]
```


## Working with Distributions

Until now, we have concentrated on cases where all outcomes are equally likely.
For example, `random.randrange(100)` is equally likely to give any integer from 0 to 99.

Many real-world situations are far less simple than this.
As a result, statisticians have created a wide variety of [`distributions`][probability-distribution] to describe "real world" results mathematically.



### Uniform distributions

For integers, `randrange()` and `randint()` are used when all probabilities are equal.
This is called a [`uniform`][uniform-distribution] distribution.


There are floating-point equivalents to `randrange()` and `randint()`.

__`random()`__ gives a `float` value `x` such that `0.0 <= x < 1.0`.

__`uniform(a, b)`__ gives `x` such that `a <= x <= b`.

```python
>>> [round(random.random(), 3) for _ in range(5)]
[0.876, 0.084, 0.483, 0.22, 0.863]

>>> [round(random.uniform(2, 5), 3) for _ in range(5)]
[2.798, 2.539, 3.779, 3.363, 4.33]
```



### Gaussian distribution

Also called the "normal" distribution or the "bell-shaped" curve, this is a very common way to describe imprecision in measured values.

For example, suppose the factory where you work has just bought 10,000 bolts which should be identical.
You want to set up the factory robot to handle them, so you weigh a sample of 100 and find that they have an average (or `mean`) weight of 4.731g.
This is extremely unlikely to mean that they all weigh exactly 4.731g.
Perhaps you find that values range from 4.627 to 4.794g but cluster around 4.731g.

This is the [`Gaussian distribution`][gaussian-distribution], for which probabilities peak at the mean and tails off symmetrically on both sides (hence "bell-shaped").
To simulate this in software, we need some way to specify the width of the curve (_typically, expensive bolts will cluster more tightly around the mean than cheap bolts!_).

By convention, this is done with the [`standard deviation`][standard-deviation]: small values for a sharp, narrow curve, large for a low, broad curve.
Mathematicians love Greek letters, so we use `μ` ('mu') to represent the mean and `σ` ('sigma') to represent the standard deviation.
Thus, if you read that "95% of values are within 2σ of μ" or "the Higgs boson has been detected with 5-sigma confidence", such comments relate to the standard deviation.

```python
>>> mu = 4.731
>>> sigma = 0.316
>>> [round(random.gauss(mu, sigma), 3) for _ in range(5)]
[4.72, 4.957, 4.64, 4.556, 4.968]
```

[gaussian-distribution]: https://simple.wikipedia.org/wiki/Normal_distribution
[probability-distribution]: https://simple.wikipedia.org/wiki/Probability_distribution
[random]: https://docs.python.org/3/library/random.html
[sampling-with-replacement]: https://www.youtube.com/watch?v=LnGFL_A6A6A
[sequence-types]: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
[standard-deviation]: https://simple.wikipedia.org/wiki/Standard_deviation
[truly-random]: https://www.malwarebytes.com/blog/news/2013/09/in-computers-are-random-numbers-really-random
[uniform-distribution]: https://www.investopedia.com/terms/u/uniform-distribution.asp#:~:text=In%20statistics%2C%20uniform%20distribution%20refers,a%20spade%20is%20equally%20likely.
