from functools import reduce
from operator import mul


def slices(series, size):

    if not size <= len(series):
        raise ValueError('span must be smaller than string length')
    elif not 0 < size:
        raise ValueError('span must not be negative')
    elif not all(item.isdigit() for item in series):
        raise ValueError('digits input must only contain digits')

    numbers = [int(digit) for digit in series]

    return [numbers[idx:idx + size]
            for idx in range(len(numbers) - size + 1)]


def largest_product(series, size):
    if size == 0:
        return 1
    return max(reduce(mul, slice) for slice in slices(series, size))
