def parse_octal(digits):
    digits = _validate_octal(digits)
    return sum(int(digit) * 8 ** i
               for (i, digit) in enumerate(reversed(digits)))


def _validate_octal(digits):
    for d in digits:
        if not '0' <= d < '8':
            raise ValueError("Invalid octal digit: " + d)
    return digits
