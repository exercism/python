"""Functions for ice cream stand."""

import itertools

def ice_cream_combinations(flawors, scoops):
    """Return a tuple of all possible combinations without repetition.

    :param flawors: list - aributary number of flawors.
    :param scoops: int - number of scoops.
    :return: tuple - tuple of all possible combinations.
    """

    return tuple(itertools.combinations(flawors, scoops))


def sprinkles(ice_creams, selector):
    """Get the ice cream with sprinkles.

    :param ice_creams: list - ice_cream_orders.
    :param selector: list - which ice creams that needs sprinkels.
    :return: list - ice creams that needs sprinkles.
    """
    return list(itertools.compress(ice_creams, selector))


def fill_out_ice_cream_menu(flavors, toping, sprinkles):
    """Fill out ice cream menu.

    :param flavors: tuple - ice cream flavors.
    :param toping: tuple - ice cream topings.
    :param sprinkles: tuple - ice cream sprinkles.
    :return: list - ice cream menu filled out.
    """
    return list(itertools.zip_longest(flavors, toping, sprinkles, fillvalue="None"))
    
     