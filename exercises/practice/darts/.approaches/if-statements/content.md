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
    
# ##OR##

# Checks scores from the edge --> center
def score(x_coord, y_coord):
    distance = math.sqrt(x_coord**2 + y_coord**2)
    
    if distance > 10: return 0
    if 5 < distance <= 10: return 1
    if 1 < distance <= 5: return 5
    if distance <= 1: return 10
```
