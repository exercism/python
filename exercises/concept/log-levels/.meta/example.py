from enum import Enum


class LogLevel(Enum):
    Trace = 'TRC'
    Debug = 'DBG'
    Info = 'INF'
    Warning = 'WRN'
    Warn = 'WRN'
    Error = 'ERR'
    Fatal = 'FTL'
    Unknown = 'UKN'


class LogLevelInt(Enum):
    Trace = 0
    Debug = 1
    Info = 4
    Warning = 5
    Warn = 5
    Error = 6
    Fatal = 7
    Unknown = 42


def parse_log_level(message):
    str_split = message.split(":")
    lvl = str_split[0][1:-1]
    if lvl in [level.value for level in LogLevel]:
        return LogLevel(lvl)
    return LogLevel.Unknown


def convert_to_short_log(log_level, message):
    return "{}:{}".format(LogLevelInt[log_level.name].value, message)


def get_warn_alias():
    return LogLevel.Warn


def get_members():
    out_list = list()
    for member in LogLevel:
        out_list.append((member.name, member.value))
    return out_list
