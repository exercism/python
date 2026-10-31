# Nested Set Comprehensions with Coordinates

```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    else:
        row_maxima = {(index, eindex, element) for index, row in
                       enumerate(matrix, start=1) for eindex, element in 
                       enumerate(row, start=1) if max(row) == element}


        column_minima = {(eindex, index, element) for index, col in
                          enumerate(zip(*matrix), start=1) for eindex, element in
                          enumerate(col, start=1) if min(col) == element}


    return [{'row': item[0], 'column': item[1]} for 
            item in row_maxima & column_minima]
```


