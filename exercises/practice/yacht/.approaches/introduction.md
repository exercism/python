# Introduction
Yacht in Python can be solved in many ways. The most intuitive approach is to use an `if` structure. More idiomatically, you can create functions and set their names to the constant names.

## General guidance
The main thing in this exercise is to map a category to a function or a standalone piece of code. While map generally reminds us of `dict`s, here the constants in the stub file are global. This indicates that the most idiomatic approach is not using a `dict`. Adhering to the principles of DRY too is important - don't repeat yourself if you can help it, especially in the `ONES` through `SIXES` categories.

## Approach: functions
Each bit of functionality for each category can be encoded in a function, and the constant set to that function. We use `lambda`s as _all_ of the functions can be written in one line. In `score`, we call the category (as it's now a function) passing in `dice`. We use `lambda`s as _all_ of the functions can be written in one line. 
```python
def digits(n):
    return lambda x: x.count(n) * n

YACHT = lambda x: 50 if x.count(x[0]) == len(x) else 0
ONES = digits(1)
TWOS = digits(2)
THREES = digits(3)
FOURS = digits(4)
FIVES = digits(5)
SIXES = digits(6)
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 and x.count(x[0]) in [2, 3] else 0
FOUR_OF_A_KIND = lambda s: 4 * sorted(s)[1] if len(set(s)) < 3 and s.count(s[0]) in (1, 4, 5) else 0
LITTLE_STRAIGHT = lambda x: 30 if sorted(x) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda x: 30 if sorted(x) == [2, 3, 4, 5, 6] else 0
CHOICE = sum

def score(dice, category):
    return category(dice)
```
This is a very idiomatic way to solve the exercise, although some one-liners get a little long. 
The repetitive code is minimized using a seperate function `digits` that returns a function (closure). For more information on this approach, read [this document][approach-functions].

## Approach: if structure
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
Read more on this approach [here][approach-if-structure].

[approach-functions]: https://exercism.org/tracks/python/exercises/yacht/approaches/functions
[approach-if-structure]: https://exercism.org/tracks/python/exercises/yacht/approaches/if-structure
