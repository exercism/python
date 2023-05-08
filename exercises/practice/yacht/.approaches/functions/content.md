## Approach: functions
Each bit of functionality for each category can be encoded in a function, and the constant set to that function. 
We use `lambda`s as _all_ the functions can be written in one line.
In `score`, we call the category (as it's now a function) passing in `dice`.

```python
def digits(n):
    return lambda dice: dice.count(n) * n

YACHT = lambda dice: 50 if dice.count(dice[0]) == len(dice) else 0
ONES = digits(1)
TWOS = digits(2)
THREES = digits(3)
FOURS = digits(4)
FIVES = digits(5)
SIXES = digits(6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3] else 0
FOUR_OF_A_KIND = lambda s: 4 * sorted(s)[1] if len(set(s)) < 3 and s.count(s[0]) in (1, 4, 5) else 0
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = sum

def score(dice, category):
    return category(dice)
```
This is a very idiomatic way to solve the exercise, although some one-liners get a little long. 
The [ternary operator][ternary-operator] is crucial in solving the exercise this way. 
Instead of `lambda`s, functions could be created and the constants set to them. 
This will remove the need for one-liners. If interested, read more on [lamdas][lambdas].
```python
def yacht(dice):
    if dice.count(dice[0]) == len(dice):
        return 50
    return 0
YACHT = yacht
# and so on
# or even, though not recommended
def YACHT(dice):
    if dice.count(dice[0]) == len(dice):
        return 50
    return 0
```

Instead of setting each constant in `ONES` through `SIXES` to a separate `lambda`, we create a function that returns a `lambda`, using [closures][closures] transparently.

For `LITTLE_STRAIGHT` and `BIG_STRAIGHT`, we first sort the dice and then check it against the hard-coded value. Another way to solve this would be to check if `sum(d) == 20 and len(set(d)) == 5` (15 in `LITTLE_STRAIGHT`).
In `CHOICE`, `lambda x: sum(x)` is shortened to just `sum`.

The essence of the one-liners in `FULL_HOUSE` and `FOUR_OF_A_KIND` is in creating `set`s to remove the duplicates and checking their lengths. 
`FOUR_OF_A_KIND` is commonly the hardest function to put in one line, and it's valid to declare it in a less complicated function:
```python
FOUR_OF_A_KIND = four_of_a_kind
def four_of_a_kind(x):
    four_times_elements = [dice for dice in set(x) if x.count(dice) >= 4]
    return 4 * four_times_elements[0] if len(four_times_elements) > 0 else 0
```
This approach can be done in one line using the [walrus operator][walrus] which exists in Python since 3.8 (done slightly differently to show the possible variations):
```python
FOUR_OF_A_KIND = lambda dice: four_elem[0] * 4 if (four_elem := [i for i in dice if dice.count(i) >= 4]) else 0
```


[closures]: https://www.programiz.com/python-programming/closure
[ternary-operator]: https://www.tutorialspoint.com/ternary-operator-in-python
[lambdas]: https://www.w3schools.com/python/python_lambda.asp
[walrus]: https://realpython.com/python-walrus-operator/