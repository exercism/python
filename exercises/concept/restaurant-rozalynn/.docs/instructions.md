# Instructions


You are the Maître D' of a hotel restaurant.
Your task is to manage the seating arrangements for the dining room according to the number of seats available today, number of reservations, and the "walk in" guests currently waiting to be seated.
For the purposes of this exercise, seating is assigned by first available empty seat.


For this exercise, you have 6 different dining room organization challenges to complete.


## 1. Make Today's Seating Chart

Define the `new_seating_chart(<size=22>)` function that takes a size argument representing the number of seats that will be set in the dining room today.
If no `size` is given, the function should return a seating chart with 22 seats.
Seat values should have a placeholder of `None` to indicate they are available to assign to a guest.


## 2. Arrange Reservations

Define the `arrange_reservations(<guest_names>)` function with 1 parameter for a list of guest names.
This represents the number of people who have places reserved in the dining room today.


This function should return a `dict` seating chart of default size (22 seats), with guests assigned to seats in the order they appear on the reservation list.
All unassigned seats should be set to `None`.
If there are no guests, an "empty" seating chart with all `None` placeholders should be returned.


```python
>>> arrange_reservations(guests=["Walter", "Frank", "Jenny", "Carol", "Alice", "George"])
...
{1: 'Walter', 2: 'Frank', 3: 'Jenny', 4: 'Carol', 5: 'Alice', 6: 'George', 7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: None, 19: None, 20: None, 21: None, 22: None}
```


## 3. Find All the "Empty" Seats

Define the `find_all_available_seats(<seats>)` function that takes 1 parameter (_a seating chart dictionary_) and returns a `list` of seat numbers that are available for guests that are currently waiting.
If a seat is empty, It will be of `None` value in the dictionary. Occupied seats will have the name of the guest.


```python
>>> seats = {1: None, 2: 'Frank', 3: 'Jenny', 4: None, 5: 'Alice', 6: 'George', 7: None, 8: 'Carol', 9: None, 10: None, 11: None, 12: 'Walter'}

>>> find_all_available_seats(seats)
[1,4,7,9,10,11]
```

## 4. Current Empty Seating Capacity

Define the `current_empty_seat_capacity(<seats>)` function that takes 1 parameter - the `dict` of existing seat reservations.
The function should return the total number of seats that are empty.

```python
>>> curr_empty_seat_capacity({1: "Occupied", 2: None, 3: "Occupied"})
1

>>> curr_empty_seat_capacity({1: "Occupied", 2: None, 3: None})
2
```


## 5. Should we wait?

Define the `accommodate_waiting_guests(<seats>, <guests>)` function that takes two parameters.
The first parameter will be a seating chart `dict`.
The second parameter will be a `list` of guests who have "walked in" unexpectedly.
You'll first need to find out how many seats are available and whether or not you can even give the unannounced guests seats at this time.

If you do not have enough seats, return the seating chart `dict` unaltered.

If seats _are_ available, assign the guests places on the seating chart, and return it updated.
**Tip:** You can use previously defined functions to do the calculations for you.


```python
# Guests cannot be accommodated.
>>> starting_reservations = {1: 'Carol', 2: 'Alice', 3: 'George', 4: None, 5: None, 6: None, 7: 'Frank', 8: 'Walter'}
>>> accommodate_guests(starting_reservations, ["Mort", "Suze", "Phillip", "Tony"])
...
{1: 'Carol', 2: 'Alice', 3: 'George', 4: None, 5: None, 6: None, 7: 'Frank', 8: 'Walter'}


# Guests can be accommodated.
>>> starting_reservations = {1: None, 2: None, 3: None, 4: 'Carol', 5: 'Alice', 6: 'George', 7: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: 'Frank', 19:  'Jenny', 20: None, 21: None, 22: 'Walter'}
>>> accommodate_guests(starting_reservations, ["Mort", "Suze", "Phillip", "Tony"])
...
{1: 'Mort', 2: 'Suze', 3: 'Phillip', 4: 'Carol', 5: 'Alice', 6: 'George', 7: 'Tony', 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None, 16: None, 17: None, 18: 'Frank', 19: 'Jenny', 20: None, 21: None, 22: 'Walter'}
```

## 6. Empty Seats

Define the `empty_seats(<seats>, <seat_numbers>)` function that takes two parameters.
The first parameter will be a seating chart dictionary.
The second parameter is a list of seat numbers you need to "free up" or empty -- that is, you need to assign the seat number value to `None`.

Return the `dict` of seats after updating the "to empty" seat values.

```python
>>> empty_seats(seats={1: "Alice", 2: None, 3: "Bob", 4: "George", 5: "Gloria"}, seat_numbers=[5,3,1])
{1: None, 2: None, 3: None, 4: "George", 5: None}
```
