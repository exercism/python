"""Functions to help the company calculate their power usage."""


def get_extra_hours(hours):
    """Return the amount of hours.

    :param: hours: int - amount of hours.
    :return: int - amount of "extra" hours.
    """

    return (hours + 3) % 24


def get_kW_value(watts):
    """Return the kW value of a given watt value.

    :param: watts: int - watt value.
    :return: float - kW value.
    """

    # rounds to one decimal place here
    return round(watts / 1000, 1)


def get_kwh_value(watts):
    """Return the kWh value of a given watt value and hours.

    :param: watts: int - watt value.
    :param: hours: int - kilowatt hour value.
    """
    return get_kW_value(watts) // 3600


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
    return price * (get_kwh_value(watts) / get_efficiency(power_factor))
