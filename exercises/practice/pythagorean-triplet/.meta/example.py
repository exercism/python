from math import sqrt, ceil, gcd


def triplets_in_range(start, end):
    for limit in range(4, end + 1, 4):
        for x_pos, y_pos, z_pos in primitive_triplets(limit):
            alpha = x_pos
            beta = y_pos
            gamma = z_pos

            while alpha < start:
                alpha = alpha + x_pos
                beta = beta + y_pos
                gamma = gamma + z_pos

            while gamma <= end:
                yield [alpha, beta, gamma]

                alpha = alpha + x_pos
                beta = beta + y_pos
                gamma = gamma + z_pos


def euclidian_coprimes(limit):
    mean = limit // 2
    for idx in range(1, int(ceil(sqrt(mean)))):
        if mean % idx == 0:
            member = mean // idx
            if (member - idx) % 2 == 1 and gcd(member, idx) == 1:
                yield member, idx


def primitive_triplets(limit):
    """See Euclid's formula
    (https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple)
    for more information
    """
    for member_1, member_2 in euclidian_coprimes(limit):
        calc_1 = member_1 ** 2
        calc_2 = member_2 ** 2

        alpha = calc_1 - calc_2
        beta = 2 * member_1 * member_2
        gamma = calc_1 + calc_2

        if alpha > beta:
            alpha, beta = beta, alpha

        yield alpha, beta, gamma


def triplets_with_sum(number):
    return [
        triplet for triplet
        in triplets_in_range(1, number // 2)
        if sum(triplet) == number
        ]
