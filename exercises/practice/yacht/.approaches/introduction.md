# Introduction
Yacht in Python can be solved in many ways. The most intuitive approach is to use an `if` structure. 
Alternatively, you can create functions and set their names to the constant names.

## General guidance
The main thing in this exercise is to map a category (_here defined as constants in the stub file_) to a function or a standalone piece of code. 
While mapping generally reminds us of dictionaries, here the constants are global.
This indicates that the most idiomatic approach is not using a `dict`.
Adhering to the principles of DRY is important - don't repeat yourself if you can help it, especially in the `ONES` through `SIXES` categories!

## Approach: functions
Each bit of functionality for each category can be encoded in a function, and the constant name set to that function. 
This can be done by assigning the constant name to a `lambda` or creating a one-line function using the constant as a function name. 
```python
def digits(num):
    return lambda dice: dice.count(num) * num
YACHT = lambda dice: 50 if dice.count(dice[0]) == len(dice) else 0
ONES = digits(1)
TWOS = digits(2)
THREES = digits(3)
FOURS = digits(4)
FIVES = digits(5)
SIXES = digits(6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else 0
FOUR_OF_A_KIND = lambda dice: 4 * dice[1] if dice[0] == dice[3] or dice[1] == dice[4] else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum
def score(dice, category):
    return category(dice)
```
This is a very succinct way to solve the exercise, although some one-liners get a little long. 
For more information on this approach, read [this document][approach-functions].

## Approach: if structure
The constants can be set to random, null, or numeric values, and an `if` structure inside `score` determines the code to be executed. 
As one-liners aren't necessary here, we can spread out the code to make it look neater:
```python
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'
YACHT = 'YACHT'
def score(dice, category):
    if category in (1,2,3,4,5,6):
         return dice.count(category) * category
    elif category == 'FULL_HOUSE':
        if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3]:
            return sum(dice) or 0
    elif category == 'FOUR_OF_A_KIND':
        if dice[0] == dice[3] or dice[1] == dice[4]:
            return dice[1] * 4 or 0
    elif category == 'LITTLE_STRAIGHT':
        if sorted(dice) == [1, 2, 3, 4, 5]: 
            return 30 or 0
    elif category == 'BIG_STRAIGHT':
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30 or 0
    elif category == 'YACHT':
        if all(num == dice[0] for num in dice):
            return 50
    elif category == 'CHOICE':
        return sum(dice)
    return 0
```
Read more on this approach [here][approach-if-structure].

[approach-functions]: https://exercism.org/tracks/python/exercises/yacht/approaches/functions
[approach-if-structure]: https://exercism.org/tracks/python/exercises/yacht/approaches/if-structure
