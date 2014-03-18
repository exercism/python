def square_of_sum(n):
    sum_ = n * (n + 1) / 2
    return sum_ * sum_


def sum_of_squares(n):
    return sum(m * m for m in range(n + 1))


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
