# Instructions

Your friend is a Locomotive Engineer who drives cargo trains between cities.
Although your friend is great handling the trains, they aren't amazing handling the logistics computers and would like your programming help organizing the train and correcting mistakes in the data.

```exercism/note
To practice, use the Unpacking and Multiple Assignment to solve each of the tasks below.
```

## 1. Create a list of all wagons

Your friend has been keeping track of each wagon identifier, but they're never sure how many wagons they are going to have to process at any given time. It would be much easier for the rest of the logistics program to have the data to be returned as a list.

Implement a function `get_list_of_wagons` that accepts an unknown amount of positive integers which are the IDs of each wagon.
It should then return the given IDs as a `list` .

```python
>>> get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)
[1, 7, 12, 3, 14, 8, 3]
```

## 2. Move the first two elements to the end of the array

At this point, you are starting to get a feel for your friend's data and how it's used in the logistics program.
The train ID system works by assigning the locomotive an ID of `1` and then assigning the remainder of the wagons a randomly chosen ID greater than `1`.

But then your friend had to connect two new wagons to the train and forgot to update the system!
Now the first two wagons in the `list` have to be moved to the back of the train, or everything will be out of order.
Your friend would be really grateful to you for fixing their mistake.

Your friend also noticed some wagons seem to have gone missing.
Fortunately, your friend just found another `list` which appears to contain the missing wagon IDs, and would like you to add them into the main wagon ID `list`.
All they can remember is that the missing values should be placed directly after the designated locomotive.

Implement a function `fix_list_of_wagons` that takes two `lists` containing wagon IDs as the arguments.
In first `list` should the 2 wagons be repositioned the end of the `list`.
Then the second `list` should be added to the front of the first `list` .
The function should `return` the `list` with the locomtive in the front.

```python
>>> fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
[1, 3, 17, 6, 15, 7, 4,  12, 6, 3, 13, 2, 5]
```

## 4. Extend routing information

Now that all the wagon data is correct, your friend would like you to update the systems routing information.
Initial routing information has been constructed as a `dict` , and you friend would like you to update it with the additions provided.
Every route requires slightly different information, so your friend would really prefer a generic solution.

Implement a function `extend_route_information` that accepts two `dicts`.
The first `dict` contains which cities the train route moves between.

The second `dict` contains other routing details such as train speed or length.
The function should return a consolidated `dict` with all routing information.

```exercism/note
The second dict can contain different properties.
```

```python
>>> extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"})
{"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}
```
