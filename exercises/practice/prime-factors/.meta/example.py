def factors(value):
    factor_list = []
    divisor = 2
    while value > 1:
        while value % divisor == 0:
            factor_list.append(divisor)
            value /= divisor

        divisor += 1

    return factor_list
