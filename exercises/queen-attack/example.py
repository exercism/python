def board(pos1, pos2):
    validate_position(pos1, pos2)
    x1, y1 = pos1
    x2, y2 = pos2
    b = [['_'] * 8 for i in range(8)]
    b[x1][y1] = 'W'
    b[x2][y2] = 'B'
    return [''.join(r) for r in b]


def can_attack(pos1, pos2):
    validate_position(pos1, pos2)
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x1 - x2 if x1 >= x2 else x2 - x1
    dy = y1 - y2 if y1 >= y2 else y2 - y1
    if dx == dy or dx == 0 or dy == 0:
        return True
    return False


def validate_position(pos1, pos2):
    if any(x < 0 or x > 7 for x in pos1 + pos2):
        raise ValueError('Invalid queen position: queen out of the board')
    if pos1 == pos2:
        raise ValueError('Invalid queen position: both queens in the same '
                         'square: {0}'.format(pos1))
