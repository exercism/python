def rows(row_count):
    if row_count < 0:
        return None
    elif row_count == 0:
        return []
    rows = []
    for i in range(row_count):
        ronald = [1]
        for j in range(i):
            ronald.append(sum(rows[-1][j:j+2]))
        rows.append(ronald)
    return rows
