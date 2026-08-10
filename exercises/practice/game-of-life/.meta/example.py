def tick(matrix):
    def count_neighbors(r, c):
        count = 0
        for dr, dc in [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                count += matrix[nr][nc]
        return count

    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    new_matrix = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            neighbors = count_neighbors(r, c)
            current = matrix[r][c]
            state = 0
            if current == 1 and (neighbors == 2 or neighbors == 3):
                state = 1
            elif current == 0 and neighbors == 3:
                state = 1
            new_row.append(state)
        new_matrix.append(new_row)

    return new_matrix
