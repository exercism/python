# Structural Pattern Matching

Another very interesting approach is to use [structural pattern matching][structural pattern matching]. 
Existing in Python since 3.10, this feature allows for neater code than traditional if structures.
 
By and large, we reuse the code from the [if structure approach][approach-if-structure]. 
We set the constants to random values and check for them in the `match` structure. 
`category` is the "subject", and in every other line, we check it against a "pattern". 
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
    match category:
        case 1 | 2 | 3 | 4 | 5 | 6:
            return dice.count(category) * category
        case 'FULL_HOUSE' if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3]:
            return sum(dice)
        case 'FOUR_OF_A_KIND' if dice[0] == dice[3] or dice[1] == dice[4]:
            return dice[1] * 4
        case 'LITTLE_STRAIGHT' if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        case 'BIG_STRAIGHT' if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30 
        case 'YACHT' if all(num == dice[0] for num in dice):
            return 50
        case 'CHOICE':
            return sum(dice)
        case _:
            return 0
```
For the first pattern, we utilize "or patterns", using the `|` operator. 
This checks whether the subject is any of the provided patterns.

In the next five patterns, we check an additional condition along with the pattern matching. 
Finally, we use the wildcard operator `_` to match anything. 
As the compiler checks the patterns (`case`s) in order, `return 0` will be executed if none of the other patterns match. 

Note that the conditions might differ, but the patterns must have hard coded values - that is, you can't say `case ONES ...` instead of `case 1 ...`. 
This will capture the category and lead to unexpected behavior. 

This code is much clenaer than the corresponding `if` structure code.

[structural pattern matching]: https://peps.python.org/pep-0636/
[approach-if-structure]: https://exercism.org/tracks/python/exercises/yacht/approaches/if-structure