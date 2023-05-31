## Approach: Using Lambdas with Functions
Each bit of functionality for each category can be encoded in an anonymous function (otherwise known as a [`lambda` expression][lambda] or lambda form), and the constant name set to that function.

In `score`, we call the category (as it now points to a function) passing in `dice` as an argument.

```python
def digits(num):
    return lambda dice: dice.count(num) * num

YACHT = lambda dice: 50 if len(set(dice)) ==  1 else 0
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


Instead of setting each constant in `ONES` through `SIXES` to a separate function, we create a function `digits` that returns a function, using [closures][closures] transparently.

For `LITTLE_STRAIGHT` and `BIG_STRAIGHT`, we first sort the dice and then check it against the hard-coded value. 
Another way to solve this would be to check if `sum(dice) == 20 and len(set(dice)) == 5` (15 in `LITTLE_STRAIGHT`).
In `CHOICE`, `lambda number : sum(number)` is shortened to just `sum`.

In `FULL_HOUSE`, we create a `set` to remove the duplicates and check the set's length along with the individual counts. 
For `FOUR_OF_A_KIND`, we check if the first and the fourth element are the same or the second and the last element are the same - if so, there are (at least) four of the same number in the array. 

This solution is a succinct way to solve the exercise, although some of the one-liners can get a little long and hard to read. 
Additionally, [PEP8][pep8] does not recommend assigning constant or variable names to `lambda` expressions, so it is a better practice to use `def`:
```python
def digits(num):
    return lambda dice: dice.count(num) * num

def YACHT(dice): return 50 if len(set(dice)) ==  1 else 0
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

As you can see from the examples, the [ternary operator][ternary-operator] (_or ternary form_) is crucial in solving the exercise using one liners.  
As functions are being used, it might be a better strategy to spread the code over multiple lines to improve readability.
```python
def YACHT(dice):
    if dice.count(dice[0]) == len(dice):
        return 50
    return 0
```

[closures]: https://www.programiz.com/python-programming/closure
[ternary-operator]: https://www.tutorialspoint.com/ternary-operator-in-python
[lambda]: https://docs.python.org/3/howto/functional.html?highlight=lambda#small-functions-and-the-lambda-expression    
[pep8]: https://peps.python.org/pep-0008/