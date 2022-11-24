# """Functions which helps the locomotive engineer to keep track of the train."""
#
# # TODO: define the 'get_list_of_wagons' function
#
#
# # TODO: define the 'fixListOfWagons()' function
# def fix_list_of_wagons(each_wagons_id, missing_wagons):
#     """Fix the list of wagons.
#
#     :parm each_wagons_id: list - the list of wagons.
#     :parm missing_wagons: list - the list of missing wagons.
#     :return: list - list of wagons.
#     """
#     pass
#
#
# # TODO: define the 'add_missing_stops()' function
#
#
# # TODO: define the 'extend_route_information()' function
# def extend_route_information(route, more_route_information):
#     """Extend the route information with the more_route_information.
#
#     :param route: dict - the route information.
#     :param more_route_information: dict -  extra route information.
#     :return: dict - extended route information.
#     """
#     pass
#
#
# # TODO: define the 'fix_wagon_depot()' function
# def fix_wagon_depot(wagons_rows):
#     """Fix the list of rows of wagons.
#
#     :param wagons_rows: list[tuple] - the list of rows of wagons.
#     :return: list[tuple] - list of rows of wagons.
#     """
#     pass
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

    #solution #1 (fastest - .02s for 5 tests)
    [*one], [*two], [*three] = zip(*wagons_rows)
    return [one, two, three]


    #solution 2 (same speed as #1)
    # one, two, three = zip(*wagons_rows)
    # return [[*one], [*two], [*three]]


    #solution 3 (same speed as #1)
    # *outer, [*one], [*two], [*three] = zip(*wagons_rows)
    # outer[:] = one, two, three
    #
    # return outer


    #solution 4 (slower - .03s for 5 tests)
    # combinations = zip(*wagons_rows)
    # results = []
    #
    # for [*row] in combinations:
    #     results.append(row)
    #
    # return results


    #solution 5 (same speed as #4)
    # results=[]
    # for [*row] in zip(*wagons_rows):
    #     results.append(row)
    #
    # return results


    #solution 6 (same speed as #4)
    # (we aren't allowed to use comprehensions in this exercise)
    #return [list(row) for row in zip(*wagons_rows)]





