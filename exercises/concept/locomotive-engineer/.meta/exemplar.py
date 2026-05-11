"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
       *args: An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers, assembled from *args..
    """

    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]) The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """

    first, second, locomotive, *rest = each_wagons_id

    return [locomotive, *missing_wagons, *rest, first, second]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        **kwargs: arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """

    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """

    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[tuple]) The list of rows of wagons.

    Returns:
        list[tuple]: the list of rows of wagons.
    """

    [*row_one], [*row_two], [*row_three] = zip(*wagons_rows)

    return [row_one, row_two, row_three]
