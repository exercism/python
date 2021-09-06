def new_seating_chart(size=22):
    """Create a new seating chart.

    :param size: int - number if seats in the seating chart. Default is 22.
    :return: dict - with number of seats specified, and placeholder values.
    """

    pass


def arrange_reservations(guest_list):
    """Assign guests to seats.

    :param guest_list: list - list of guest names for reservations.
    :return: dict - Default sized dictionary with guests assigned seats,
             and placeholders for empty seats.
    """

    pass


def find_all_available_seats(seats):
    """Find and return seat numbers that are unassigned.

    :param seats: dict - seating chart.
    :return: list - list of seat numbers available for reserving..
    """

    pass


def current_empty_seat_capacity(seats):
    """Find the number of seats that are currently empty.

    :param seats: dict - dictionary of reserved seats.
    :return: int - number of seats empty.
    """

    pass


def accommodate_waiting_guests(seats, guests):
    """Asses if guest can be accommodated.  Update seating if they can be.

    :param seats: dict - seating chart dictionary.
    :param guests: list - walk-in guests
    :return: dict - updated seating chart with available spaces filled.
    """

    pass


def empty_seats(seats, seat_numbers):
    """Empty listed seats of their previous reservations.

    :param seats: dict - seating chart dictionary.
    :param seat_numbers: list - list of seat numbers to free up or empty.
    :return: updated seating chart dictionary.
    """

    pass
