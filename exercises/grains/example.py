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
        raise ValueError("Square input of zero is invalid.")
    elif square < 0:
        raise ValueError("Negative square input is invalid.")
    elif square > 64:
        raise ValueError("Square input greater than 64 is invalid.")
