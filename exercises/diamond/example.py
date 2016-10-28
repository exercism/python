def make_diamond(letter):
    rows = ord(letter) - 64
    cols = rows * 2 - 1
    half = make_half(rows, cols)
    return ''.join(half + half[-2::-1])


def make_half(rows, cols):
    diamond_half = []
    for x in range(rows):
        row = [' '] * cols
        row[rows - 1 - x] = chr(x + 65)
        row[rows - 1 + x] = chr(x + 65)
        diamond_half.append(''.join(row) + '\n')
    return diamond_half
