# Instructions

Conda Airlines is the programming-world's biggest airline, with over 10,000 flights a day!

They are currently assigning all seats to passengers by hand; this will need to be automated.

They have asked _you_ to create software to automate passenger seat assignments.
They require your software to be memory efficient and performant.

## 1. Generate seat letters

Conda wants to generate seat letters for their airplanes.
An airplane is made of rows of seats.
Each row has _4 seats_.
The seats in each row are always named `A`, `B`, `C`, and `D`.
The first seat in the row is `A`, the second seat in the row is `B`, and so on.
After reaching `D`, it should start again with `A`.

Implement a function `generate_seat_letters(<number>)` that accepts an `int` that holds how many seat letters to be generated.
The function should then return an _iterable_ of seat letters.

```python
>>> letters = generate_seat_letters(4)
>>> next(letters)
"A"
>>> next(letters)
"B"
```

## 2. Generate seats

Conda wants a system that can generate a given number of seats for their airplanes.
Each airplane has _4 seats_ in each row.
The rows are defined using numbers, starting from `1` and going up.
The seats should be ordered, like: `1A`, `1B`, `1C`, `1D`, `2A`, `2B`, `2C`, `2D`, `3A`, `3B`, `3C`, `3D`, ...

Here is an example:

|      x      |  1  |  2  |
| :---------: | :-: | :-: |
|     Row     |  5  | 21  |
| Seat letter |  A  |  D  |
|   Result    | 5A  | 21D |

Many airlines do not have _row_ number 13 on their flights, due to superstition amongst passengers.
Conda Airlines also follows this convention, so make sure you _don't_ generate seats for _row_ number 13.

Implement a function `generate_seats(<number>)` that accepts an `int` that holds how many seats to be generated.
The function should then return an _iterable_ of seats given.

```python
>>> seats = generate_seats(10)
>>> next(seats)
"1A"
>>> next(seats)
"1B"
```

## 3. Assign seats to passengers

Now that you have a function that generates seats, you can use it to assign seats to passengers.

Implement a function `assign_seats(<passengers>)` that accepts a `list` of passenger names.
The function should then return a _dictionary_ of `passenger` as _key_, and `seat_number` as _value_.

```python
>>> passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']

>>> assign_seats(passengers)
{'Jerimiah': '1A', 'Eric': '1B', 'Bethany': '1C', 'Byte': '1D', 'SqueekyBoots': '2A', 'Bob': '2B'}
```

## 4. Ticket codes

Conda Airlines would like to have a unique code for each ticket.
Since they are a big airline, they have a lot of flights.
This means that there are multiple flights with the same seat number.
They want you to create a system that creates a unique ticket that is _12_ characters long string code for identification.

This code begins with the `assigned_seat` followed by the `flight_id`.
The rest of the code is appended by `0s`.

Implement a function `generate_codes(<seat_numbers>, <flight_id>)` that accepts a `list` of `seat_numbers` and a `string` with the flight number.
The function should then return a `generator` that yields a `ticket_number`.

```python
>>> seat_numbers = ['1A', '17D']
>>> flight_id = 'CO1234'
>>> ticket_ids = generate_codes(seat_numbers, flight_id)

>>> next(ticket_ids)
'1ACO12340000'
>>> next(ticket_ids)
'17DCO1234000'
```
