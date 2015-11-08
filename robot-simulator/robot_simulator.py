# Support for enumerations is new in version 3.4.
try:
    from enum import Enum
except ImportError:
    Enum = object


class Bearing(Enum):
    NORTH, EAST, SOUTH, WEST = range(4)


class Robot(object):
    def __init__(self):
        pass  # Complete the Robot class ...
