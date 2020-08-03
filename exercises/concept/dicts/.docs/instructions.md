In this exercise you'll be managing an inventory system.

You will be given a list of items. Each time an item is in the given list, add `1` to the key in the _given_ inventory. Each item should be organized by their name and the amount of that item. You will also have to delete items from the inventory.

You will also have to implement a function which returns a list of `tuples` of all the key-value pairs in the _given_ inventory.

## 1. Create an inventory from a list

Implement the `create_inventory()` function that creates an "inventory" from a list of items. It should return a `dictionary` representing the types and amounts of the items.

```python
>>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
{"coal":1, "wood":2 "diamond":3}
```

## 2. Add items from a list to an existing dictionary

Implement the `add_items()` function that adds a list of items to a passed in inventory dictionary:

```python
>>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
{"coal":2, "wood":2, "iron":1}
```

## 3. Remove items from the inventory

Implement the `delete_items()` function that removes items in the passed-in list from the passed inventory dictionary:

```python
>>> delete_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
{"coal":2, "diamond":0, "iron":3}
```

Item counts should not fall below `0`, if the amount of an item in the list exceeds the amount of items in the inventory, the value should stop at `0` and not go into negative numbers.

```python
>>> delete_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}
```

## 4. Return the inventory content

Implement the `list_inventory()` function that takes an inventory and returns a list of `(item, amount)` tuples. Only include items where the amount is greater than zero:

```python
>>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver": 0})
[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
```
