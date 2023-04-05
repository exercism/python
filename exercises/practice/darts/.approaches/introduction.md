# Introduction


There are multiple  Pythonic ways to solve the Darts exercise.
Among them are:

- Using if statements
- Using a tuple (or list or dict) and a for loop
- Using a dict (or tuple or list) and a `generator-expression`
- Using boolean values as ints
- Using a dict and dict.get()
- Using `match/case` (_Python 3.10+ only_)



## General guidance

The goal of the Darts exercise is to score a single toss in a Darts game.
The scoring areas are _concentric circles_, so boundary values need to be checked in order to properly score a toss.
The key is to determine how far from the center the dart lands (_by calculating sqrt(x**2 + y**2), or a variation_) and then determine what scoring ring it falls into.


**_Order matters_** - each bigger target circle contains all the smaller circles, so the most straightforward solution is to check the smallest circle first.
Otherwise, you must box your scoring by checking both a _lower bound_ and an _upper bound_.


Darts that fall on a _boundary_ are scored based on the area below the line (_closer to center_).


## Approach: Using `if` statements


```python
import math

# Checks scores from the center --> edge.
def score(x_coord, y_coord):
    distance = math.sqrt(x_coord**2 + y_coord**2)
    
    if distance <= 1: return 10
    if distance <= 5: return  5
    if distance <= 10: return  1
    
    return 0

  ###OR##

# Checks scores from the edge --> center
def score(x_coord, y_coord):
    distance = math.sqrt(x_coord**2 + y_coord**2)
    
    if distance > 10: return 0
    if 5 < distance <= 10: return 1
    if 1 < distance <= 5: return 5
    if distance <= 1: return 10
```


This approach uses [concept:python/conditionals]() to check the boundaries for each scoring ring, returning the corresponding score.
Because the `if-statements` are simple and readable, they're written on one line to shorten the function body.

One variant checks from the center, moving outward.
Zero is returned if no other if check is true.

The other variant checks from the edge, moving inward, and includes an explicit check for the zero case.
To avoid importing the `math` module, (x**2 +y**2) can be calculated instead, and the scoring rings can be adjusted to 1, 25, and 100.

For more details, see the [if statements][approach-if-statements] approach.


## Approach: Using a `tuple` and a  `loop`

```python
def score(x_coord, y_coord):
    distance = x_coord**2 + y_coord**2
    rules = (1.0, 10), (25.0, 5), (100.0, 1), (200.0, 0)
    
    for distance, point in rules:
        if length <= distance:
            return point
```


This approach loops through the _rules_ `tuple`, unpacking each `distance` and corresponding`score`.
If the calculated distance of the toss is less than or equal to a given distance, the point score is returned.
For more details, see the [tuple and loop][approach-tuple-and-loop] approach.


## Approach: Using a `dict` with a `generator-expression`

```python
def score(x_coord, y_coord):
    length = x_coord**2 + y_coord**2
    rules = {1.0: 10, 25.0: 5, 100.0: 1, 200: 0}
    score = max(point for 
                distance, point in 
                rules.items() if length <= distance)

    return score
```

This approach is very similar to the  [tuple and loop][approach-tuple-and-loop] approach, but iterates over [`dict.items()`][dict-items],  and writes the `loop` as a [`generator-expression`][generator-expression] inside `max()`.
For more information, see the [dict with generator-expression][approach-dict-with-generator-expression]  approach.


## Approach: Using Boolean Values as Integers

```python
def score(x_coord, y_coord):
    radius = (x_coord**2 + y_coord**2)
    return (radius<=1)*5 + (radius<=25)*4 +(radius<=100)*1
```


This approach exploits Boolean values as integers.

In Python, the boolean values `True` and `False` are _subclasses_ of `int` , and can be interpreted as `0` (False) and `1` (True) in a mathematical context.

For more information, see the [boolean values as integers][approach-boolean-values-as-integers]  approach.


## Approach: Using a `Dictionary` and `dict.get()`

```python
def score(x_coord, y_coord):
    point = (x_coord**2 + y_coord**2)
    scores = {
        point <= 100: 1,
        point <= 25: 5,
        point <= 1: 10
    }
    
    return scores.get(True, 0)
```

This approach uses a dictionary to hold the distance --> scoring mappings and `dict.get()` to retrieve the correct points value.
For more details, read the [`Dictionary and dict.get()`][approach-dict-and-dict-get]  approach.


## Approach:  Using `match/case` (structural pattern matching)

```python
from math import hypot, ceil


def score(x, y):
    match ceil(hypot(x, y)):
        case 0 | 1: return 10
        case 2 | 3 | 4 | 5: return 5
        case 6 | 7 | 8 | 9 | 10: return 1
        case _: return 0

```


This approach uses Python 3.10's [`structural pattern matching`][structural-pattern-matching], with return values on the same line as `case`.
A fallthrough case (`_`) is used if the dart throw is outside the outer circle of the target (_greater than 10_).
For more details, see the [structural pattern matching][approach-struct-pattern-matching] approach.


## Which approach to use?

Many of these approaches are a matter of personal preference - there aren't significant memory or performance differences.
That being said, ___ is the fastest and __ the slowest for the test data.

# TODO: add in the details here!

To compare the performance and other tradeoffs of the approaches, take a look at the [Performance article][article-performance].


[approach-boolean-values-as-integers]:  https://exercism.org/tracks/python/exercises/darts/approaches/boolean-values-as-integers
[approach-dict-and-dict-get]:  https://exercism.org/tracks/python/exercises/darts/approaches/dict-and-dict-get
[approach-dict-with-generator-expression]:  https://exercism.org/tracks/python/exercises/darts/approaches/dict-with-gnerator-expresson
[approach-if-statements ]:  https://exercism.org/tracks/python/exercises/darts/approaches/if-statements
[approach-struct-pattern-matching]:  https://exercism.org/tracks/python/exercises/darts/approaches/struct-pattern-matching
[approach-tuple-and-loop]:  https://exercism.org/tracks/python/exercises/darts/approaches/tuple-and-loop
[article-performance]:https://exercism.org/tracks/python/exercises/darts/articles/performance
[structural-pattern-matching]: https://peps.python.org/pep-0636/
[dict-items]: https://docs.python.org/3/library/stdtypes.html#dict.items
[generator-expression]: https://dbader.org/blog/python-generator-expressions
