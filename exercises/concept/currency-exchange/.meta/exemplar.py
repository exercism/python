"""Functions for calculating steps in exchaning currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""

def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange.

    Parameters:
        budget (float): Tthe amount of money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.

    Returns:
        float: The exchanged value of the foreign currency you can receive.

    Examples:
        >>> exchange_money(127.5, 1.2)
        106.25

        >>> exchange_money(200, 1.10)
        181.82

    This function calculates and returns the (estimated) value of the exchanged currency.

    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange.

    Parameters:
        budget (float): The amount of money you own.
        exchanging_value (float): The amount of your money you want to exchange now.

    Returns:
        float: The amount left of your starting currency after the exchange

    Examples:
        .>>> get_change(127.5, 120.0)
        7.5

        >>> get_change(300.75, 150.25)
        150.50

    This function calcultes and returns the amount of money left over from the budget
    after an exchange.

    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate the total value of currency at current denomination.

    Parameters:
        denomination (int): The value of a single unit (bill).
        number_of_bills (int): The total number of units (bills).

    Returns:
        int: Calculated value of the units (bills).

    Examples:
        >>> get_value_of_bills(5, 128)
        640

        >>> get_value_of_bills(15.13, 16)
        242

    This function calculates and returns the total value of the bills (excluding fractionaal amounts).

    """

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of currency units (bills) within the amount.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        int: The number of units (bills) that can be obtained from the amount.

    Examples:
        >>> get_number_of_bills(127.5, 5)
        25

        >>> get_number_of_bills(35.16, 10)
        3

    This function calcluates and returns the number pf currency units (bills) that can
    be obtained from the given amount. Whole bills only - no fractioal amounts.

    """

    return int(amount) // denomination


def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills.

    Parameters:
        amount (float): The total starting value.
        denomination (int): The value of a single unit (bill).

    Returns:
        float: The amount that is "leftover", given the current denomination.

    Examples:
        >>> get_leftover_of_bills(127.5, 20)
        7.5

        >>> get_leftover_of_bills(153.2, 10)
        3.20

    This function calculates and returns the leftover amount that cannot be
    returned from starting amount, due to the currency denomination.

    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the new currency.

    Parameters:
        budget (float): The amount of your money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.
        spread (int): The percentage that is taken as an exchange fee.
        denomination (int) The value of a single unit (bill).

    Returns:
        int: The maximum value you can get in the new currency.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20)
        80

        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95

    Note:
        The currency denomination is a whole number and cannot be sub-divided.

    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """

    exchange_fee = (exchange_rate / 100) * spread
    exchange_value = exchange_money(budget, exchange_rate + exchange_fee)
    number_of_bills = get_number_of_bills(exchange_value, denomination)
    value_of_bills = get_value_of_bills(denomination, number_of_bills)

    return value_of_bills
