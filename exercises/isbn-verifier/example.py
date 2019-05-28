def is_valid(isbn):
    chars = list(isbn.replace('-', ''))
    if chars and chars[-1] == 'X':
        chars[-1] = '10'
    if not len(chars) == 10 or not all(char.isdigit() for char in chars):
        return False
    indices = list(range(10, 0, -1))
    return sum(int(char) * idx for char, idx in zip(chars, indices)) % 11 == 0
