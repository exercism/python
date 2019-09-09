def square(number):
    check_square_input(number)

    return 2 ** (number - 1)


def total(number):
    check_square_input(number)

    return sum(square(n + 1) for n in range(number))


def check_square_input(number):
    if number == 0:
        raise ValueError("Square input of zero is invalid.")
    elif number < 0:
        raise ValueError("Negative square input is invalid.")
    elif number > 64:
        raise ValueError("Square input greater than 64 is invalid.")
