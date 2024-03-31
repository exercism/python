# Introduction

This exercise has two main purposes:

- To practice class-based programming, especially initialization of instance variables.
- To practice random numbers.

There are no complicated decisions to make about which algorithm to use, as the tests constrain the implementation.

This document will mostly explore some variations in Python syntax.

## General considerations

Several items are specifically required by the tests:

- A standalone function called `modifier()`.
- A `Character` class.
- Instance variables for 6 named abilities, plus one for hitpoints.
- An instance method called `ability()` to handle dice throws.

Further methods are optional, but may be helpful with random dice rolls.

## The `modifier()` function

This function needs integer division:

```python
def modifier(constitution):
    return (constitution - 10) // 2
```

In Python 3.x, the division operators are `/` for floating point and `//` for integer division (ignore any old Python 2.x documentation you may find).

Integer division will always round *down*: not to the nearest integer and not towards zero:

```python
>>> 11 // 3
3
>>> -11 // 3
-4
```

Using `math.floor()` here will work, but slightly misses the point of what is being practised, as well as forcing an unnecessary import.

## Dice rolls

The instructions are to roll four 6-sided dice and record the sum of the largest three dice.

To roll a die we need the [`random`][random] module.

There are various suitable options available, including `random.randint()` and `random.choice()` for a single throw or `random.sample()` for multiple rolls.
Note that `randint(lower, upper)` *includes* the upper bound, in contrast to `range(lower, uppper + 1)`.

To roll four dice may need a list comprehension:

```python
    def dice_rolls_1(self):
        return [random.randint(1, 6) for _ in range(4)]

    def dice_rolls_2(self):
        return [random.choice(range(1,7)) for _ in range(4)]

    def four_dice_rolls(self):
        return random.sample(range(1, 7), 4)
```

Some community solutions begin with a call to `random.seed()` but (at least in recent versions of Python) calling this without a parameter has exactly the same effect as omitting it.
The value of this method is in debugging situations when it helps to have a reproducible sequence of results.
Then we would call it with a known seed such as `random.seed(42)`.

After rolling four dice, next we need to sum the largest three scores, discarding the lowest.

Most Python programmers use a list sort and slicing for this:

```python
# the dice variable was generated as a 4-element list, as above
sum(sorted(dice)[1:4])
```

In some ways simpler, we could use the built-in `sum()` and `min()` functions to subtract the smallest score from the total:

```python
# the dice variable was generated as a 4-element enumerable, as above
sum(dice) - min(dice)
```

In this second case, `dice` can be any enumerable, not just a list.

## Class initialization

The various abilities need to be set just once for each character, which is most conveniently done in the class initializer.

The examples below assume that `modifier()` and `self.ability()` are implemented as dicussed above

The explicit approach is simple but rather verbose and repetitive:

```python
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
```

Alternatively, we could start from a tuple of ability names then loop over these using [`setattr()`][setattr]:

```python
ABILITIES = (
    'strength',
    'dexterity',
    'constitution',
    'intelligence',
    'wisdom',
    'charisma'
)

class Character:
    def __init__(self):
        for ability_name in ABILITIES:
            setattr(self, ability_name, self.ability())
        self.hitpoints = modifier(self.constitution) + 10
```

The key to this is that these two expressions have identical results:

```python
    setattr(self, 'strength`, self.ability())
    self.strength = self.ability()
```

[random]: https://exercism.org/tracks/python/concepts/random
[setattr]: https://docs.python.org/3/library/functions.html#setattr
