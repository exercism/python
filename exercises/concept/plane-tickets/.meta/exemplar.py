"""Functions to automate Conda airlines ticketing system."""

import math

SEATS_IN_ROW = ['A', 'B', 'C', 'D']


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    for seat in range(number):
        yield SEATS_IN_ROW[seat % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For exampl: 3C, 3D, 4A, 4B

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

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    number = len(passengers)
    output = {}
    for passenger, seat_number in zip(passengers, generate_seats(number)):
        output[passenger] = seat_number
    return output

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))
