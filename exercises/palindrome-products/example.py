def largest_palindrome(max_factor, min_factor=0):
    if max_factor < min_factor:
        raise ValueError("invalid input: min is {min} and max is {max}"
                         .format(min=min_factor, max=max_factor))

    palindromes_found = palindromes(max_factor, min_factor)

    if len(palindromes_found) == 0:
        raise ValueError("no palindrome with factors in the "
                         "range {min} to {max}"
                         .format(min=min_factor, max=max_factor))

    return max(palindromes_found, key=lambda tup: tup[0])


def smallest_palindrome(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError("invalid input: min is {min} and max is {max}"
                         .format(min=min_factor, max=max_factor))

    palindromes_found = palindromes(max_factor, min_factor)

    if len(palindromes_found) == 0:
        raise ValueError("no palindrome with factors in the "
                         "range {min} to {max}"
                         .format(min=min_factor, max=max_factor))

    return min(palindromes_found, key=lambda tup: tup[0])


def palindromes(max_factor, min_factor):
    return [(a * b, (a, b))
            for a in range(min_factor, max_factor + 1)
            for b in range(min_factor, a + 1)
            if is_palindrome(a * b)]


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]
