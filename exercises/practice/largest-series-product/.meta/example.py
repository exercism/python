from functools import reduce
from operator import mul


def slices(series, length):

    if not length <= len(series):
        raise ValueError("span must be smaller than string length")
    elif not 0 < length:
        raise ValueError("span must be greater than zero")
    elif not all(item.isdigit() for item in series):
        raise ValueError("digits input must only contain digits")

    numbers = [int(digit) for digit in series]

    return [numbers[i:i + length]
            for i in range(len(numbers) - length + 1)]


def largest_product(series, length):
    if length == 0:
        return 1
    return max(reduce(mul, slc) for slc in slices(series, length))
