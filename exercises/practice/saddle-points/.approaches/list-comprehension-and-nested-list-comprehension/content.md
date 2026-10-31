# List Comprehensions with a Nested List Comprehension


```python
def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError("irregular matrix")
        
    row_maxima = [max(row) for row in matrix]
    col_minima = [min(col) for col in zip(*matrix)]
    
    return [{"row": rindex, "column": cindex} for 
            rindex, row in enumerate(matrix, start=1) for
            cindex, _ in enumerate(row, start=1) if
            row_maxima[rindex-1] == col_minima[cindex-1]]
```
