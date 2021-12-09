"""Plane Tickets Exercise"""

import math

SEATS_IN_ROW = ['A', 'B', 'C', 'D']

def generate_seats(amount):

    """Generate a series of seat numbers for airline boarding.

    :param amount: Amount of seats to be generated. (int)
    :return: Generator that generates seat numbers. (generator)

    There should be no row 13

    Seat numbers are generated with each row having 4 seats.
    These should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    amount = amount + 4 if amount >= 13 else amount

    for seat in range(amount):
        row_number = math.ceil((seat+1) / 4)
        if row_number != 13:
            seat_letter = SEATS_IN_ROW[seat % 4]
            yield f'{str(row_number)}{seat_letter}'

def assign_seats(passengers):

    """Assign seats to passenger.

    :param passengers: A list of strings containing names of passengers. (list[str])
    :return: A dictionary type object containing the names of the passengers as keys and seat numbers as values.

    Example output: {"Foo": "1A", "Bar": "1B"}

    """

    amount = len(passengers)
    output = {}
    for passenger, seat_number in zip(passengers, generate_seats(amount)):
        output[passenger] = seat_number
    return output

def generate_codes(seat_numbers, flight_id):

    """Generate codes for a ticket.

    :param seat_numbers: A list of seat numbers. (list[str])
    :param flight_id: A string containing the flight identification. (str)
    :return: Generator that generates 12 character long strings. (generator[str])

    """

    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))
