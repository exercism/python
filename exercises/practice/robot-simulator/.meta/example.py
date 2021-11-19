NORTH, EAST, SOUTH, WEST = range(4)


class Compass:
    compass = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, direction=NORTH):
        self.direction = direction

    def left(self):
        self.direction = self.compass[self.direction - 1]

    def right(self):
        self.direction = self.compass[(self.direction + 1) % 4]


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.compass = Compass(direction)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def advance(self):
        if self.direction == NORTH:
            self.y_pos += 1
        elif self.direction == SOUTH:
            self.y_pos -= 1
        elif self.direction == EAST:
            self.x_pos += 1
        elif self.direction == WEST:
            self.x_pos -= 1

    def turn_left(self):
        self.compass.left()

    def turn_right(self):
        self.compass.right()

    def move(self, commands):
        instructions = {'A': self.advance,
                        'R': self.turn_right,
                        'L': self.turn_left}
        for cmd in commands:
            if cmd in instructions:
                instructions[cmd]()

    @property
    def direction(self):
        return self.compass.direction

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
