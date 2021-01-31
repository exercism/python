from math import sqrt


def score(x, y):
    dart_location = sqrt(x * x + y * y)

    if dart_location <= 1.0:
        return 10
    elif dart_location <= 5.0:
        return 5
    elif dart_location <= 10.0:
        return 1
    else:
        return 0
