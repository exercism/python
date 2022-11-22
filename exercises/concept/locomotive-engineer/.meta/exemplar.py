"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, loctomotive, *rest = each_wagons_id
    return [loctomotive, *missing_wagons, *rest, first, second]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param **kwards:  arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    """Extend the route information with the more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[tuple] - the list of rows of wagons.
    :return: list[tuple] - list of rows of wagons.
    """
    combined = zip(*wagons_rows)
    return [*combined]
