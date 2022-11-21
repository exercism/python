"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, locomotive, *rest = each_wagons_id
    return [locomotive, *missing_wagons, *rest, first, second]
