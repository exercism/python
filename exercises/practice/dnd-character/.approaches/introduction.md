# Introduction

The DnD Character exercise has two main purposes:

1. Practice class-based programming, especially initialization of instance variables and the creation of methods.
2. Practice the use of pseudo-random numbers and methods in the Python [`random`][random] module.

There are no complicated decisions to make about which algorithm to use, as the tests for this exercise constrain the implementation.
However, there is variation in how class and object variables are declared and initialized, how methods are declared, and which random functions are employed.

These approaches will mostly explore these variations in Python syntax.


## General considerations

Several items are specifically required and tested for:

- A standalone (_outside the `Character` class_) function called `modifier()`.
- A `Character` class.
- Instance variables for 6 named abilities, plus one for hit points.
- An instance method called `ability()` to return ability values.

Further methods are optional, but may be helpful to simulate random dice rolls and calculate ability scores.
Some methods (_such as `ability()`, or the optional `dice_roll()`_) may be better as [static methods][static-methods], since they do not necessarily require the class or object as a parameter but are still tied to the class logic/purpose.


### The `modifier()` function

This stand-alone function modifies the characters constitution score by subtracting 10 from the total and dividing by 2.

In Python 3.x, the division operators are `/` for floating point and `//` for integer or 'floor' division.
`modifier()` needs to use integer division, and return a result that does not have a decimal.
Function equivalents to `/` and `//` are [`operator.truediv(a, b)`][operator-trudiv] and [`operator.floordiv(a, b)`][operator-floordiv] (or [`math.floor(x)`][math-floor]).

Integer division will always round "down": not to the nearest integer and not towards zero:

```python
>>> 11 // 3
3
>>> -11 // 3
-4
```

Here are examples using both operators and functions imported from `math` and from `operator`:

```python
def modifier(constitution):
    return (constitution - 10)//2

# You can import the math module and use `floor()`
from math import floor

def modifier(constitution):
    return floor((constitution - 10)/2)

# Another strategy is to use `floordiv()` from the operator module.
from operator import floordiv

def modifier(constitution):
    return floordiv((constitution - 10), 2)
    
```

Using function equivalents in a solution will work, but they do create overhead due to module import and function calls.


### Dice rolls

The instructions are to roll four 6-sided dice and record the sum of the largest three rolls.

To simulate a roll of the dice, we need the [`random`][random] module which produces pseudo-random numbers.
The [`secrets`][secrets] module, which produces cryptographically strong random numbers is not needed here.

Within `random`, there are various suitable methods available.
 These include [`random.randint()`][randint] to produce an integer in a range, [`random.choice()`][choice] to select from a sequence of values, or even [`random.sample()`][random-sample] for multiple rolls 'sampled' from a distribution, group, or range of values.

 ````exercism/note
 
`randint(lower, upper)` _**includes**_ the upper bound, in contrast to the built-in [`range(lower, upper)`][range], or Python's [slice notation][slice] which both _**exclude**_ the upper bound.

[slice]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[range]: https://docs.python.org/3/library/stdtypes.html#range
````


To roll four dice may need a loop or comprehension:

```python
from random import randint, choice, sample

    # Choosing a pseudo-random number between 1 and 6 (inclusive) four different times.
    def dice_rolls_randint(self):
        rolls = []
        
        for dice in rage(4):
            rolls.append(randint(1, 6))
        
        return rolls

    # Choosing from a range sequence between 1 and 7 (exclusive) four different times.
    def dice_rolls_choice(self):
        return [choice(range(1,7)) for dice in range(4)]

    # Choosing for different 'samples' (rolls) from a sample range 
    # between 1 and 7 (exclusive). This avoids a comprehension, 
    # since random.sample returns a list of unique values from the range.
    def four_dice_rolls_sample(self):
        return sample(range(1, 7), 4)
        
```

Some community solutions begin with a call to `random.seed()` but (_at least in recent versions of Python_) calling this without a parameter has exactly the same effect as omitting it.
The value of this method is in debugging situations when it helps to have a reproducible sequence of results.
Then we would call it with a known seed such as `random.seed(42)`.

After rolling four dice, we next need to sum the largest three scores, discarding the lowest.
Many programmers use `sorted()` and a slice for determining the three largest values:


```python
# The dice variable was generated as a 4-element list, as above.
sum(sorted(dice)[1:])

# The list can also be reverse sorted.
sum(sorted(dice, reverse=True)[:-1])

```

If slicing is hard to read or confusing, the built-ins `sum()` and `min()` can be used to subtract the smallest score from the total.
In this second case, `dice` can be any sequence, not just a list.
Because we are calculating a `min()` value, a generator expression cannot be used.

```python
# The dice variable was generated as a 4-element sequence, as above.
sum(dice) - min(dice)

```

This strategy might be considered more readable to some, since `min()` is very clear as to what is being calculated.
This is also more efficient when the input list is long and the order of values doesn't need to be preserved.


