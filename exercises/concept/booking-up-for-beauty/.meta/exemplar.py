from datetime import date, time, datetime


def schedule_numeric(appointment):
    """
    Convert an all-numeric date/time string to a datetime object.

    :param appointment: string - representation of a date and time.
    :return: datetime.datetime - a datetime object corresponding to the input string.
    """

    return datetime.strptime(appointment, '%m/%d/%Y %H:%M:%S')


def schedule_mixed(appointment):
    """
    Convert a date/time string including text to a datetime object.

    :param appointment: string - representation of a date and time.
    :return: datetime.datetime - a datetime object corresponding to the input string.
    """

    return datetime.strptime(appointment, '%A, %B %d, %Y %H:%M:%S')


def has_passed(appointment):
    """
    Check if the appointment has already passed.

    :param appointment: datetime.datetime - The appointment to check.
    :return: bool - was the appointment in the past?
    """

    return datetime.now() > appointment


def is_afternoon_appointment(appointment):
    """
    Check if the given appointment is in the afternoon.

    :param appointment: The appointment to check.
    :type appointment: datetime.datetime
    :return: True if the appointment is in the afternoon, False otherwise.
    :rtype: bool
    """

    return 12 <= appointment.hour < 18


def description(appointment):
    """
    Return appointment details as a customer-friendly text string.

    :param appointment: datetime.datetime
    :return: string: The customer message
    """

    return "You have an appointment on " + appointment.strftime('%m/%d/%y %I:%M:%S %p.')


def anniversary():
    """
    Calculate this year's anniversary date.

    :return: datetime.date
    """

    return date(date.today().year, 9, 15)
