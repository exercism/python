# Introduction


There are multiple  Pythonic ways to solve the Darts exercise.
Among them are:

- Using `if-statements`
- Using a `tuple` (or `list` or `dict`) and a `for-loop`
- Using a `dict` (or `tuple` or `list`) and a `generator-expression`
- Using `boolean` values as `ints`
- Using a `dict` and `dict.get()`
- Using `match/case` (_Python 3.10+ only_)

<br>

## General guidance

The goal of the Darts exercise is to score a single throw in a Darts game.
The scoring areas are _concentric circles_, so boundary values need to be checked in order to properly score a throw.
The key is to determine how far from the center the dart lands (_by calculating sqrt(x**2 + y**2), or a variation_) and then determine what scoring ring it falls into.


**_Order matters_** - each bigger target circle contains all the smaller circles, so the most straightforward solution is to check the smallest circle first.
Otherwise, you must box your scoring by checking both a _lower bound_ and an _upper bound_.


Darts that fall on a _boundary_ are scored based on the area below the line (_closer to center_), so checking `<=` or `>=` is advised.


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
```


This approach uses [concept:python/conditionals]() to check the boundaries for each scoring ring, returning the corresponding score.
For more details, see the [if statements][approach-if-statements] approach.


## Approach: Using a `tuple` and a  `loop`

```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = (1, 10), (25, 5), (100, 1), (200, 0)
    
    for distance, points in rules:
        if throw <= distance:
            return points
```


This approach uses a loop to iterate through the _rules_ `tuple`, unpacking each `distance` and corresponding`score`.
For more details, see the [tuple and loop][approach-tuple-and-loop] approach.


## Approach: Using a `dict` with a `generator-expression`

```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = {1: 10, 25: 5, 100: 1, 200: 0}
    
    return max(point for distance, point in 
               rules.items() if throw <= distance)
```

This approach is very similar to the  [tuple and loop][approach-tuple-and-loop] approach, but iterates over [`dict.items()`][dict-items].
For more information, see the [dict with generator-expression][approach-dict-with-generator-expression]  approach.


## Approach: Using Boolean Values as Integers

```python
def score(x_coord, y_coord):
    radius = (x_coord**2 + y_coord**2)
    return (radius<=1)*5 + (radius<=25)*4 +(radius<=100)*1
```


This approach exploits the fact that Boolean values are an integer subtype in Python.
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


This approach uses `Python 3.10`'s structural pattern matching with `return` values on the same line as `case`.
A fallthrough case (`_`) is used if the dart throw is outside the outer circle of the target (_greater than 10_).
For more details, see the [structural pattern matching][approach-struct-pattern-matching] approach.


## Which approach to use?

Many of these approaches are a matter of personal preference - there are not significant memory or performance differences.
Although a strong argument could be made for simplicity and clarity — many listed solutions (_while interesting_) are harder to reason about or are over-engineered for the current scope of the exercise.

[approach-boolean-values-as-integers]:  https://exercism.org/tracks/python/exercises/darts/approaches/boolean-values-as-integers
[approach-dict-and-dict-get]:  https://exercism.org/tracks/python/exercises/darts/approaches/dict-and-dict-get
[approach-dict-with-generator-expression]:  https://exercism.org/tracks/python/exercises/darts/approaches/dict-and-generator
[approach-if-statements ]:  https://exercism.org/tracks/python/exercises/darts/approaches/if-statements
[approach-struct-pattern-matching]:  https://exercism.org/tracks/python/exercises/darts/approaches/struct-pattern-matching
[approach-tuple-and-loop]:  https://exercism.org/tracks/python/exercises/darts/approaches/tuple-and-loop
[dict-items]: https://docs.python.org/3/library/stdtypes.html#dict.items
