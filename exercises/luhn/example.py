class Luhn(object):
    def __init__(self, number):
        self.number = number

    def addends(self):
        def luhn_transform(n):
            return (2 * n - 9) if (n > 4) else (2 * n)
        old_digits = [int(d) for d in str(self.number)]
        return [(luhn_transform(n) if (i % 2 == 0) else n)
                for i, n in enumerate(old_digits, start=len(old_digits) % 2)]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0

    @staticmethod
    def create(n):
        diff = (10 - Luhn(n * 10).checksum()) % 10
        return 10 * n + diff
