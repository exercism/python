def square_of_sum(count):
    sum_ = count * (count + 1) / 2
    return sum_ * sum_


def sum_of_squares(count):
    return sum(m * m for m in range(count + 1))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
