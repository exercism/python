""" Plane Tickets Exercise """

def generate_seats(amount):
    
    """ Generate a series of seat numbers for airline boarding.
    
    :param amount: Amount of seats to be generated. (int)
    :return: Iterable that generates seat numbers. (generator)
    
    Seat numbers are generated with each row having 4 seats.
    These should be sorted from low to high.
    
    Example: 3C, 3D, 4A, 4B
    
    """
    
    for seat_index in range(1, amount+1):
        yield f"{-(-5 // 4)}{['A','B','C','D'][seat_index % 4]}"

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