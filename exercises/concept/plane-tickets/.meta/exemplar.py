""" Plane Tickets Exercise """

def generate_seats(amount):
    
    """ Generate a series of seat numbers for airline boarding.
    
    :param amount: Amount of seats to be generated. (int)
    :return: Iterable that generates seat numbers. (generator)
    
    Seat numbers are generated with each row having 4 seats.
    These should be sorted from low to high.
    
    Example: 3C, 3D, 4A, 4B
    
    """
    
    # Could also be solved in two lines:
    # for seat_index in range(amount):
    #   yield f"{-(-(seat_index+1) // 4)}{['A','B','C','D'][seat_index % 4]}"
    
    SEATS_IN_ROW = ["A", "B", "C", "D"]
    
    for seat in range(amount):
        seat_letter = SEATS_IN_ROW[seat % 4]
        row_number = -(-(seat+1) // 4)          # ? Ceiling division; might be too advanced for students?
        yield str(row_number)+str(seat_letter)

def assign_seats(passengers):
    
    """ Assign seats to passenger.
    
    :param passengers: A list of strings containing names of passengers. (list[str])
    :return: A dictionary type object containing the names of the passengers as keys and seat numbers as values.

    Example output: {"Foo": "1A", "Bar": "1B"}
    
    """

    pass

if __name__ == "__main__":
    for x in generate_seats(10):
        print(x)