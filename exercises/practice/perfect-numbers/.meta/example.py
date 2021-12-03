import math

def divisor_generator(number):
    """Returns an unordered list of divisors for n (1 < number).

    :param number: int a positive integer
    :return: list of int divisors
    """

    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0:
            yield index
            if index * index != number:
                yield number // index


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')

    aliquot_sum = sum(divisor_generator(number)) + (1 if number > 1 else 0)

    if aliquot_sum < number:
        return 'deficient'
    elif aliquot_sum == number:
        return 'perfect'
    else:
        return 'abundant'
