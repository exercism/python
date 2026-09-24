# List Comprehensions And a Nested Loop

```python
def saddle_points(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    else:
        row_maxima = [max(row) for row in matrix]
        column_minima = [min(col) for col in zip(*matrix)]
        
        results = []

        for idx, value in enumerate(matrix[0]):
            for index, element in enumerate(matrix):
                if row_maxima[index] == column_minima[idx]:
                    results.append({'row': index+1, 'column': idx+1})
        

    return results or []
```
