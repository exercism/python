# Hints

## General

- In Python, `None` is frequently used as a placeholder to represent the **absence of a value** for a variable, object, or argument.

## 1. Make New Seating Chart

Remember, you will need to create an empty dictionary first. Next, fill the dictionary _keys_ with however many seats are available and set their _values_ to a **placeholder** to indicate that they are available but unassigned.

## 2. Arrange Reservations

- If there isn't a guest list, you will want to return a `new_seating_chart()` filled with placeholders. A `default argument` for your function might be helpful here. If you do have a guest list, you can start with a `new_seating_chart()`, then loop from 1 to the number of guests and assign them to seats in order.

## 3. Find all Available Seats

- You can loop through all the (key, value) pairs in a dictionary by calling `dict.items()`. You can verify that a variable or value is None through an `if statement` -- `if var is None` will return True if the value is `None`. You can add things to a `list` by calling `list.append()`

## 4. Current seating capacity

- You can loop through all of the values in the dict object by calling `dict.values()`. Seats are available when their value is `None`.

## 5. Accommodate Waiting Guests

- You need to find the current number of empty seats and check to see if it is greater than or equal to the number of guests waiting. If the guests can be accommodated, you will need to call `find_all_available_seats()` to get a list of seat numbers you can assign guests to. Remember that `range()` can take any sort of number as an argument....**including** the number returned from calling `len()` on a list. Also remember that using `list[index_number]` will return the **value** that is located at the **index number** inside the brackets.

## 6. Empty the Seats

- Given the seating chart `dict`, and a `list` of seat numbers, you'll want to indicate the seat is now available for another guest by replacing their name with a placeholder. Looping through the seat number list and looking for those seats in the dictionary might be helpful here.
