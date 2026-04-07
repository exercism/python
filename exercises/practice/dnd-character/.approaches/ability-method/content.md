# Use the `ability()` Method to Generate and Return the Dice Rolls


```python
from random import sample

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        values = sample(range(1, 7), 4)
        return sum(values) - min(values)
        
def modifier(constitution):
    return (constitution - 10)//2
```


This approach uses a single `ability()` method to calculate the dice rolls and return an ability value.
`ability()` is then called in `__init__()` to populate the listed-out character attributes.
`self.hitpoints` calls the stand-alone `modifier()` function, adding it to 10 for the character's hitpoints attribute.

This approach is valid and passes all the tests.
However, it will trigger an analyzer comment about there being "too few public methods", since there are no methods for this class beyond the one that calculates attribute values.


The "too few" rule encourages you to think about the design of the class: is it worth the effort to create the class if it only holds attribute values for a character?
What other functionality should this class hold?
Should you separate dice rolls from ability values?
Is the class better as a [dataclass][dataclass], with dice roll as a utility function?

None of these (_including the analyzer complaint about too few methods_) is a hard and fast rule or requirement - all are considerations for the class as you build out a larger program.


[dataclass]: https://docs.python.org/3/library/dataclasses.html
