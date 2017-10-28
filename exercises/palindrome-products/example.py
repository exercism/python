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

    return (palin, set(map(frozenset, factor_pairs)))


def palindromes(max_factor, min_factor, reverse=False):
    if max_factor < min_factor:
        raise ValueError("invalid input: min is {min_factor} "
                         "and max is {max_factor}"
                         .format(min_factor=min_factor,
                                 max_factor=max_factor))

    if reverse:
        return (p for p in range(max_factor ** 2, (min_factor ** 2) - 1, -1)
                if is_palindrome(p))
    else:
        return (p for p in range(min_factor ** 2, (max_factor ** 2) + 1)
                if is_palindrome(p))


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
