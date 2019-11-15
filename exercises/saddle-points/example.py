def saddle_points(matrix):
    if not matrix:
        return []
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError('irregular matrix')
    mmax = [max(row) for row in matrix]
    mmin = [min(col) for col in zip(*matrix)]
    points = [{"row": index + 1, "column": col_index + 1}
              for index in range(len(matrix))
              for col_index in range(len(matrix[0]))
              if mmax[index] == mmin[col_index]]

    return points or []
