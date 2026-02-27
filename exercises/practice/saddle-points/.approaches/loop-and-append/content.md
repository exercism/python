# Loop and Append to List


```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    else:
        row_maxima = []
        column_minima = []
        results = []

        for row in matrix:
            row_maxima.append(max(row))

        for column in zip(*matrix):
            column_minima.append(min(column))
            
        for idx, value in enumerate(matrix[0]):
            for index, value in enumerate(matrix):
                if row_maxima[index] == column_minima[idx]:
                    results.append({'row': index+1, 'column': idx+1})

        return results
```

