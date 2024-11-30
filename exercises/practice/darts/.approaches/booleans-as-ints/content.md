# Using Boolean Values as Integers


```python
def score(x_coord, y_coord):
    radius = (x_coord**2 + y_coord**2)
    return (radius<=1)*5 + (radius<=25)*4 + (radius<=100)*1
```


In Python, the [Boolean values `True` and `False` are _subclasses_ of `int`][bools-as-ints] and can be interpreted as `0` (False) and `1` (True) in a mathematical context.
This approach leverages that interpretation by checking which areas the throw falls into and multiplying each Boolean `int` by a scoring multiple.
For example, a throw that lands on the 25 (_or 5 if using `math.sqrt(x**2 + y**2)`_) circle should have a score of 5:

```python
>>> (False)*5 + (True)*4 + (True)*1
5
```


This makes for very compact code and has the added boost of not requiring any `loops` or additional data structures.
However, it is considered bad form to rely on Boolean interpretation.
Instead, the Python documentation recommends an explicit conversion to `int`:


```python
def score(x_coord, y_coord):
    radius = (x_coord**2 + y_coord**2)
    return int(radius<=1)*5 + int(radius<=25)*4 + int(radius<=100)*1
```

Beyond that recommendation, the terseness of this approach might be harder to reason about or decode — especially if a programmer is coming from a programming langauge that does not treat Boolean values as `ints`.
Despite the "radius" variable name, it is also more difficult to relate the scoring "rings" of the Dartboard to the values being checked and calculated in the `return` statement.
If using this code in a larger program, it would be strongly recommended that a docstring be provided to explain the Dartboard rings, scoring rules, and the corresponding scores.

[bools-as-ints]: https://docs.python.org/3/library/stdtypes.html#boolean-type-bool