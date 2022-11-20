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

Implement a function `fixListOfWagons` that accepts a wagon ID `list` .
The function should `return` the `list` with the first 2 elements repositioned to the end of the `list`.

```python
eachWagonsWieght = [2, 5, 1, 7, 4, 12, 6, 3, 13]
fixListOfWagons(eachWagonsWieght)
// => [1, 7, 4,  12, 6, 3, 13, 2, 5]
```

## 3. Add missing values

Uh-oh. some wagons seem to have gone missing.

Fortunately, your friend just found another `list` which appears to contain the missing wagon IDs, and would like you to add them into the main wagon ID `list`.
All they can remember is that the missing values should be placed _directly after_ the designated locomotive.

Given this new information, write a function called `CorrectListOfWagons` that takes two `lists` containing wagon IDs as the arguments.
The wagon IDs of the second `list` should be added into the first `list` directly after the locomotive (ID `1`).

```python
eachWagonsWieght = [1, 5, 20, 7, 4, 8]
missingWagons = [3, 17, 6, 15]
CorrectListOfWagons(eachWagonsWieght, missingWagons)
// => [1, 3, 17, 6, 15, 5, 20, 7, 4, 8]
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
