"""Functions to automate Conda airlines ticketing system."""

import math

SEATS_IN_ROW = ['A', 'B', 'C', 'D']


def generate_seat_letters(amount):
    """Generate a series of seat letters for airline boarding.

    :param amount: int - amount of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for seat in range(amount):
        yield SEATS_IN_ROW[seat % 4]


def generate_seats(amount):
    """Generate a series of seat numbers for airline boarding.

    :param amount: int - Amount of seats to be generated.
    :return: generator - generator that yields seat numbers.

    There should be no row 13

    Seat numbers are generated with each row having 4 seats.
    These should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    amount = amount + 4 if amount >= 13 else amount
    letters = generate_seat_letters(amount)
    for seat in range(amount):
        row_number = math.ceil((seat+1) / 4)
        if row_number != 13:
            yield f'{str(row_number)}{next(letters)}'

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - A list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Foo": "1A", "Bar": "1B"}

    """

    amount = len(passengers)
    output = {}
    for passenger, seat_number in zip(passengers, generate_seats(amount)):
        output[passenger] = seat_number
    return output

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identification.
    :return: generator - generator that yields 12 character long strings.

    """

    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))
