class Octal(object):
    def __init__(self, octal_string):
        self.digits = octal_string
        self.is_valid = all('0' <= digit < '8' for digit in octal_string)

    def to_decimal(self):
        if self.is_valid:
            return sum(int(digit) * 8 ** i
                       for (i, digit) in enumerate(reversed(self.digits)))
        return 0
