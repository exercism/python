## Approach: functions
Each bit of functionality for each category can be encoded in a function, and the constant set to that function. 
We use `lambda`s as _all_ the functions can be written in one line.
In `score`, we call the category (as it's now a function) passing in `dice`.

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
FOUR_OF_A_KIND = lambda dice: 4 * sorted(dice)[1] if len(set(dice)) < 3 and dice.count(dice[0]) in (1, 4, 5) else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum

def score(dice, category):
    return category(dice)
```
This is a succinct way to solve the exercise, although some one-liners get a little long. 
If interested, read more on [lamdas][lambdas].

Instead of setting each constant in `ONES` through `SIXES` to a separate function, we create a function `digits` that returns a function, using [closures][closures] transparently.

For `LITTLE_STRAIGHT` and `BIG_STRAIGHT`, we first sort the dice and then check it against the hard-coded value. Another way to solve this would be to check if `sum(d) == 20 and len(set(d)) == 5` (15 in `LITTLE_STRAIGHT`).
In `CHOICE`, `lambda x: sum(x)` is shortened to just `sum`.

The essence of the one-liners in `FULL_HOUSE` and `FOUR_OF_A_KIND` is in creating `set`s to remove the duplicates and checking their lengths.
However, PEP8 doesn't recommend setting variables to `lambda`s for use as functions, so it's better practice to use `def`:
```python
def digits(num):
    return lambda dice: dice.count(num) * num

def YACHT(dice): return 50 if dice.count(dice[0]) == len(dice) else 0
ONES = digits(1)
TWOS = digits(2)
THREES = digits(3)
FOURS = digits(4)
FIVES = digits(5)
SIXES = digits(6)
def FULL_HOUSE(dice): return sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else 0
def FOUR_OF_A_KIND(dice): return 4 * sorted(dice)[1] if len(set(dice)) < 3 and dice.count(dice[0]) in (1, 4, 5) else 0
def LITTLE_STRAIGHT(dice): return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
def BIG_STRAIGHT(dice): return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum

def score(dice, category):
    return category(dice)
```
`FOUR_OF_A_KIND` is commonly the hardest function to encode in one line, so it's good to break it over multiple lines:
```python
def four_of_a_kind(dice):
    four_times_elements = [num for num in set(dice) if dice.count(num) >= 4]
    return 4 * four_times_elements[0] if len(four_times_elements) > 0 else 0
FOUR_OF_A_KIND = four_of_a_kind
```
This approach can be done in one line using the [walrus operator][walrus] which exists in Python since 3.8 (done slightly differently to show the possible variations):
```python
def FOUR_OF_A_KIND(dice): return four_elem[0] * 4 if (four_elem := [num for num in dice if dice.count(num) >= 4]) else 0
```

The [ternary operator][ternary-operator] is crucial in solving the exercise using one line. 
As functions are being used, we can even spread code over multiple lines as it improves readability.
```python
# and so on
# or even, though not recommended
def YACHT(dice):
    if dice.count(dice[0]) == len(dice):
        return 50
    return 0
```

[closures]: https://www.programiz.com/python-programming/closure
[ternary-operator]: https://www.tutorialspoint.com/ternary-operator-in-python
[lambdas]: https://www.w3schools.com/python/python_lambda.asp
[walrus]: https://realpython.com/python-walrus-operator/