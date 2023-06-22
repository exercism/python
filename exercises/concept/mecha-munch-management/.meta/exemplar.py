"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart:
    :param items_to_add:
    :return: dict - the updated user cart dictionary.
    """

    pass


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    pass


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    pass


def add_recipe(cart, recipe):
    """Add the ingredients from a recipe to the users shopping cart.

    :param cart: dict - users shopping cart dictionary.
    :param recipe: dict - recipe dictionary with ingredients.
    :return: dict - user cart dictionary updated with recipe ingredients.
    """

    pass


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    pass


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store inventory: dict - store available inventory
    :return: dict - store inventory updated.
    """

pass
