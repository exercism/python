# If structure

The constants here can be set to random, null, or numeric values, and an `if` structure inside the `score` function can determine the code to be executed. 
 
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
Note that the code inside the `if` statements themselves can differ, but the key idea here is to use `if` and `elif` to branch out the code, and return `0` at the end if nothing else has been returned. 
The `if` condition itself can be different, with people commonly checking if `category == ONES` as opposed to `category == 'ONES'` (or whatever the dummy value is).

This may not be an ideal way to solve the exercise, as the code is rather long and convoluted.
However, it is a valid (_and fast_) solution.
Using [structural pattern matching][structural pattern matching], introduced in Python 3.10, could shorten and clarify the code in this situation.
Pulling some logic out of the `score` function and into additional "helper" functions could also help.

[structural pattern matching]: https://peps.python.org/pep-0636/