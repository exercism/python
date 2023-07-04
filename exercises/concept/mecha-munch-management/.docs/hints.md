# Hints

## General

Remember, this is an [MVP][mvp].
That means you don't need to get too fancy with error handling or different "edge case" scenarios.
It's OK to be simple and direct with the functions you are writing.

The dictionary section of the [official tutorial][dicts-docs] and the mapping type [official library reference][mapping-types-dict] are excellent places to look for more help with all these methods.


## 1. Add Item(s) to the Users Shopping Cart

- You will need to iterate through each item in `items_to_add`.
- You can avoid a `KeyError` when a key is missing by using a `dict` [method][set-default] that takes a _default value_ as one of its arguments.
- It is also possible to accomplish the same thing manually in the `loop` by using some checking and error handling, but the `dict` method is easier.

## 2. Read in Items Listed in the Users Notes App

- Remember, Python's got a method for _everything_. This one is a _classmethod_ that's an easy way to [populate a `dict`][fromkeys] with keys.
- This `dict` method returns a _new dictionary_, populated with default values. If no value is given, the default value will become `None`

## 3. Update Recipe "Ideas" Section

- Don't overthink this one!  This can be solved in **one** `dict` method call.
- The key word here is .... [_update_][update].

## 4. Sort the Items in the User Cart

- What method would you call to get an [iterable view of items][items] in the dictionary?
- If you had a `list` or a `tuple`, what [`built-in`][builtins] function might you use to sort them?
- The built-in function you want is the one that returns a _copy_, and doesn't mutate the original.

## 5. Send User Shopping Cart to Store for Fulfillment

- Having a fresh, empty dictionary here as the `fulfillment_cart` might be handy for adding in items.
- `Looping` through the members of the cart might be the most direct way of accessing things here.
- What method would you call to get an [iterable view of just the keys][keys] of the dictionary?
- Remember that you can get the `value` of a given key by using `<dict name>[<key_name>]` syntax.
- If you had a `list` or a `tuple`, what [`built-in`][builtins] function might you use to sort them?
- Remember that the `built-in` function can take an optional `reversed=true` argument.

## 6. Update the Store Inventory to Reflect what a User Has Ordered.

- There is a method that will give you an iterable view of (`key`, `value`) pairs from the dictionary.
- You can access an item in a _nested tuple_ using _bracket notation_:  `<tuple>[<nested_tuple>][<index_of_value>]`
- Don't forget to check if an inventory count falls to zero, you'll need to add in the "Out of Stock" message.

[builtins]: https://docs.python.org/3/library/functions.html
[dicts-docs]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[fromkeys]: https://docs.python.org/3/library/stdtypes.html#dict.fromkeys
[items]: https://docs.python.org/3/library/stdtypes.html#dict.items
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[mvp]: https://en.wikipedia.org/wiki/Minimum_viable_product
[set-default]: https://docs.python.org/3/library/stdtypes.html#dict.setdefault
[update]: https://docs.python.org/3/library/stdtypes.html#dict.update
