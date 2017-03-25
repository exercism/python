def on_square(square):
    check_square_input(square)
    return 2 ** (square - 1)


def total_after(square):
    check_square_input(square)
    return sum(
        on_square(n + 1) for n
        in range(square)
    )


def check_square_input(square):
    if square == 0:
        raise SquareZeroError
    elif square < 0:
        raise SquareNegativeValueError
    elif square > 64:
        raise SquareGTSixtyFourError


class SquareZeroError(Exception):
    pass


class SquareNegativeValueError(Exception):
    pass


class SquareGTSixtyFourError(Exception):
    pass
