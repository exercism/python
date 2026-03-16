"""Functions for formatting bakery receipts."""


def receipt_header(customer_name, receipt_width):
    """Format the receipt header.

    :param customer_name: str - the name of the customer.
    :param receipt_width: int - the total width of the receipt in characters.
    :return: str - a centered title string bounded by dashes.
    """

    pass


def receipt_item(item_name, price, item_width, price_width):
    """Format a single receipt item with price.

    :param item_name: str - the name of the item.
    :param price: float - the cost of the item.
    :param item_width: int - the total width allocated for the item name.
    :param price_width: int - the total width allocated for the price.
    :return: str - formatted string with item name and price.
    """

    pass


def receipt_summary(subtotal, tax_rate, total_width):
    """Format the tax and subtotal summary of the receipt.

    :param subtotal: float - the total cost before tax.
    :param tax_rate: float - the tax percentage (e.g., 0.05 for 5%).
    :param total_width: int - the total width of the receipt in characters.
    :return: str - formatted string summarizing the financials.
    """

    pass


def format_message(template, **kwargs):
    """Format a message from a stored template using keyword arguments.

    :param template: str - a message template with named placeholders.
    :param kwargs: keyword arguments to fill the template placeholders.
    :return: str - the formatted message, wrapped with '~ ' and ' ~'.
    """

    pass


def generate_receipt(customer_name, items, prices, tax_rate, receipt_width, gift_message=""):
    """Generate the full receipt block.

    :param customer_name: str - the name of the customer.
    :param items: list[str] - a list of item names.
    :param prices: list[float] - a list of prices matching the items.
    :param tax_rate: float - the tax percentage (e.g., 0.05 for 5%).
    :param receipt_width: int - the total width of the receipt in characters.
    :param gift_message: str - an optional pre-formatted gift message to append.
    :return: str - the complete receipt string.
    """

    pass
