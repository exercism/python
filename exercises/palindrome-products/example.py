from itertools import groupby


def largest_palindrome(max_factor, min_factor=0):
    return next(palindromes(max_factor, min_factor, True))


def smallest_palindrome(max_factor, min_factor):
    return next(palindromes(max_factor, min_factor))


def palindromes(max_factor, min_factor, reverse=False):
    return (
        (prod, list(zip(*grp))[1])
        for prod, grp in groupby(sorted(
            (
                (a * b, (a, b))
                for a in range(min_factor, max_factor + 1)
                for b in range(min_factor, a + 1)
                if is_palindrome(str(a * b))
            ),
            key=lambda tup: tup[0],
            reverse=reverse
        ), key=lambda tup: tup[0])
    )


def is_palindrome(num_str):
    return num_str == num_str[::-1]
