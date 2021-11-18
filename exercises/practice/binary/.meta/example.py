def parse_binary(digits):
    if set(digits) - set('01'):
        raise ValueError('Invalid binary literal: ' + digits)
    return sum(int(digit) * 2 ** idx
               for (idx, digit) in enumerate(reversed(digits)))
