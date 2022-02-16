class Alien:
    """A class to represent an Alien.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate int - position on the x-axis
    y_coordinate: int - position on the y-axis
    health : int - amount of helath points

    Methods
    -------
    hit(): Decrements Alien health by one point.
    is_alive(): Returns a boolena for if Alien is alive.
    teleport(new_x_coordinate, new_y_coordinate): Moves Alien to new coordinates.
    collision_detection: Implementation TBD.
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

def new_aliens_collection(positions):
    """Creates a list of Alien instances from a list of coordinate tuples.

     :param positions: list - a list of tuples of (x, y) coordinates.
     :return: list - a list of Alien objects.
     """
    return [Alien(position[0], position[1]) for position in positions]
