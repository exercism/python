"""Functions which helps the locomotive engineer to keep track of the train."""

import itertools

def ice_cream_combinations(flawors, scoops):
    """Return a tuple of all possible combinations without repetition.

    :param flawors: list - aributary number of flawors.
    :param scoops: int - number of scoops.
    :return: tuple - tuple of all possible combinations.
    """

    return tuple(itertools.combinations(flawors, scoops))


def compress():
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    pass


def zip_longest(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param **kwargs: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    return {**route, "stops": list(kwargs.values())}


def product(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict - extra route information.
    :return: dict - extended route information.
    """

    return {**route, **more_route_information}
