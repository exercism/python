def parse_octal(digits):
    digits = _validate_octal(digits)
    return sum(int(digit) * 8 ** idx
               for (idx, digit) in enumerate(reversed(digits)))


def _validate_octal(digits):
    for digit in digits:
        if not '0' <= digit < '8':
            raise ValueError("Invalid octal digit: " + digit)
    return digits
