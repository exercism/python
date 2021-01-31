def rows(row_count):
    if row_count < 0:
        return None
    elif row_count == 0:
        return []
    r = []
    for i in range(row_count):
        rn = [1]
        for j in range(i):
            rn.append(sum(r[-1][j:j+2]))
        r.append(rn)
    return r
