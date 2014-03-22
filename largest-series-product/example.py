from functools import reduce
from operator import mul


class Series(object):
    def __init__(self, number_string):
        self.digits = [int(d) for d in number_string]

    def slices(self, length):
        if not 1 <= length <= len(self.digits):
            raise ValueError("Invalid slice length for this series: " +
                             str(length))
        return [self.digits[i:i + length]
                for i in range(len(self.digits) - length + 1)]

    def largest_product(self, length):
        if length == 0:
            return 1
        return max(reduce(mul, slc) for slc in self.slices(length))
