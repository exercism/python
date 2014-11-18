class SumOfMultiples(object):

    def __init__(self, *args):
        self.numbers = args or (3, 5)

    def to(self, limit):
        return sum(n
                   for n in range(limit)
                   if self.is_multiple(n))

    def is_multiple(self, m):
        return any(n != 0 and m % n == 0
                   for n in self.numbers)
