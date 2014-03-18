class Octal(object):
    def __init__(self, octal_string):
        self.digits = self.__validate(octal_string)

    def __validate(self, s):
        for char in s:
            if not '0' <= char < '8':
                raise ValueError("Invalid octal digit: " + char)
        return s

    def to_decimal(self):
        return sum(int(digit) * 8 ** i
                   for (i, digit) in enumerate(reversed(self.digits)))
