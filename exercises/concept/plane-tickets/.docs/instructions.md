# Instructions

Conda airlines has over 10.000 flights a day, but they need to automate. They are currently assigning all seats to passengers by hand.

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

Many airlines do not have _row_ number 13 on their flights, due to superstition amongst passengers. Make sure you also _don't_ assign seats to _row_ number 13.

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
>>> passengers = ["Jerimiah", "Eric", "Bethaney"]

>>> assign_seats(passengers)
{"Jerimiah" : "1A", "Eric" : "1B", "Bethaney" : "1C"}
```
