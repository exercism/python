def new_seating_chart(size=22):
    seats = dict()
    for number in range(1, size+1):
        seats[number] = None
    return seats

def arrange_reservations(guests=None):
    if guests is None:
        return new_seating_chart()
    else:
        seats = new_seating_chart()
        for seat_number in range(1, len(guests)):
            seats[seat_number] = guests[seat_number]
    return seats

def find_all_available_seats(seats):
    available = []
    for seat_num, value in seats.items():
        if value is None:
            available.append(seat_num)
    return available

def curr_empty_seat_capacity(seats):
    count = 0
    for value in seats.values():
        if value is None:
            count += 1
    return count

def accommodate_waiting_guests(seats, guests):
    curr_empty_seats = curr_empty_seat_capacity(seats)
    empty_seat_list = find_all_available_seats(seats)
    if len(guests) > curr_empty_seats:
        return False
    else:
        for index in range(len(guests)):
            seats[empty_seat_list[index]] = guests[index]
    return seats

def empty_seats(seats, seat_numbers):
   for seat in seat_numbers:
      seats[seat] = None
   return seats