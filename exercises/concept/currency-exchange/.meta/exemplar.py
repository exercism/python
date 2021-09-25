def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return number_of_bills * denomination


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return int(budget / denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    exchange_fee = (exchange_rate / 100) * spread
    actual_rate = exchange_rate + exchange_fee
    exchangeable_amount = int((budget / actual_rate) / denomination)
    return exchangeable_amount * denomination


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :param spread: int - the percentage taken as an exchange fee.
    :param denomination:  int - the value of a single bill.
    :return: int - the value that cannot be exchanged, due to the denomination.
    """

    exchange_fee = (exchange_rate / 100) * spread
    actual_rate = exchange_rate + exchange_fee
    non_exchangeable_amount = int((budget / actual_rate) % denomination)
    return non_exchangeable_amount
