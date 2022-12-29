"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(amount):
    """ Generate a series of seat letters for airline boarding.

    :param amount: int - amount of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated with each row having 4 seats.
    These should be sorted from low to high.

    Example: A, B, C, D

    """

    pass


def generate_seats(amount):
    """ Generate a series of seat numbers for airline boarding.

    :param amount: int - Amount of seats to be generated.
    :return: generator - generator that yields seat numbers.

    There should be no row 13

    Seat numbers are generated with each row having 4 seats.
    These should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    pass

def assign_seats(passengers):
    """ Assign seats to passengers.

    :param passengers: list[str] - A list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Foo": "1A", "Bar": "1B"}

    """

    pass

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identification.
    :return: generator - generator that yields 12 character long strings.

    """
