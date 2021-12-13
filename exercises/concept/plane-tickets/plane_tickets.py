"""Plane Tickets Exercise"""

def generate_seats(amount):

    """ Generate a series of seat numbers for airline boarding.

    :param amount: Amount of seats to be generated. (int)
    :return: Generator that yields seat numbers.

    There should be no row 13

    Seat numbers are generated with each row having 4 seats.
    These should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    pass

def assign_seats(passengers):

    """ Assign seats to passengers.

    :param passengers: A list of strings containing names of passengers. (list[str])
    :return: A dictionary type object containing the names of the passengers as keys and seat numbers as values.

    Example output: {"Foo": "1A", "Bar": "1B"}

    """

    pass

def generate_codes(seat_numbers, flight_id):

    """Generate codes for a ticket.

    :param seat_numbers: A list of seat numbers. (list[str])
    :param flight_id: A string containing the flight identification. (str)
    :return: Generator that generates 12 character long strings. (generator[str])

    """
