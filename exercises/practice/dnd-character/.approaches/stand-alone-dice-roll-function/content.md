# Separate Dice Rolls into a Stand-Alone Dice Roll Function


```python
from random import choice, randint
from operator import floordiv


class Character:
    def __init__(self):
        self.strength = dice_rolls()
        self.dexterity = dice_rolls()
        self.constitution = dice_rolls()
        self.intelligence = dice_rolls()
        self.wisdom = dice_rolls()
        self.charisma = dice_rolls()
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return choice([*vars(self).values()])
    
        
def dice_rolls():
    values = sorted(randint(1, 6) for item in range(4))
    return sum(values[1:])

def modifier(constitution):
    return floordiv((constitution - 10), 2)
```


This approach separates the `ability()` method from a stand-alone function that calculates dice rolls.
`ability()` returns the value of a randomly chosen character ability using [`random.choice`][randon-choice], but does not roll dice or calculate values.
Instead, `dice_rolls()` handles the rolls/values, using [`random.randint`][random-randint] to generate them.
The argument for this is that the logic/functionality of rolling dice 4 times and summing the top three values is not really related to a DnD character or their abilities - it is independent and likely useful across a wider scope than just the character class.
It also makes it cleaner to maintain, should the method or number of the dice rolls change.

`dice_rolls()` is then called in `__init__()` to populate the listed-out character attributes.
`self.hitpoints` calls the second stand-alone `modifier()` function, adding it to 10 for the character's `hitpoints` attribute.
Note that `modifier()` uses the [`operator.floordiv`][operator-floordiv] method to trunkate the value.

This approach is valid and passes all the tests.
However, it will trigger an analyzer comment about there being "too few public methods", since there are no methods for this class beyond `ability()`.

The "too few" rule encourages you to think about the design of the class: is it worth the effort to create the class if it only holds attribute values for a character?
What other functionality should this class hold?
Should the `dice_roll()` function be outside or inside (_as a regular method or a static method_) the class?

None of these (_including the analyzer complaint about too few methods_) is a hard and fast rule or requirement - all are considerations for the class as you build out a larger program.

An alternative is to write a [dataclass][dataclass], although the design discussion and questions above remain the same:


```python
from random import choice, sample
from dataclasses import dataclass

@dataclass
class Character:
    
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0
    hitpoints: int = 0
    
    def __post_init__(self):
        for ability in vars(self):
            setattr(self, ability, dice_rolls())
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return choice([*vars(self).values()])
          
  
def dice_rolls():
    values = sample(range(1, 7), 4)
    return sum(values) - min(values)
        
def modifier(constitution):
    return (constitution - 10)//2
```


Note that here there is a [`__post_init__`][post-init] method to assign ability values to the attributes, and that the attributes must start with a default value (_otherwise, they can't be assigned to in post-init_).
`hitpoints` has the same treatment as the other attributes, and requires assignment in post-init.

`dice_rolls()` uses [`random.sample`][random-sample] for roll values here and `modifier()` uses the floor-division operator `//`.

[dataclass]: https://docs.python.org/3/library/dataclasses.html
[operator-floordiv]: https://docs.python.org/3/library/operator.html#operator.floordiv
[post-init]: https://docs.python.org/3/library/dataclasses.html#post-init-processing
[random-randint]: https://docs.python.org/3/library/random.html#random.randint
[random-sample]: https://docs.python.org/3/library/random.html#random.randint
[randon-choice]: https://docs.python.org/3/library/random.html#random.choice
