class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
        self.checksum = -1
        digits = card_num.replace(' ', '')
        length = len(digits)
        if digits.isdigit() and length > 1:
            self.checksum = 0
            cadence = length % 2
            for idx, digit in enumerate(digits):
                num = int(digit)
                if idx % 2 == cadence:
                    num *= 2
                    if num > 9:
                        num -= 9
                self.checksum += num

    def valid(self):
        return self.checksum % 10 == 0
