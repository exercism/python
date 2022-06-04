def rows(row_count, previous_row=[1]):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    elif row_count == 0:
        return []
    temp_row = previous_row + [0]
    new_row = list(map(sum, zip(temp_row, temp_row[::-1])))
    return [previous_row] + rows(row_count - 1, new_row)
