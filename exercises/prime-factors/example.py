def factors(value):
    factors = []
    divisor = 2
    while value > 1:
        while value % divisor == 0:
            factors.append(divisor)
            value /= divisor

        divisor += 1

    return factors
