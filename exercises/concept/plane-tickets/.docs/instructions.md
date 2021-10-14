# Instructions

Conda airlines has over 10.000 flights a day, but they need to automate. They are currently assigning all seats to passengers by hand.

They have asked _you_ to create software to automate the assigning of seats to passengers. They require your software to be memory efficient and performant.

Conda's airplanes have up to _6 seats_ in each row, and each airplane can have many rows.

While the rows are defined using numbers, seats in each row are defined using letters from the alphabet, with `seat A` being `seat 1` in its row.

You can use this _table_ as a guide:

| x             | 1         | 2     |
| :----:        | :----:    | :----:|
| Row           | 5         | 21    |
| Seat number   | 1         | 4     |
| Seat letter   | A         | D     |
| Result        | 5A        | 21D   |

## 1. Generate an amount of seats

Implement the `generate_seats()` function that returns an iterable of seats given the following variable:

`amount`: The amount of seats to be generated.

_Note: The returned seats should be ordered, so: 1A 1B 1C._

```python
>>> seats = generate_seats(10)

>>> next(seats)
1A
```

## 2. Assign seats to people

