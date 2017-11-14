def board(inp):
    if(inp == []):
        return []
    verify_board(inp)
    rowlen = len(inp[0])
    collen = len(inp)
    b = [list(r) for r in inp]
    for i1 in range(collen):
        for i2 in range(rowlen):
            if b[i1][i2] != ' ':
                continue
            low = max(i2 - 1, 0)
            high = min(i2 + 2, rowlen + 2)
            cnt = inp[i1][low:high].count('*')
            if(i1 > 0):
                cnt += inp[i1 - 1][low:high].count('*')
            if(i1 < collen - 1):
                cnt += inp[i1 + 1][low:high].count('*')
            if cnt == 0:
                continue
            b[i1][i2] = str(cnt)
    return ["".join(r) for r in b]


def verify_board(inp):
    # Rows with different lengths
    rowlen = len(inp[0])
    if not all(len(r) == rowlen for r in inp):
        raise ValueError("Invalid board")
    # Unknown character in board
    cset = set()
    for r in inp:
        cset.update(r)
    if cset - set(' *'):
        raise ValueError("Invalid board")
