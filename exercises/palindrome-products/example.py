from __future__ import division
from itertools import chain
from math import log10, floor, ceil


def largest_palindrome(max_factor, min_factor):
    return get_extreme_palindrome_with_factors(max_factor, min_factor,
                                               "largest")


def smallest_palindrome(max_factor, min_factor):
    return get_extreme_palindrome_with_factors(max_factor, min_factor,
                                               "smallest")


def get_extreme_palindrome_with_factors(max_factor, min_factor, extreme):
    palindromes_found = palindromes(max_factor, min_factor,
                                    reverse=(extreme == "largest"))
    factor_pairs = None
    for palin in palindromes_found:
        factor_pairs = ((fact, palin // fact)
                        for fact in range(min_factor, max_factor + 1)
                        if palin % fact == 0)
        factor_pairs = list(pair for pair in factor_pairs
                            if min_factor <= pair[1] <= max_factor)
        if len(factor_pairs) > 0:
            break

    if factor_pairs is None or len(factor_pairs) == 0:
        raise ValueError("no palindrome with factors in the "
                         "range {min_factor} to {max_factor}"
                         .format(min_factor=min_factor,
                                 max_factor=max_factor))

    return (palin, factor_pairs)


def reverse_num(n):
    rev = 0
    while n > 0:
        rev *= 10
        rev += (n % 10)
        n //= 10
    return rev


def num_digits(n):
    return int(floor(log10(n) + 1))


def palindromes(max_factor, min_factor, reverse=False):
    """Generates all palindromes between `min_factor`**2 and max_factor`**2

    If `reverse` is True, will produce the palindromes in decreasing order,
    from `max_factor`**2 down to `min_factor`**2. This is needed for
    `largest_palindrome`, since it won't have to iterate through a
    most of the palindromes just to find the one it needs.
    """
    if max_factor < min_factor:
        raise ValueError("invalid input: min is {min_factor} "
                         "and max is {max_factor}"
                         .format(min_factor=min_factor,
                                 max_factor=max_factor))

    minimum = min_factor ** 2
    maximum = max_factor ** 2

    def gen_palins_of_length(nd, reverse=reverse):
        """Generates all palindromes with `nd` number of digits that are
        within the desired range.

        Again, if `reverse` is True, the palindromes are generated in
        reverse order.
        """
        even_nd = (nd % 2 == 0)

        min_left_half = max(10 ** (int(ceil(nd / 2)) - 1),
                            minimum // (10 ** (nd // 2)))
        max_left_half = min((10 ** int(ceil(nd / 2))) - 1,
                            maximum // (10 ** (nd // 2)))

        current_left_half = min_left_half if not reverse else max_left_half

        def make_palindrome(left_half, even_nd=False):
            right_half = (reverse_num(left_half)
                          if even_nd
                          else reverse_num(left_half // 10))
            return (left_half * (10 ** (nd // 2))) + right_half

        if not reverse:
            while current_left_half <= max_left_half:
                palin = make_palindrome(current_left_half, even_nd)
                if minimum <= palin <= maximum:
                    yield palin
                elif palin > maximum:
                    # since palindromes are generated in increasing order,
                    #   we break out of the loop once we've exceeded the
                    #   maximum value
                    break
                current_left_half += 1
        else:
            while current_left_half >= min_left_half:
                palin = make_palindrome(current_left_half, even_nd)
                if minimum <= palin <= maximum:
                    yield palin
                elif palin < minimum:
                    # since palindromes are generated in decreasing order,
                    #   we break out of the loop once we've gone below the
                    #   minimum value
                    break
                current_left_half -= 1

    min_nd, max_nd = num_digits(minimum), num_digits(maximum)

    lengths = (range(min_nd, max_nd + 1)
               if not reverse
               else range(max_nd, min_nd - 1, -1))

    return chain(*map(gen_palins_of_length, lengths))
