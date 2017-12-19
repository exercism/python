def divisor_generator(n):
    ''' Returns an unordered list of divisors for n (1 < n). '''
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                yield n // i


def classify(n):
    ''' A perfect number equals the sum of its positive divisors. '''
    if n <= 0:
        raise ValueError("Classification is only possible" +
                         " for positive whole numbers.")

    aliquot_sum = sum(divisor_generator(n)) + (1 if n > 1 else 0)

    if aliquot_sum < n:
        return "deficient"
    elif aliquot_sum == n:
        return "perfect"
    else:
        return "abundant"
