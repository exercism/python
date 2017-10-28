def largest_palindrome(max_factor, min_factor=0):
    return max(palindromes(max_factor, min_factor), key=lambda tup: tup[0])


def smallest_palindrome(max_factor, min_factor):
    return min(palindromes(max_factor, min_factor), key=lambda tup: tup[0])


def palindromes(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError("invalid input: min is {min_factor}"
                         "and max is {max_factor}"
                         .format(min_factor=min_factor,
                                 max_factor=max_factor))

    palindromes_found = [(a * b, (a, b))
                         for a in range(min_factor, max_factor + 1)
                         for b in range(min_factor, a + 1)
                         if is_palindrome(a * b)]

    if len(palindromes_found) == 0:
        raise ValueError("no palindrome with factors in the "
                         "range {min_factor} to {max_factor}"
                         .format(min_factor=min_factor,
                                 max_factor=max_factor))

    return palindromes_found


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
