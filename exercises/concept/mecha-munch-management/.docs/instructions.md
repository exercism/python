# Instructions

Mecha Munch(TM), a local grocery shopping automation company has just hired you to work on their ordering app.
Your team is tasked with building an MVP (_minimum viable product_) that manages all the basic shopping cart activities, allowing users to add, remove, and sort their grocery orders.
Thankfully, a different team is handling all the money and check-out functions!


## 1. Add an Item to the User Shopping Cart

The MVP should allow the user to add items to their shopping cart.
If the user has previously added the item to their cart, the quantity should be increased.
Create the function `add_item(<current_cart>, <items_to_add>)` that returns a new/updated cart for the user.

```python
>>> add_item({'Banana': 3, 'Apple': 2, 'Orange': 1}, ('blue berries', 2))
{'Banana': 5, 'Apple': 2, 'Orange': 1, 'blue berries': 2}
```

## 2. Read in Items Listed in the Users Notes App

Uh-oh.
Looks like the product team is engaging in [feature creep][feature creep].
They want to add extra functionality to the MVP.
The application now has to create a shopping cart by reading items off a users notes app.
Create the function `read_notes(<notes>)` that can take any iterable as an argument.
The function should parse the items and add one of each to a shopping cart.
The cart should then be returned in the form of a dictionary.

```python
>>> read_notes(('Banana','Apple', 'Orange'),)
{'Banana': 1, 'Apple': 1, 'Orange': 1}
```

## 3.Sort the Items in the User Cart

Once a user has started a cart, the app allows them to sort their items alphabetically.
This makes things easier to find, and helps when there are data-entry errors like having "potatoes" and 'Potato' in the database.
Create the function `sort_entries(<cart>)` that takes a shopping cart as an argument, and returns a new alphabetically sorted cart.

```python
>>> sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1})
['Apple', 'Banana', 'Orange']
```

## 4. Add Recipe Ingredients to the Shopping Cart

The app has an "ideas" section that's filled with finished recipes from various cuisines.
The user can select any one of these recipes and have all its ingredients added to their shopping cart automatically.
Adding a second recipe will add all of its ingredients to the cart as well, increasing counts or adding new entries as needed.

Create the function `add_recipe(<cart>, <recipe>)` that takes the current cart and a selected recipe as arguments.
The updated cart should be returned in alphabetical order by ingredient.

```python
>>> add_recipe({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Pie Crust': 1}, 
[{'name': 'Banana Bread', 'ingredients': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 1}}, {'name': 'Raspberry Pie', 'ingredients': {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}])

{'Apple': 2, 'Banana': 4, 'Cream Custard': 1, 'Eggs': 1, 'Flour': 1, 'Orange': 2, 'Pie Crust': 2, 'Raspberry': 1, 'Walnuts'}
```

## 5. Send User Shopping Cart to Store for Fulfillment

The app needs to send a given users cart to the store for fulfillment.
However, the shoppers in the store need to know which store isle the item can be found in and if the item needs refrigeration.
So (_rather arbitrarily_) the "fulfillment cart" needs to be sorted in reverse alphabetical order with item quantities combined with location and refrigeration information.


Create the function `send_to_store(<cart>, <isle mapping>)` that takes a user shopping cart and a dictionary that has store isle number and a True/False for refrigeration needed for each item.
The function should `return` a combined "fulfillment cart" that has (quantity, isle, and refrigeration) for each item the customer is ordering.
Items should appear in _reverse_ alphabetical order.


```python
>>> send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2}, 
                  {'Banana': (5, False), 'Apple': (4, False), 'Orange': (4, False), 'Milk': (2, True)})
{'Banana': (3, 5, False), 'Apple': (2, 4, False), 'Orange': (1, 4, False), 'Milk': (2, 2, True)}
```

## 6. Update the Store Inventory to Reflect what a User Has Ordered.

The app can't just place customer orders endlessly.
Eventually, the store is going to run out of various products.
So your app MVP needs to update the store inventory every time a user sends their order to the store.
Otherwise, customers will order products that aren't actually available.

Create the function `update_store_inventory(<fulfillment cart>, <store_inventory>)` that takes a "fulfillment cart" and a store inventory.
The function should remove the "fulfillment cart" items from the store inventory and return the updated inventory.
Where a store item count falls to 0, the count should be replaced by the message 'Out of Stock'.

```python

```


[feature creep]: https://en.wikipedia.org/wiki/Feature_creep