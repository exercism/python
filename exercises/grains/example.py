def square(number):
    if number == 0:
        raise ValueError("Square input of zero is invalid.")
    elif number < 0:
        raise ValueError("Negative square input is invalid.")
    elif number > 64:
        raise ValueError("Square input greater than 64 is invalid.")

    return 2 ** (number - 1)


def total():
    return (2 ** 64) - 1
