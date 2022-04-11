"""Functions to keep track of inventory lists and alter them."""


def create_inventory(items):
    """Create a dict that tracks the frequency (count) of each element in the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    pass


def add_items(inventory, items):
    """Add or increment items to the `inventory` dict using elements from the `items` list.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory dictionary update with the new items.
    """

    pass


def decrement_items(inventory, items):
    """Decrement items in the `inventory` dict using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory dictionary with items decremented.
    """

    pass


def remove_item(inventory, item):
    """Remove item from `inventory` dict if a key matches `item` string and return the result, else just return.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory dictionary with item removed.
    """

    pass


def list_inventory(inventory):
    """Create a list of tuples containing all key value pairs in `inventory` dict.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    pass
