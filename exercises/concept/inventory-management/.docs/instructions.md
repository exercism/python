# Instructions

In this exercise, you will be managing an inventory system.

The inventory should be organized by the item name and it should keep track of the number of items available.

You will have to handle adding items to an inventory. Each time an item appears in a given list, increase the item's quantity by `1` in the inventory. Then, you will have to handle deleting items from an inventory.

To finish, you will have to implement a function which returns all the key-value pairs in an inventory as a list of `tuples`.

## 1. Create an inventory based on a list

Implement the `create_inventory()` function that creates an "inventory" from a list of items. It should return a `dict` containing each item name paired with their respective quantity.

```python
>>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
{"coal":1, "wood":2 "diamond":3}
```

## 2. Add items from a list to an existing dictionary

Implement the `add_items()` function that adds a list of items to an inventory:

```python
>>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
{"coal":2, "wood":2, "iron":1}
```

## 3. Decrement items from the inventory

Implement the `decrement_items(<items>)` function that takes a `list` of items. The function should remove one from the available count in the inventory for each time an item appears on the `list`:

```python
>>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
{"coal":2, "diamond":0, "iron":3}
```

Item counts in the inventory should not fall below 0. If the number of times an item appears on the list exceeds the count available, the quantity listed for that item should remain at 0 and additional requests for removing counts should be ignored.

```python
>>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}
```

## 4. Remove an item entirely from the inventory

Implement the `remove_item(<inventory>, <item>)` function that removes an item and its count entirely from an inventory:

```python
>>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
{"wood":1, "diamond":2}
```

If the item is not found in the inventory, the function should return the original inventory unchanged.

```python
>>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
{"coal":2, "wood":1, "diamond":2}
```

## 5. Return the inventory content

Implement the `list_inventory()` function that takes an inventory and returns a list of `(item, quantity)` tuples. The list should only include the available items (with a quantity greater than zero):

```python
>>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
```
