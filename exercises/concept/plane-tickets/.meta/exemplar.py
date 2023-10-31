"""Functions to automate Conda airlines ticketing system."""

import math

SEATS_IN_ROW = ['A', 'B', 'C', 'D']


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for seat in range(number):
        yield SEATS_IN_ROW[seat % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    number = number + 4 if number >= 13 else number
    letters = generate_seat_letters(number)
    for seat in range(number):
        row_number = math.ceil((seat+1) / 4)
        if row_number != 13:
            yield f'{str(row_number)}{next(letters)}'

    # return (f'{str(row_number)}{next(letters)}' for seat in range(number)
    #         if (row_number := math.ceil((seat+1) / 4)) and row_number != 13)


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    number = len(passengers)
    output = {}
    for passenger, seat_number in zip(passengers, generate_seats(number)):
        output[passenger] = seat_number
    return output

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))
