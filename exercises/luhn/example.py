class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def addends(self):
        def luhn_transform(n):
            return (2 * n - 9) if (n > 4) else (2 * n)
        old_digits = [int(d) for d in str(self.card_num)]
        return [(luhn_transform(n) if (i % 2 == 0) else n)
                for i, n in enumerate(old_digits, start=len(old_digits) % 2)]

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False
        return self.checksum() % 10 == 0
