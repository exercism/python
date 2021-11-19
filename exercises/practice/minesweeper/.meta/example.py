def annotate(minefield):
    if not minefield:
        return []
    verify_board(minefield)
    row_len = len(minefield[0])
    col_len = len(minefield)
    board = [list(row) for row in minefield]

    for index1 in range(col_len):
        for index2 in range(row_len):
            if board[index1][index2] != ' ':
                continue

            low = max(index2 - 1, 0)
            high = min(index2 + 2, row_len + 2)
            counts = minefield[index1][low:high].count('*')

            if index1 > 0:
                counts += minefield[index1 - 1][low:high].count('*')
            if index1 < col_len - 1:
                counts += minefield[index1 + 1][low:high].count('*')
            if counts == 0:
                continue

            board[index1][index2] = str(counts)
    return [''.join(row) for row in board]


def verify_board(minefield):
    # Rows with different lengths
    row_len = len(minefield[0])
    if not all(len(row) == row_len for row in minefield):
        raise ValueError('The board is invalid with current input.')

    # Unknown character in board
    character_set = set()
    for row in minefield:
        character_set.update(row)
    if character_set - set(' *'):
        raise ValueError('The board is invalid with current input.')
