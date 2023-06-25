"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart:
    :param items_to_add:
    :return: dict - the updated user cart dictionary.
    """

    current_cart.setdefault(items_to_add[0], 0)
    current_cart[items_to_add[0]] += items_to_add[1]
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Add the ingredients from a recipe to the users shopping cart.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.keys()))


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}

    for key in dict_one.keys():
        fulfillment_cart[key] = [dict_one[key]] + dict_two[key]
    return dict(sorted(fulfillment_cart.items(), reverse=True))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for key, values in fulfillment_cart.items():
        store_inventory[key].insert(0, store_inventory[key][0] - values[0])
        if store_inventory[key][0] == 0:
            store_inventory[key][0] = 'Out of Stock'
    return store_inventory
