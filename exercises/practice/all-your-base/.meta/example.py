def from_digits(digits, base):
    return sum(n * base ** idx for idx, n in enumerate(reversed(digits)))


def to_digits(number, base_to):
    result = []
    while number > 0:
        result.append(number % base_to)
        number //= base_to
    if result:
        return result[::-1]  # list(reversed(result))
    return [0]


def rebase(from_base, digits, to_base):
    if from_base < 2:
        raise ValueError("input base must be >= 2")

    if to_base < 2:
        raise ValueError("output base must be >= 2")

    if any(True for d in digits if d < 0 or d >= from_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    return to_digits(from_digits(digits, from_base), to_base)
