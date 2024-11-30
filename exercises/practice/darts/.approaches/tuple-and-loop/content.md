# Use a tuple with a loop

```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = (1, 10), (25, 5), (100, 1), (200, 0)
    
    for distance, points in rules:
        if throw <= distance:
            return points
```

This approach uses a loop to iterate through the _rules_ `tuple`, unpacking each (`distance`, `points`) pair (_For a little more on unpacking, see [Tuple Unpacking Improves Python Code Readability][tuple-unpacking]_).
If the calculated distance of the throw is less than or equal to a given distance, the score for that region is returned.
A `list` of `lists`, a `list` of `tuples`, or a dictionary could be used here to the same effect:

```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = [[1, 10], [25, 5], [100, 1]]
    
    for distance, points in rules:
        if throw <= distance:
            return points
    
    return 0
            
#OR#

def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = [(1, 10), (25, 5), (100, 1), (200, 0)]
    
    for distance, points in rules:
        if throw <= distance:
            return points

#OR#

def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = {1: 10, 25: 5, 100: 1}
    
    for distance, points in rules.items():
        if throw <= distance:
            return points
    
    return 0
```

This approach would work nicely in a scenario where you expect to be adding more scoring "rings", since it is cleaner to edit the data structure than to add additional `if-statements` as you would have to in the [`if-statement` approach][approach-if-statements ].
For the three rings as defined by the current exercise, it is a bit over-engineered to use a data structure + `loop`, and results in a slight (_**very** slight_) slowdown over using `if-statements`.

[tuple-unpacking]: https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/#Unpacking_in_a_for_loop
[approach-if-statements ]: https://exercism.org/tracks/python/exercises/darts/approaches/if-statements
