# Using Boolean Values as Integers

```python
def score(x_coord, y_coord):
    radius = (x_coord**2 + y_coord**2)
    return (radius<=1)*5 + (radius<=25)*4 +(radius<=100)*1
```