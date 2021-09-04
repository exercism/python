def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    inventory = dict()
    add_items(inventory, items)
    return inventory


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def delete_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to remove from the inventory.
    :return:  dict - updated inventory dictionary with items removed.
    """

    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    output = list()
    for item in sorted(inventory.items()):
        if item[1] > 0:
            output.append(item)
    return output
