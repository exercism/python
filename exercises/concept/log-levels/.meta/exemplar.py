from enum import Enum


class LogLevel(Enum):
    """Represent different log levels by their verbose codes."""

    TRACE = 'TRC'
    DEBUG = 'DBG'
    INFO = 'INF'
    WARNING = 'WRN'
    WARN = 'WRN'
    ERROR = 'ERR'
    FATAL = 'FTL'
    UNKNOWN = 'UKN'


class LogLevelInt(Enum):
    """Represent different log levels by their short codes."""

    TRACE = 0
    DEBUG = 1
    INFO = 4
    WARNING = 5
    WARN = 5
    ERROR = 6
    FATAL = 7
    UNKNOWN = 42


def parse_log_level(message):
    """Return level enum for log message.

    :param message: log message (string)
    :return: enum - 'LogLevel.<level>'.  Return 'LogLevel.Unknown' if an unknown severity is passed.
    """

    str_split = message.split(':')
    lvl = str_split[0][1:-1]
    if lvl in [level.value for level in LogLevel]:
        return LogLevel(lvl)
    return LogLevel('UKN')


def convert_to_short_log(log_level, message):
    """Convert a log message to its shorter format.

    :param log_level: enum - 'LogLevel.<level>'  e.g.  'LogLevel.Error'
    :param message: str - log message
    :return: enum -  'LogLevelInt.<value>` e.g. 'LogLevelInt.5'
    """

    return f'{LogLevelInt[log_level.name].value}:{message}'


def get_warn_alias():
    """Returns the enum for LogLevel.Warning.

    :return: enum - 'LogLevel'.<alias>'
    """

    return LogLevel('WRN')


def get_members():
    """Return all members of the enum.

    :return: list of tuples -  [(name1, value1), (name2, value2)]
    """

    out_list = []
    for member in LogLevel:
        out_list.append((member.name, member.value))
    return out_list
