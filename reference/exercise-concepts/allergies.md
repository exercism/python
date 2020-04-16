# Concepts of `allergies`

## Example implementation

After Python 3.4 an `enum.Flag` is the "one obvious" approach:

```python
from enum import Flag, auto

class Allergens(Flag):
    eggs = auto()
    peanuts = auto()
    shellfish = auto()
    strawberries = auto()
    tomatoes = auto()
    chocolate = auto()
    pollen = auto()
    cats = auto()

class Allergies:

    def __init__(self, score):
        mask = sum(a.value for a in Allergens)
        self.flags = Allergens(score & mask)

    def allergic_to(self, item):
        return Allergens[item] in self.flags

    @property
    def lst(self):
        return [a.name for a in Allergens if a in self.flags]
```

In prior versions an OrderedDict was necessary to _reliably_ ensure sort order and also O(1) lookup:

```python
from collections import OrderedDict

Allergens = OrderedDict(
    eggs = 1,
    peanuts = 2,
    shellfish = 4,
    strawberries = 8,
    tomatoes = 16,
    chocolate = 32,
    pollen = 64,
    cats = 128,
)

class Allergies:

    def __init__(self, score):
        mask = sum(Allergens.values())
        self.score = score & mask

    def allergic_to(self, item):
        return bool(self.score & Allergens[item])

    @property
    def lst(self):
        return [a for a in Allergens if self.allergic_to(a)]
```

There are also various solutions involving lists, but these all come with O(N) lookup.

## Concepts

- [Classes][classes]: the exercise relies on the `class` statement to create a custom class
- [Methods][methods]: the exercise relies on the `def` statement to create an instance method
- [Implied Argument][implied-argument]: the exercise relies on the implied passing of `self` as the first parameter of bound methods
- [Dunder Methods][dunder-methods]: the exercise relies on the `__init__` dunder method to control class instantiation
- [Enumerated Values][enumerated-values]: the exercise relies on a fixed enumeration of possible values in a data structure
- [Data Structures][data-structures]: the exercise requires the use of a collection like enum.Flag or collections.OrderedDict
- [Imports][imports]: a reasonably readable solution will require importing from the standard library
- [Powers of Two][powers-of-two]: the exercise relies on the use of powers of two in fundamental binary (bitwise) operations
- [Bitflags][bitflags]: a general understanding of bitflags is required to solve this exercise
- [Bitwise Operators][bitwise-operators]: this exercise relies on bitwise AND (`&`) and potentially bitwise LSHIFT (`<<`) to inspect the Boolean value of individual bits in a bitflag
- [Property Decorator][property-decorator]: this exercise relies on the `@property` decorator to provide read-only dynamic access to the current list of allergens
- [Membership Testing][membership-testing]: this exercise relies on testing membership of a value in a collection of values
- [Lookup Efficiency][lookup-efficiency]: an efficient solution requires knowing that membership testing is O(1) in **dict** and the **enum.Enum** variants, but is O(N) in **list** and other sequential types
