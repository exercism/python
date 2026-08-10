# Move Dice Rolls Into a Static Method Separate from the `ability` Method


```python
from math import floor
from random import choice

class Character:
    def __init__(self):
        self.strength = Character.dice_rolls()
        self.dexterity = Character.dice_rolls()
        self.constitution = Character.dice_rolls()
        self.intelligence = Character.dice_rolls()
        self.wisdom = Character.dice_rolls()
        self.charisma = Character.dice_rolls()
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return choice([*vars(self).values()])
        
    @staticmethod    
    def dice_rolls():
        values = sorted(choice(range(1,7)) for dice in range(4))[::-1]
        return sum(values[:-1])

def modifier(constitution):
    return floor((constitution - 10)/2)
```

This approach separates the `ability()` method from a [`static method`][staticmethod] that calculates dice rolls.
`ability()` returns the value of a randomly chosen character ability using [`random.choice`][random-choice] but does not roll dice or calculate values.
Instead, `dice_rolls()` handles the rolls/values using [`random.choice`][random-choice] for selection.

The argument for this is that the logic/functionality of rolling dice 4 times and summing the top three values is not really related to a DnD character or their abilities - it is independent and likely useful across a wider scope than just the character class.
However, it might be tidier to include it in the character class, rather than "clutter" the program or module with an additional stand-alone function.
Declaring `dice_rolls()` as a static method allows other callers to use the function with or without instantiating a new  `Character` object.
It also makes it cleaner to maintain, should the method or number of the dice rolls change.

`dice_rolls()` is then called in `__init__()` to populate the listed-out character attributes.
Note that it needs to be called with the class name: `Character.dice_rolls()`.
`self.hitpoints` then calls the second stand-alone `modifier()` function, adding it to 10 for the character's `hitpoints` attribute.
`modifieer()` in this example uses [`math.floor`][math-floor] for calculating the `hitpoints` value.

[math-floor]: https://docs.python.org/3/library/math.html#math.floor
[random-choice]: https://docs.python.org/3/library/random.html#random.choice
[staticmethod]: https://docs.python.org/3/library/functions.html#staticmethod
