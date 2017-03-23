def board(inp):
    verify_board(inp)
    rowlen = len(inp[0])
    collen = len(inp)
    b = [list(r) for r in inp]
    for i1 in range(collen):
        for i2 in range(rowlen):
            if b[i1][i2] != ' ':
                continue
            cnt = inp[i1 - 1][i2 - 1:i2 + 2].count('*') + \
                inp[i1][i2 - 1:i2 + 2].count('*') + \
                inp[i1 + 1][i2 - 1:i2 + 2].count('*')
            if cnt == 0:
                continue
            b[i1][i2] = str(cnt)
    return ["".join(r) for r in b]


def verify_board(inp):
    # Null board or a null row
    if not inp or not all(r for r in inp):
        raise ValueError("Invalid board")
    # Rows with different lengths
    rowlen = len(inp[0])
    collen = len(inp)
    if not all(len(r) == rowlen for r in inp):
        raise ValueError("Invalid board")
    # Unknown character in board
    cset = set()
    for r in inp:
        cset.update(r)
    if cset - set('+- *|'):
        raise ValueError("Invalid board")
    # Borders not as expected
    if any(inp[i1] != '+' + '-' * (rowlen - 2) + '+'
           for i1 in [0, -1]) or any(inp[i1][i2] != '|'
                                     for i1 in range(1, collen - 1)
                                     for i2 in [0, -1]):
        raise ValueError("Invalid board")
