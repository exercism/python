"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_ids):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(wagon_ids)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    locomotive=1
    posiio_one=each_wagons_id[0]
    position_two=each_wagons_id[1]
    each_wagons_id.remove(each_wagons_id[0])
    each_wagons_id.remove(each_wagons_id[0])
    each_wagons_id.remove(locomotive)
    list_of_wagons = [locomotive] + missing_wagons +each_wagons_id+ [posiio_one, position_two]
    return list_of_wagons


def add_missing_stops(route,**stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    response={}
    response['from']=route['from']
    response['to']=route['to']
    response["stops"] = list(stops.values())
    return response


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return route|more_route_information


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    return [list(wagons) for wagons in zip(*wagons_rows)]
