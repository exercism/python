# If structure
The constants can be set to random, null, or numeric values, and an `if` structure inside `score` determines the code to be executed. 
As one-liners aren't necessary here, we can spread out the code to make it look neater.
```python
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'

def score(dice, category):
    if category == 'ONES':
        return dice.count(1)
    elif category == 'TWOS':
        return dice.count(2) * 2
    elif category == 'THREES':
        return dice.count(3) * 3
    elif category == 'FOURS':
        return dice.count(4) * 4
    elif category == 'FIVES':
        return dice.count(5) * 5
    elif category == 'SIXES':
        return dice.count(6) * 6
    elif category == 'FULL_HOUSE':
        for i in dice:
            for j in dice:
                if dice.count(i) == 3 and dice.count(j) == 2:
                    return i * 3 + j * 2
    elif category == 'FOUR_OF_A_KIND':
        for j in dice:
            if dice.count(j) >= 4:
                return j * 4
    elif category == 'LITTLE_STRAIGHT':
        if dice.count(1) == 1 and dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5) == 1:
            return 30
    elif category == 'BIG_STRAIGHT':
        if dice.count(6) == 1 and dice.count(2) == 1 and dice.count(3) == 1 and dice.count(4) == 1 and dice.count(5) == 1:
            return 30
    elif category == 'YACHT':
        if all(i == dice[0] for i in dice):
            return 50
    elif category == 'CHOICE':
        return sum(dice)
    return 0
```
Note that the code inside the `if` statements themselves can differ, but the key idea here is to use `if` and `elif` to branch out the code, and return `0` at the end if nothing else has been returned. 
The `if` condition itself can be different, with people commonly checking if `category == ONES` as opposed to `category == 'ONES'` (or whatever the dummy value is).

This is not an ideal way to solve the exercise, as the provided constants are used as dummies, and the code is rather long and winded. It remains, however, valid, and does have its advantages, such as the lack of repetition in returning 0 that we had in the `lambda` approach.