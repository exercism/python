def rows(row_count):
    if row_count < 0:
        return None
    elif row_count == 0:
        return []
    row_list = []
    for idx in range(row_count):
        ronald = [1]
        for edx in range(idx):
            ronald.append(sum(row_list[-1][edx:edx+2]))
        row_list.append(ronald)
    return row_list
