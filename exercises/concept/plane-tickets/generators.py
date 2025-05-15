"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    seat_letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield seat_letters[i % 4]


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

    generated_seats = []
    seat_letters = ["A", "B", "C", "D"]
    row = 1
    
    while len(generated_seats) < number:
        if row == 13:
            row += 1
            continue
            
        for letter in seat_letters:
            seat = str(row) + letter
            generated_seats.append(seat)
            if len(generated_seats) == number:
                yield seat
                break
            else:
                yield seat
                
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    n = len(passengers)
    passengers_seats = {}
    seats = list(generate_seats(n))
    
    for index in range(len(passengers)):
        passengers_seats[passengers[index]] = seats[index]
        
    return passengers_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        _code = seat_number + flight_id
        remaining_len_to_complete = 12 - len(_code)

        for n in range(remaining_len_to_complete):
            _code += "0"
        
        yield _code