### The ability() Method

The directions do not state how `ability()` should be implemented, but a look at [the tests][dnd-tests] indicate that any of the character's ability scores or a freshly generated score can be returned provided the score falls in the required range.
This means that the method can return a random ability value chosen from `vars(self).values()` **or** it can calculate and return a random value for use in an ability score.
Some solutions use this method as their "dice roll", and call it to populate abilities in `__init__`.
Other solutions separate out "dice rolls" or "ability score" logic into a separate method or function, leaving `ability()` as a method that returns a random choice from the character's already assigned abilities.

Either strategy above will pass the tests, but separating out "dice roll" logic from a random character ability score can be both clearer and more reusable in scenarios where the same "dice roll" is used to calculate/populate some other metric.
Moving the "dice roll" or "ability score" out of the class altogether or making it a static method also lets it be called/used without instantiating the class and can make it clearer what is being calculated.


## Class initialization

The various abilities need to be set just once for each character, which is most conveniently done in the class `__init__` method.

The examples below assume that `modifier()` and `self.ability()` are implemented as discussed in the sections above.
The explicit approach is simple but rather verbose and repetitive.
It does have the advantage of declaring the abilities very explicitly, so that a reader can quickly determine how many and of what type the abilities are:


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
        
        ...


# Using a dice_roll static method instead of self.ability()
class Character:
    def __init__(self):
        self.strength = Character.dice_roll()
        self.dexterity = Character.dice_roll()
        self.constitution = Character.dice_roll()
        self.intelligence = Character.dice_roll()
        self.wisdom = Character.dice_roll()
        self.charisma = Character.dice_roll()
        self.hitpoints = 10 + modifier(self.constitution)
        
        ...
```


Alternatively, we could start from an iterable of ability names and loop over these using [`setattr()`][setattr] to write the values into the objects attribute dictionary.
This sacrifices a bit of readability/clarity for less verbosity and (somewhat) easier ability additions:


```python
# Setting a global ABILITIES constant. 
# This enables other classes to "see" the abilities. 
# This could be useful for a larger program that modifies 
# or adds abilities outside  the Character class.
ABILITIES = ('strength', 'dexterity', 'constitution',
             'intelligence', 'wisdom','charisma')


class Character:
    def __init__(self):
    
        for ability_name in ABILITIES:
            setattr(self, ability_name, self.ability())
            
        self.hitpoints = modifier(self.constitution) + 10

        
# Conversely, we can declare ABILITIES as a 
# class attribute. This ensures that all objects made from 
# the class share ABILITIES and they are only added or 
# modified through the Character class. ABILITIES are not 
# visible globally.
class Character:

    abilities = ('strength', 'dexterity', 'constitution',
                 'intelligence', 'wisdom','charisma')

    def __init__(self):
    
        for ability_name in Character.abilities:
            setattr(self, ability_name, self.ability())
            
        self.hitpoints = modifier(self.constitution) + 10
```

Listing out each ability vs looping through and using `setatter()` has identical results for the object.
Both calculate a score for an ability and write that ability + score into the object attribute dictionary when an object is instantiated from the class.


## Putting things together

The four approaches below combine various options from the previous sections to show how a solution would work with them.
More variations are possible, but these cover most of the main decision differences.

- [One `ability` method][approach-ability-method]
- [Dice roll static method][approach-dice-roll-static-method]
- [Dice roll stand-alone method][approach-stand-alone-dice-roll-function]
- [Loop and `setatter()` in `__init__`][approach-loop-and-setattr-in-init]


[approach-ability-method]: https://exercism.org/tracks/python/exercises/dnd-character/approaches/ability-method
[approach-dice-roll-static-method]: https://exercism.org/tracks/python/exercises/dnd-character/approaches/dice-roll-static-method
[approach-loop-and-setattr-in-init]: https://exercism.org/tracks/python/exercises/dnd-character/approaches/loop-and-setattr-in-init
[approach-stand-alone-dice-roll-function]: https://exercism.org/tracks/python/exercises/dnd-character/approaches/tand-alone-dice-roll-function
[choice]: https://docs.python.org/3/library/random.html#random.choice
[dnd-tests]: https://github.com/exercism/python/blob/main/exercises/practice/dnd-character/dnd_character_test.py
[math-floor]: https://docs.python.org/3/library/math.html#math.floor
[operator-floordiv]: https://docs.python.org/3/library/operator.html#operator.floordiv
[operator-trudiv]: https://docs.python.org/3/library/operator.html#operator.truediv
[randint]: https://docs.python.org/3/library/random.html#random.randint
[random-sample]: https://docs.python.org/3/library/random.html#random.sample
[random]: https://exercism.org/tracks/python/concepts/random
[secrets]: https://docs.python.org/3/library/secrets.html
[setattr]: https://docs.python.org/3/library/functions.html#setattr
[static-methods]: https://www.digitalocean.com/community/tutorials/python-static-method
