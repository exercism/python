# Support for enumerations is new in version 3.4.
try:
    from enum import Enum
except ImportError:
    Enum = object


class Bearing(Enum):
    NORTH, EAST, SOUTH, WEST = range(4)


class Robot(object):
    def __init__(self, bearing=Bearing.NORTH, coordiantes=[0, 0]):
        self.coordiantes = coordiantes
        self.bearing = bearing

    def advance(self):
        if self.bearing == Bearing.NORTH:
            self.coordiantes[1] += 1
        elif self.bearing == Bearing.SOUTH:
            self.coordiantes[1] -= 1
        elif self.bearing == Bearing.EAST:
            self.coordiantes[0] += 1
        elif self.bearing == Bearing.WEST:
            self.coordiantes[0] -= 1

    def turn_left(self):
        left = {Bearing.NORTH: Bearing.WEST,
                Bearing.WEST: Bearing.SOUTH,
                Bearing.SOUTH: Bearing.EAST,
                Bearing.EAST: Bearing.NORTH}
        self.bearing = left[self.bearing]

    def turn_right(self):
        right = {Bearing.NORTH: Bearing.EAST,
                 Bearing.EAST: Bearing.SOUTH,
                 Bearing.SOUTH: Bearing.WEST,
                 Bearing.WEST: Bearing.NORTH}
        self.bearing = right[self.bearing]

    def simulate(self, commands):
        instructions = {'A': self.advance,
                        'R': self.turn_right,
                        'L': self.turn_left}
        for cmd in commands:
            if cmd in instructions:
                instructions[cmd]()
