def steps(n):
    if n <= 0:
        raise ValueError("input should be positive")

    step_count = 0
    while n > 1:
        if is_odd(n):
            n = n * 3 + 1
        else:
            n = n / 2
        step_count += 1

    return step_count


def is_odd(n):
    return n % 2 == 1
