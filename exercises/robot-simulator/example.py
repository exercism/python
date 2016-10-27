NORTH, EAST, SOUTH, WEST = range(4)


class Compass(object):
    compass = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, bearing=NORTH):
        self.bearing = bearing

    def left(self):
        self.bearing = self.compass[self.bearing - 1]

    def right(self):
        self.bearing = self.compass[(self.bearing + 1) % 4]


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.compass = Compass(bearing)
        self.x = x
        self.y = y

    def advance(self):
        if self.bearing == NORTH:
            self.y += 1
        elif self.bearing == SOUTH:
            self.y -= 1
        elif self.bearing == EAST:
            self.x += 1
        elif self.bearing == WEST:
            self.x -= 1

    def turn_left(self):
        self.compass.left()

    def turn_right(self):
        self.compass.right()

    def simulate(self, commands):
        instructions = {'A': self.advance,
                        'R': self.turn_right,
                        'L': self.turn_left}
        for cmd in commands:
            if cmd in instructions:
                instructions[cmd]()

    @property
    def bearing(self):
        return self.compass.bearing

    @property
    def coordinates(self):
        return (self.x, self.y)
