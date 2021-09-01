
def new_seating_chart(size=22):
    '''

    :param size: int - number if seats in the seating chart.
    :return: dict - with number of seats specified, and placeholder values.
    '''

    return {number: None for number in range(1, size+1) }


def arrange_reservations(guests=None):
    '''

    :param guest_list: list - list of guest names for reservations.
    :return: dict - Default sized dictionary with guests assigned seats,
             and placeholders for empty seats.
    '''

    seats = new_seating_chart()

    if guests:
        for seat_number in range(1, len(guests)):
            seats[seat_number] = guests[seat_number]
    return seats


def find_all_available_seats(seats):
    '''

    :param seats: dict - seating chart.
    :return: list - list of seat numbers available for reserving..
    '''

    available = []
    for seat_num, value in seats.items():
        if value is None:
            available.append(seat_num)
    return available


def curr_empty_seat_capacity(seats):
    '''

    :param seats: dict - dictionary of reserved seats.
    :return: int - number of seats empty.
    '''

    count = 0
    for value in seats.values():
        if value is None:
            count += 1
    return count


def accommodate_waiting_guests(seats, guests):
    '''

    :param seats: dict - seating chart dictionary.
    :param guests: list - walk-in guests
    :return: dict - updated seating chart with available spaces filled.
    '''

    curr_empty_seats = curr_empty_seat_capacity(seats)
    empty_seat_list = find_all_available_seats(seats)

    if len(guests) > curr_empty_seats:
        return False
    else:
        for index, item in enumerate(guests):
            seats[empty_seat_list[index]] = guests[index]

    return seats


def empty_seats(seats, seat_numbers):
    '''

    :param seats: dict - seating chart dictionary.
    :param seat_numbers: list - list of seat numbers to free up or empty.
    :return: updated seating chart dictionary.
    '''

    for seat in seat_numbers:
        seats[seat] = None

    return seats