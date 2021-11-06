from enum import Enum


class LogLevel(Enum):
    """Represents different logging levels by their verbose codes"""

    pass


def parse_log_level(message):
    """Takes a log message and returns the enum member of its level
    Returns a LogLevel.Unknown incase an unknown severity is found

    :param message: log message (string)
    :return: <enum 'LogLevel'>

    Ex:
    - parse_log_level("[INF]: File deleted") #=> LogLevel.Info
    - parse_log_level("[XYZ]: Out of context message") #=> LogLevel.Unknown
    """

    pass


def convert_to_short_log(log_level, message):
    """Converts a log message to a shorter format optimized for storage.

    :param log_level: The Log level of the log sent. ex: LogLevel.Error.
    :param message: log message (string)
    :return: <enum 'LogLevelInt'>

    Ex:
    - convert_to_short_log(LogLevel.Error, "Stack overflow") #=> "6:Stack overflow"
    """

    pass


def get_warn_alias():
    """Returns the enum for LogLevel Warning

    :return: <enum 'LogLevel'>
    """

    pass


def get_members():
    """Returns a list of tuples (name, value) containing all the members
    of the enum LogLevel.

    :return: List of tuples [(name1, value1), (name2, value2)]
    """

    pass
