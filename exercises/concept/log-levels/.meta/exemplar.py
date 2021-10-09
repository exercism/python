from enum import Enum


class LogLevel(Enum):
    TRACE = 'TRC'
    DEBUG = 'DBG'
    INFO = 'INF'
    WARNING = 'WRN'
    WARN = 'WRN'
    ERROR = 'ERR'
    FATAL = 'FTL'
    UNKNOWN = 'UKN'


class LogLevelInt(Enum):
    TRACE = 0
    DEBUG = 1
    INFO = 4
    WARNING = 5
    WARN = 5
    ERROR = 6
    FATAL = 7
    UNKNOWN = 42


def parse_log_level(message):
    str_split = message.split(':')
    lvl = str_split[0][1:-1]
    if lvl in [level.value for level in LogLevel]:
        return LogLevel(lvl)
    return LogLevel('UKN')


def convert_to_short_log(log_level, message):
    return '{}:{}'.format(LogLevelInt[log_level.name].value, message)


def get_warn_alias():
    return LogLevel('WRN')


def get_members():
    out_list = list()
    for member in LogLevel:
        out_list.append((member.name, member.value))
    return out_list
