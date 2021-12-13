# Instructions

Conda airlines is the programming-world's biggest airline, with over 10.000 flights a day!

They are currently assigning all seats to passengers by hand, this will need to automated.

They have asked _you_ to create software to automate the assigning of seats to passengers. They require your software to be memory efficient and performant.

Conda's airplanes have up to _4 seats_ in each row, and each airplane has many rows.

While the rows are defined using numbers, seats in each row are defined using letters from the alphabet, with `seat A` being the first _seat_ in the row.

You can use this table as a guide:

| x             | 1         | 2     |
| :----:        | :----:    | :----:|
| Row           | 5         | 21    |
| Seat letter   | A         | D     |
| Result        | 5A        | 21D   |

## 1. Generate an amount of seats

Implement the `generate_seats()` function that returns an _iterable_ of seats given the following variable:

`amount`: The amount of seats to be generated.

Many airlines do not have _row_ number 13 on their flights, due to superstition amongst passengers.
Conda Airlines also follows this convention, so make sure you _don't_ generate seats for _row_ number 13.

_Note: The returned seats should be ordered, like: 1A 1B 1C._

```python
>>> seats = generate_seats(10)
>>> next(seats)
"1A"
>>> next(seats)
"1B"
```

## 2. Assign seats to passengers

Implement the `assign_seats()` function that returns a _dictionary_ of `passenger` as _key_, and `seat_number` as _value_. Given is the following _list_:

`passengers`: A list containing passenger names.

```python
>>> passengers = ['Jerimiah', 'Eric', 'Bethaney', 'Byte', 'SqueekyBoots', 'Bob']

>>> assign_seats(passengers)
{'Jerimiah': '1A', 'Eric': '1B', 'Bethaney': '1C', 'Byte': '1D', 'SqueekyBoots': '2A', 'Bob': '2B'}
```

## 3. Ticket codes

Each ticket has a _12_ character long string code for identification.

This code begins with the `assigned_seat` followed by the `flight_id`. The rest of the code is appended by `0s`.

Implement a `generator` that yields a `ticket_number` given the following arguments:

`seat_numbers`: A _list_ of *seat_numbers*.
`flight_id`: A string containing the flight identification.

```python
>>> seat_numbers = ['1A', '17D']
>>> flight_id = 'CO1234'
>>> ticket_ids = generate_codes(seat_numbers, flight_id)

>>> next(ticket_ids)
'1ACO12340000'
>>> next(ticket_ids)
'17DCO1234000'
```
