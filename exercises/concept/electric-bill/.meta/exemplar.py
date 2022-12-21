"""Functions which helps company to calculate their power usage"""


def get_the_amount_of_hours(hours):
    """Return the amount of hours.

    :param: hours: int - amount of hours.
    :return: int - amount of hours.
    """
    return (hours + 3) % 24


def get_kW_value(watts):
    """Return the kW value of a given watt value.

    :param: watts: int - watt value.
    :return: float - kW value.
    """
    return round(watts / 1000, 1) # rounds here


def get_kwh_value(watts):
    """Return the kWh value of a given watt value and hours.

    :param: watts: int - watt value.
    :param: hours: int - kilowatt hour value.
    """
    return get_kW_value(watts) // 3600


def get_efficiency(efficiency):
    """Return the efficiency as a power factor.

    :param: efficiency: float - efficiency.
    :return: float - efficiency.
    """
    return efficiency / 100


def get_price_of_kwh(watts, efficiency, price):
    """Return the price of a given kWh value, efficiency and price.

    :param: watts: int - watt value.
    :param: efficiency: float - efficiency.
    :param: price: float - price of kWh.
    :return: float - price of kWh.
    """
    return price * (get_kwh_value(watts) / get_efficiency(efficiency))
