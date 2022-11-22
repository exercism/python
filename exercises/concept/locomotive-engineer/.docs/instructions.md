# Instructions

Your friend Linus is a Locomotive Engineer who drives cargo trains between cities.
Although your friend is great handling the trains, they aren't amazing handling the logistics computers and would like your programming help organizing the train and correcting mistakes in the data.

```exercism/note
This exercise could easily be solved using `list` slicing, indexing, and `dict` methods.
 However, we'd like you to practice using Unpacking and Multiple Assignment to solve each of the tasks below.
```

## 1. Create a list of all wagons

Your friend has been keeping track of each wagon identifier, but they're never sure how many wagons they are going to have to process at any given time. It would be much easier for the rest of the logistics program to have the data to be returned as a list.

Implement a function `get_list_of_wagons` that accepts an unknown amount of positive integers which are the IDs of each wagon.
It should then return the given IDs as a `list`.

```python
>>> get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)
[1, 7, 12, 3, 14, 8, 3]
```

## 2. Fix the list of wagons

At this point, you are starting to get a feel for your friend's data and how it's used in the logistics program.
The train ID system works by assigning the locomotive an ID of `1` and then assigning the remainder of the wagons a randomly chosen ID greater than `1`.

But then your friend had to connect two new wagons to the train and forgot to update the system!
Now the first two wagons in the `list` have to be moved to the back of the train, or everything will be out of order.

Additionally, your friend just found a second `list` that appears to contain missing wagon IDs, and would like you to merge it together with the main wagon ID `list`.
All they can remember is that once the new wagons are moved to the end, the values from the second list should be placed directly after the designated locomotive.

Your friend would be really grateful to you for fixings their mistakes and consolodating the data.

Implement a function `fix_list_of_wagons` that takes two `lists` containing wagon IDs as the arguments.
It should reposition the first two items of the first list to the end, and then insert the values from the second list behind the locomotive ID (`1`).
The function should then `return` the `list` with the modfications.

```python
>>> fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
[1, 3, 17, 6, 15, 7, 4,  12, 6, 3, 13, 2, 5]
```

## 3. Add missing stops

Now that all the wagon data is correct, your friend would like you to update the systems routing information.
Under the train journey the train will stop at a few stations to pick up and drop off cargo.
Each journey will have different amount of stops. To simplyfy setting up the routing program your friend would like you to add the missing stops to a `dict`.

Implement a function `add_missing_stops` that accepts an unknown amount of `dicts` which are the stops in order.
It should then return the given stops as one `dict`.

```python
>>> add_missing_stops({"stop_1": "Hamburg"}, {"stop_2": "Hannover"}, {"stop_3": "Frankfurt"})
{"stop_1": "Hamburg", "stop_2": "Hannover", "stop_3": "Frankfurt"}
```

## 4. Extend routing information

Your friend has been working on the routing program and has noticed that the routing information is missing some important details.
Initial routing information has been constructed as a `dict` , and you friend would like you to update it with the additions provided.
Every route requires slightly different information, so your friend would really prefer a generic solution.

Implement a function `extend_route_information` that accepts two `dicts`.
The first `dict` contains which cities the train route moves between.

The second `dict` contains other routing details such as train speed or length.
The function should return a consolidated `dict` with all routing information.

```exercism/note
The second dict can contain different properties than the ones shown in the example.
```

```python
>>> extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"})
{"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}
```

## 5. Fix the wagon depot

When your friend was surveying the wagon depot they noticed that the wagons were not getting stored in the correct order.
In addition to an ID, each wagon has a color that corresponds to the type of cargo it carries.
Wagons are stored in the depot in grids, with each column in the grid grouped by wagon color.

In the control system, it appears that the lists of wagons to be stored in the depo have their row positioning swapped so that the columns won't align by color. For the storage grid to work correctly, the first and last wagons in each "row" need to switch positions.
Your friend would like you to help them sort out the wagon depot lists, so that the wagons get stored correctly.

Implement a function `fix_wagon_depot` that accepts a nested `list`.
The first `list` contains the first row of wagons, the second `list` contains the second row of wagons and the third `list` contains the third row of wagons. All rows are of equal length.
Every wagon within a row is represented by a `tuple` with (`<wagon ID>`, `<wagon color>`).

Your function should return a `list` with the 3 row `lists` reordered with the wagons swapped into their correct positions.

```python
>>> fix_wagon_depot([
                    [(2, "red"), (4, "red"),(8, "red")],
                    [(5, "blue"),(9, "blue"),(13,"blue")], 
                    [(3, "orange"),(7, "orange"), (11, "orange")],
                    ])

[
[(2, "red"),(5, "blue"),(3, "orange")],
[(4, "red"),(9, "blue"),(7, "orange")],
[(8, "red"),(13,"blue"),(11, "orange")]
]
```
