"""Functions to help the company calculate their power usage."""


def get_extra_hours(hours):
    """Return the amount of hours.

    :param: hours: int - amount of hours.
    :return: int - amount of "extra" hours.
    """

    return (hours + 3) % 24


def get_kW_amount(watts):
    """Return the kW amount of a given watt amount.

    :param: watts: int - watt amount.
    :return: float - kW amount.
    """

    # rounds to one decimal place here
    return round(watts / 1000, 1)


def get_kwh_amount(watts):
    """Return the kWh amount of a given watt amount and hours.

    :param: watts: int - watt amount.
    :return: int - kilowatt hour amount.
    """
    return get_kW_amount(watts) // 3600


def get_efficiency(power_factor):
    """Return the efficiency calculated from the power factor.

    :param: power_factor: float.
    :return: float - efficiency.
    """
    return power_factor / 100


def get_cost(watts, power_factor, price):
    """Calculate the cost of a given kWh value, efficiency and price.

    :param: watts: int - watt value.
    :param: power_factor: float - efficiency.
    :param: price: float - price of kWh.
    :return: float - cost of kWh.
    """
    return price * (get_kwh_amount(watts) / get_efficiency(power_factor))
