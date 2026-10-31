# Nested List Comprehensions with Coordinates

```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(item) != len(matrix[0]) for item in matrix):
        raise ValueError("irregular matrix")
    
    else:
        row_maxima = [(index, eindex, element) for index, row in
                       enumerate(matrix) for eindex, element in 
                       enumerate(row) if max(row) == element]


        col_minima = [(eindex, index, element) for index, col in
                       enumerate(zip(*matrix)) for eindex, element in
                       enumerate(col) if min(col) == element]


    return [{'row': item[0]+1, 'column': item[1]+1} for 
            item in col_minima if item in row_maxima]
```
