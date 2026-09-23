from datetime import date, time, datetime


def schedule_numeric(appointment):
    """
    Convert an all-numeric date/time string to a datetime object.

    :param appointment: string - representation of a date and time.
    :return: datetime.datetime - a datetime object corresponding to the input string.
    """

    pass


def schedule_mixed(appointment):
    """
    Convert a date/time string including text to a datetime object.

    :param appointment: string - representation of a date and time.
    :return: datetime.datetime - a datetime object corresponding to the input string.
    """

    pass


def has_passed(appointment):
    """
    Check if the appointment has already passed.

    :param appointment: datetime.datetime - The appointment to check.
    :return: bool - was the appointment in the past?
    """

    pass


def is_afternoon_appointment(appointment):
    """
    Check if the given appointment is in the afternoon.

    :param appointment: The appointment to check.
    :type appointment: datetime.datetime
    :return: True if the appointment is in the afternoon, False otherwise.
    :rtype: bool
    """

    pass


def description(appointment):
    """
    Return appointment details as a customer-friendly text string.

    :param appointment: datetime.datetime
    :return: string: The customer message
    """

    pass


def anniversary():
    """
    Calculate this year's anniversary date.

    :return: datetime.date
    """

    pass
