def find_stop(row, column, word, puzzle):
    directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    for d in directions:
        row_number, column_number = row, column
        for char_number, character in enumerate(word):
            try:
                if puzzle[row_number][column_number] != character:
                    break
            except IndexError:
                break
            if char_number == len(word) - 1:
                return row_number, column_number
            row_number += d[0]
            column_number += d[1]


def search(puzzle, word):
    for row_number, row in enumerate(puzzle):
        for column_number, character in enumerate(row):
            stop = find_stop(row_number, column_number, word, puzzle)
            if stop:
                return (row_number, column_number), stop
