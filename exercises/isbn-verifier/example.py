def verify(isbn):
    chars = list(isbn.replace('-', ''))
    if chars and chars[-1] == 'X':
        chars[-1] = '10'
    if not len(chars) == 10 or not all(c.isdigit() for c in chars):
        return False
    indices = list(range(10, 0, -1))
    return sum(int(c) * i for c, i in zip(chars, indices)) % 11 == 0
