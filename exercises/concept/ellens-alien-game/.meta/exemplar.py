class Alien:
    """A class to represent an Alien.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of helath points.

    Methods
    -------
    hit(): Decrements Alien health by one point.
    is_alive(): Returns a boolena for if Alien is alive.
    teleport(new_x_coordinate, new_y_coordinate): Moves Alien to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass
