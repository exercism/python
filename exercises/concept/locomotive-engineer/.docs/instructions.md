# Instructions

Your friend Linus is a Locomotive Engineer who drives cargo trains between cities.
Although they are amazing at handling trains, they are not amazing at handling logistics or computers.
They would like to enlist your programming help organizing train details and correcting mistakes in route data.

~~~~exercism/note
This exercise could easily be solved using slicing, indexing, and various `dict` methods.
However, we would like you to practice packing, unpacking, and multiple assignment in solving each of the tasks below.
~~~~

## 1. Create a list of all wagons

Your friend has been keeping track of each wagon identifier (ID), but they are never sure how many wagons the system is going to have to process at any given time. It would be much easier for the rest of the logistics program to have this data packaged into a unified `list`.

Implement a function `get_list_of_wagons()` that accepts an arbitrary number of wagon IDs.
Each ID will be a positive integer.
The function should then `return` the given IDs as a single `list`.

```python
>>> get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)
[1, 7, 12, 3, 14, 8, 5]
```

## 2. Fix the list of wagons

At this point, you are starting to get a feel for the data and how it's used in the logistics program.
The ID system always assigns the locomotive an ID of **1**, with the remainder of the wagons in the train assigned a randomly chosen ID greater than **1**.

Your friend had to connect two new wagons to the train and forgot to update the system!
Now, the first two wagons in the train `list` have to be moved to the end, or everything will be out of order.

To make matters more complicated, your friend just uncovered a second `list` that appears to contain missing wagon IDs.
All they can remember is that once the new wagons are moved, the IDs from this second `list` should be placed directly after the designated locomotive.

Linus would be really grateful to you for fixing their mistakes and consolidating the data.

Implement a function `fix_list_of_wagons()` that takes two `lists` containing wagon IDs.
It should reposition the first two items of the first `list` to the end, and insert the values from the second `list` behind (_on the right hand side of_) the locomotive ID (**1**).
The function should then `return` a `list` with the modifications.

```python
>>> fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
[1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
```

## 3. Add missing stops

Now that all the wagon data is correct, Linus would like you to update the system's routing information.
Along a transport route, a train might make stops at a few different stations to pick up and/or drop off cargo.
Each journey could have a different number of these intermediary delivery points.
Your friend would like you to update the systems routing `dict` with any missing/additional delivery information.

Implement a function `add_missing_stops()` that accepts a routing `dict` followed by a variable number of keyword arguments.
These arguments could be in the form of a `dict` holding one or more stops, or any number of `stop_number=city` keyword pairs.
Your function should then return the routing `dict` updated with an additional `key` that holds a `list` of all the added stops in order.

```python
>>> add_missing_stops({"from": "New York", "to": "Miami"},
                      stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                      stop_4="Jacksonville", stop_5="Orlando")

{"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}
```

## 4. Extend routing information

Linus has been working on the routing program and has noticed that certain routes are missing some important details.
Initial route information has been constructed as a `dict` and your friend would like you to update that `dict` with whatever might be missing.
Every route in the system requires slightly different details, so Linus would really prefer a generic solution.

Implement a function called `extend_route_information()` that accepts two `dicts`.
The first `dict` contains the origin and destination cities the train route runs between.

The second `dict` contains other routing details such as train speed, length, or temperature.
The function should return a consolidated `dict` with all routing information.

~~~~exercism/note
The second `dict` can contain different/more properties than the ones shown in the example.
~~~~

```python
>>> extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"})
{"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}
```

## 5. Fix the wagon depot

When Linus was surveying the wagon depot they noticed that the wagons were not getting stored in the correct order.
In addition to an ID, each wagon has a color that corresponds to the type of cargo it carries.
Wagons are stored in the depot in grids, where each column in the grid has wagons of the same color.

However, the logistics system shows `lists` of wagons to be stored in the depot have their _rows_ grouped by color.
But for the storage grid to work correctly, each _row_ should have three different colors so that the _columns_ align by color.
Your friend would like you to sort out the wagon depot `lists`, so that the wagons get stored correctly.

Implement a function called `fix_wagon_depot()` that accepts a `list` of three items.
Each `list` item is a sublist (or "row") that contains three `tuples`.
Each `tuple` is a `(<wagon ID>, <wagon color>)` pair.

Your function should return a `list` with the three "row" `lists` reordered to have the wagons swapped into their correct positions.

```python
>>> fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ])

[
[(2, "red"), (5, "blue"), (3, "orange")],
[(4, "red"), (9, "blue"), (7, "orange")],
[(8, "red"), (13,"blue"), (11, "orange")]
]
```
