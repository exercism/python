# Instructions

Mecha Munch™, a grocery shopping automation company has just hired you to work on their ordering app.
Your team is tasked with building an MVP (_[minimum viable product][mvp]_) that manages all the basic shopping cart activities, allowing users to add, remove, and sort their grocery orders.
Thankfully, a different team is handling all the money and check-out functions!

## 1. Add Item(s) to the Users Shopping Cart

The MVP should allow the user to add items to their shopping cart.
This could be a single item or multiple items at once.
Since this is an MVP, item quantity is indicated by _repeats_.
If a user wants to add 2 Oranges, 'Oranges' will appear twice in the input iterable.
If the user already has the item in their cart, the cart quantity should be increased by 1.
If the item is _new_ to the cart, it should be added with a quantity of 1.

Create the function `add_items(<current_cart>, <items_to_add>)` that takes a cart dictionary and any list-like iterable of items to add as arguments.
It should return a new/updated shopping cart dictionary for the user.

```python
>>> add_items({'Banana': 3, 'Apple': 2, 'Orange': 1},
              ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))
{'Banana': 4, 'Apple': 5, 'Orange': 2}

>>> add_items({'Banana': 3, 'Apple': 2, 'Orange': 1},
              ['Banana', 'Orange', 'Blueberries', 'Banana'])
{'Banana': 5, 'Apple': 2, 'Orange': 2, 'Blueberries': 1}
```

## 2. Read in Items Listed in the Users Notes App

Uh-oh.
Looks like the product team is engaging in [feature creep][feature creep].
They want to add extra functionality to the MVP.
The application now has to create a shopping cart by reading items off a users notes app.
Convenient for the users, but slightly more work for the team.

Create the function `read_notes(<notes>)` that can take any list-like iterable as an argument.
The function should parse the items and create a user shopping cart/dictionary.
Each item should be added with a quantity of 1.
The new user cart should then be returned.

```python
>>> read_notes(('Banana','Apple', 'Orange'))
{'Banana': 1, 'Apple': 1, 'Orange': 1}

>>> read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple'])
{'Blueberries' : 1, 'Pear' : 1, 'Orange' : 1, 'Banana' : 1, 'Apple' : 1}
```

## 3. Update Recipe "Ideas" Section

The app has an "ideas" section that's filled with finished recipes from various cuisines.
The user can select any one of these recipes and have all its ingredients added to their shopping cart automatically.
The project manager has asked you create a way to edit these "ideas" recipes, since the content team keeps changing around ingredients and quantities.

Create the function `update_recipes(<ideas>, <recipe_updates>)` that takes an "ideas" dictionary and an iterable of recipe updates as arguments.
The function should return the new/updated "ideas" dictionary.

```python
>>> update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                    'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
(('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),))
...

{'Banana Bread' : {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Eggs': 2, 'Butter': 1, 'Milk': 2, 'Eggs': 3},
 'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}}

>>> update_recipes({'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
                    'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
                    'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
[('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})])
...

{'Banana Bread': {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
 'Raspberry Pie': {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2},
 'Pasta Primavera': {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1},
 'Blueberry Crumble': {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3}}
```

## 4. Sort the Items in the User Cart

Once a user has started a cart, the app allows them to sort their items alphabetically.
This makes things easier to find, and helps when there are data-entry errors like having 'potatoes' and 'Potato' in the database.

Create the function `sort_entries(<cart>)` that takes a shopping cart/dictionary as an argument and returns a new, alphabetically sorted one.

```python
>>> sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1})
{'Apple': 2, 'Banana':3, 'Orange': 1}
```

## 5. Send User Shopping Cart to Store for Fulfillment

The app needs to send a given users cart to the store for fulfillment.
However, the shoppers in the store need to know which store aisle the item can be found in and if the item needs refrigeration.
So (_rather arbitrarily_) the "fulfillment cart" needs to be sorted in reverse alphabetical order with item quantities combined with location and refrigeration information.

Create the function `send_to_store(<cart>, <aisle_mapping>)` that takes a user shopping cart and a dictionary that has store aisle number and a `True`/`False` for refrigeration needed for each item.
The function should `return` a combined "fulfillment cart" that has (quantity, aisle, and refrigeration) for each item the customer is ordering.
Items should appear in _reverse_ alphabetical order.

```python
>>> send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
                  {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]})
{'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}
```

## 6. Update the Store Inventory to Reflect what a User Has Ordered.

The app can't just place customer orders endlessly.
Eventually, the store is going to run out of various products.
So your app MVP needs to update the store inventory every time a user sends their order to the store.
Otherwise, customers will order products that aren't actually available.

Create the function `update_store_inventory(<fulfillment_cart>, <store_inventory>)` that takes a "fulfillment cart" and a store inventory.
The function should reduce the store inventory amounts by the number "ordered" in the "fulfillment cart" and then return the updated store inventory.
Where a store item count falls to 0, the count should be replaced by the message 'Out of Stock'.

```python
>>> update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
{'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]})

{'Banana': [12, 'Aisle 5', False], 'Apple': [10, 'Aisle 4', False], 'Orange': ['Out of Stock', 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True]}
```

[feature creep]: https://en.wikipedia.org/wiki/Feature_creep
[mvp]: https://en.wikipedia.org/wiki/Minimum_viable_product
