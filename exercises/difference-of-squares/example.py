def square_of_sum(number):
    sum_ = number * (number + 1) / 2
    return sum_ * sum_


def sum_of_squares(number):
    numerator = number * (number + 1) * (2 * number + 1)
    return numerator / 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
