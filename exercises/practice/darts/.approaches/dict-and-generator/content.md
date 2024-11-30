# Use a Dictionary and a Generator Expression

```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = {1: 10, 25: 5, 100: 1, 200: 0}
    
    return max(point for distance, point in 
               rules.items() if throw <= distance)
```


This approach is very similar to the  [tuple and loop][approach-tuple-and-loop] approach, but iterates over [`dict.items()`][dict-items] and writes the `loop` as a [`generator-expression`][generator-expression] inside `max()`.
In cases where the scoring circles overlap, `max()` will return the maximum score available for the throw.
The generator expression inside `max()` is the equivalent of using a `for-loop` and a variable to determine the max score:


```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = {1: 10, 25: 5, 100: 1}
    max_score = 0
    
    for distance, point in rules.items():
        if throw <= distance and point > max_score:
            max_score = point
    return max_score
```


A `list` or `tuple` can also be used in place of `max()`, but then requires an index to return the max score:

```python
def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = {1: 10, 25: 5, 100: 1, 200: 0}
    
    return [point for distance, point in 
               rules.items() if throw <= distance][0] #<-- have to specify index 0.
               
#OR#

def score(x_coord, y_coord):
    throw = x_coord**2 + y_coord**2
    rules = {1: 10, 25: 5, 100: 1, 200: 0}
    
    return tuple(point for distance, point in 
               rules.items() if throw <= distance)[0]
```


This solution can even be reduced to a "one-liner".
However, this is not performant, and is difficult to read:

```python
def score(x_coord, y_coord):    
    return max(point for distance, point in 
               {1: 10, 25: 5, 100: 1, 200: 0}.items() if 
               (x_coord**2 + y_coord**2) <= distance)
```

While all of these variations do pass the tests, they suffer from even more over-engineering/performance caution than the earlier tuple and loop approach (_although for the data in this problem, the performance hit is slight_).
Additionally, the dictionary will take much more space in memory than using a `tuple` of tuples to hold scoring values.
In some circumstances, these variations might also be harder to reason about for those not familiar with `generator-expressions` or `list comprehensions`.


[approach-tuple-and-loop]:  https://exercism.org/tracks/python/exercises/darts/approaches/tuple-and-loop
[dict-items]: https://docs.python.org/3/library/stdtypes.html#dict.items
[generator-expression]: https://dbader.org/blog/python-generator-expressions
