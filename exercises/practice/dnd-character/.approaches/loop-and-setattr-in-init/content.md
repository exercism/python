# Loop Through an Abilities Tuple to Set Attribute Values in `__init__`


```python
from random import choice, sample

class Character:
    
    abilities = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')

    def __init__(self):
        for ability_type in Character.abilities:
            setattr(self, ability_type, Character.dice_rolls())
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return choice([*vars(self).values()])
          
    @staticmethod    
    def dice_rolls():
        values = sample(range(1, 7), 4)
        return sum(values) - min(values)
        
def modifier(constitution):
    return (constitution - 10)//2
```


This approach uses a `tuple` to hold character attributes in a [`class variable`][class-variable] or `class attribute`.
Since this variable is common to all instances of the class, it can be looped through during object initialization to create instance variables and assign them values using [`setattr][setattr].

This strategy has several benefits:
1.  The `__init__`  is less verbose and the abilities are easier to maintain.
2.  Organizationally, attributes remain with the class, making it clearer where they apply.
3.  Attributes are inherited in any subclass and can be added to or overridden by them.
4.  Changes to attributes are reflected in all new objets and subclasses automatically.

Because `hitpoints` is calculated differently, it is assigned a value outside the `tuple` and `loop`.

The remainder of the class body is the same as in the [dice roll static method][approach-dice-roll-static-method] approach (_as is the variant below_).


```python
from random import choice, sample

CHARACTER_ABILITIES = ('strength', 'dexterity', 'constitution',
             'intelligence', 'wisdom', 'charisma')

class Character:
    
    def __init__(self):
        for ability_type in CHARACTER_ABILITIES:
            setattr(self, ability_type, Character.dice_rolls())
        
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return choice([*vars(self).values()])
          
    @staticmethod    
    def dice_rolls():
        values = sample(range(1, 7), 4)
        return sum(values) - min(values)
        
def modifier(constitution):
    return (constitution - 10)//2
```

Above, the character attributes are moved out of the class into a [`constant`][constant] at the module level.
The Character `__init__` method loops through them using `setattr` to create instance variables and assign them values, similar to the first example.
Again, because `hitpoints` is calculated differently, it is assigned a value outside the `tuple` and `loop`.
Making the character attributes a constant has the advantage of being visible to all other classes and functions defined in the module.
 This could be easier if the attributes are being used by multiple classes beyond the Character class.
This also avoids having to reference the Character class when using or modifying the abilities and could help with clarity and maintenance in the larger program.
However, modifying the abilities in this context would also be visible at the module level, and could have wide or unintended consequences, so should be commented/documented carefully.

The remainder of the class body is the same as in the [dice roll static method][approach-dice-roll-static-method] approach (_as is the variant below_).


[approach-dice-roll-static-method]: https://exercism.org/tracks/python/exercises/dnd-character/approaches/dice-roll-static-method
[class-variable]: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
[constant]: https://peps.python.org/pep-0008/#constants
[setattr]: https://docs.python.org/3/library/functions.html#setattr
