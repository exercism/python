from enum import Enum


class LogLevel(Enum):
    """Represent different log levels by their verbose codes."""

    pass


def parse_log_level(message):
    """Returns level enum for log message.

    :param message: log message (string)
    :return: enum - 'LogLevel.<level>'.  Return 'LogLevel.Unknown' if an unknown severity is passed.
    """

    pass


def convert_to_short_log(log_level, message):
    """Convert a log message to its shorter format.

    :param log_level: enum - 'LogLevel.<level>'  e.g.  'LogLevel.Error'
    :param message: str - log message
    :return: enum -  'LogLevelInt.<value>` e.g. 'LogLevelInt.5'
    """

    pass


def get_warn_alias():
    """Return the enum for LogLevel.Warning.

    :return: enum - 'LogLevel'.<alias>'
    """

    pass


def get_members():
    """Return all members of the enum.

    :return: list of tuples -  [(name1, value1), (name2, value2)]
    """

    pass
