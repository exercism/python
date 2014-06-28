def parse_binary(digits):
    if set(digits) - set('01'):
        raise ValueError("Invalid binary literal: " + digits)
    return sum(int(digit) * 2 ** i
               for (i, digit) in enumerate(reversed(digits)))
