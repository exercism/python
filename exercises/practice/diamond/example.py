def rows(letter):
    lines = ord(letter) - 64
    columns = lines * 2 - 1
    half = make_half(lines, columns)
    return half + half[-2::-1]


def make_half(lines, columns):
    diamond_half = []
    for number in range(lines):
        row = [' '] * columns
        row[lines - 1 - number] = chr(number + 65)
        row[lines - 1 + number] = chr(number + 65)
        diamond_half.append(''.join(row))
    return diamond_half
