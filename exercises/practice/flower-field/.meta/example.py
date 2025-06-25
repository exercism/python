def annotate(garden):
    if not garden:
        return []
    verify_board(garden)
    row_len = len(garden[0])
    col_len = len(garden)
    board = [list(row) for row in garden]

    for index1 in range(col_len):
        for index2 in range(row_len):
            if board[index1][index2] != ' ':
                continue

            low = max(index2 - 1, 0)
            high = min(index2 + 2, row_len + 2)
            counts = garden[index1][low:high].count('*')

            if index1 > 0:
                counts += garden[index1 - 1][low:high].count('*')
            if index1 < col_len - 1:
                counts += garden[index1 + 1][low:high].count('*')
            if counts == 0:
                continue

            board[index1][index2] = str(counts)
    return [''.join(row) for row in board]


def verify_board(garden):
    # Rows with different lengths
    row_len = len(garden[0])
    if not all(len(row) == row_len for row in garden):
        raise ValueError('The board is invalid with current input.')

    # Unknown character in board
    character_set = set()
    for row in garden:
        character_set.update(row)
    if character_set - set(' *'):
        raise ValueError('The board is invalid with current input.')
