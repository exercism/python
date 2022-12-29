# Instructions

An ice cream stand in the neighborhood does a lot of manual work.
You have offered to help them with a program that can automate some of the work.

```exercism/note
This exercise could be solved with a lot of different approaches.
However, we would like you to practice using methods from the `itertools` module.
```

## 1. All flawors combinations

The ice cream stand wants to make an advertisement for how many different ice creams they can make.
They therefore want a program that can generate all the combinations of flawors they can make.
Each ice cream has a different amount of scoopes of flawors but you can't use the same flawor more than once.

Implement a function `flawor_combinations()` that takes a `tuple` with an arbitrary number of flawors and an `int` which says how many scoopes.
The function should then `return` all combinations in the form of a `tuple`.

```python
>>> flawors = ['vanilla', 'chocolate', 'strawberry']
>>> scoops = 2
>>> ice_cream_combinations(flawors, scoops)
(('vanilla', 'chocolate'), ('vanilla', 'strawberry'), ('chocolate', 'strawberry'))
```

## 2. Sprinkels

They also want a program to optimize the process of adding sprinkels to the ice cream.
Currently they have a `list` of all ice cream order numbers and another `list` with `booleans` that say if the ice cream should have sprinkels or not.
The order numbers and the `booleans` are in the same order.

The ice cream stand has a machine that takes a `list` of orders that should have sprinkels and adds sprinkels to them.
Therefore they want a program that takes away all the orders that should not have sprinkels.

Implement a function `sprinkels()` that takes a `list` of order numbers and a `list` of `booleans` and returns a `list` of order numbers that should have sprinkels.

```python
>>> ice_creams = ['ice_cream_1', 'ice_cream_2', 'ice_cream_3']
>>> selector = [0, 1, 0]
>>> sprinkles(ice_creams, selector)
['ice_cream_2']
```

## 3. Fill out ice cream menu

Currently the ice cream has to manualy write down the ice cream menu.
Since they often make new ice creams they want a program that can generate the menu for them.

The menu is built up like this:

| Flavors    | Toping    | Sprinkels |
| ---------- | --------- | --------- |
| Strawberry | Cherry    | Licorice  |
| Choclate   | Raspberry | Caramel   |
| Mint       | Blueberry | None      |
| Vanilla    | None      | None      |

The ice cream stand has a `tuple` with all the ice cream flavors, a `tuple` with all the topings and a `tuple` with all the sprinkels.
They have set it up so the `tuple` of ice cream flavors, topings and sprinkels are in the same order.

They want a program that takes **i**th index of the `tuple` of ice cream flavors, topings and sprinkels and returns a `tuple` with the ice cream menu.

All ice creams flavors doesn't have to have a toping or sprinkels.
If an ice cream doesn't have a toping or sprinkels the value should be `"None"`.

Implement a function `fill_out_ice_cream_menu()` that accepts a `tuple` with ice cream flavors, a `tuple` with topings, and a `tuple` sprinkels.
The function should `return` a `list` of `tuples` with the ice cream menu.

```python
>>> flavors = ('vanilla', 'chocolate', 'strawberry')
>>> topings = ('cherry', 'raspberry')
>>> sprinkels = ('licorice')
>>> fill_out_ice_cream_menu(flavors, topings, sprinkels)
[('vanilla', 'cherry', 'licorice'), ('chocolate', 'raspberry', 'None'), ('strawberry', 'None', 'None')]
```
