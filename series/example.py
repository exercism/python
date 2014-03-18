class Series(object):
    def __init__(self, digits):
        self.digits = digits
        self.numbers = [int(d) for d in digits]

    def slices(self, length):
        if not 1 <= length <= len(self.numbers):
            raise ValueError("Invalid slice length for this series: " +
                             str(length))
        return [self.numbers[i:i + length]
                for i in range(len(self.numbers) - length + 1)]
