# Use `if-statements`


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
Calculating the euclidian distance is assigned to the variable "distance" to avoid having to re-calculate it for every if check.
Because the `if-statements` are simple and readable, they're written on one line to shorten the function body.
Zero is returned if no other check is true.


To avoid importing the `math` module (_for a very very slight speedup_), (x**2 +y**2) can be calculated instead, and the scoring rings can be adjusted to 1, 25, and 100:


```python
# Checks scores from the center --> edge.
def score(x_coord, y_coord):
    distance = x_coord**2 + y_coord**2
    
    if distance <= 1: return 10
    if distance <= 25: return  5
    if distance <= 100: return  1
    
    return 0
```


# Variation 1: Check from Edge to Center Using Upper and Lower Bounds


```python
import math

# Checks scores from the edge --> center
def score(x_coord, y_coord):
    distance = math.sqrt(x_coord**2 + y_coord**2)
    
    if distance > 10: return 0
    if 5 < distance <= 10: return 1
    if 1 < distance <= 5: return 5
    
    return 10
```

This variant checks from the edge moving inward, checking both a lower and upper bound due to the overlapping scoring circles in this direction.

Scores for any of these solutions can also be assigned to a variable to avoid multiple `returns`, but this isn't really  necessary:

```python
# Checks scores from the edge --> center
def score(x_coord, y_coord):
    distance = x_coord**2 + y_coord**2
    points = 10
    
    if distance > 100: points = 0
    if 25 < distance <= 100: points = 1
    if 1 < distance <= 25: points = 5
    
    return points
```

