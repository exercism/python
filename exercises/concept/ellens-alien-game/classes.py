"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    x_coordinate: int
    y_coordinate: int
    health: int
    total_aliens_created: int = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Initialize Alien object with x_coordinate and y_coordinate."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1
    def is_alive(self) -> bool:
        """Return a boolean for if Alien is alive (if health is > 0)."""
        return self.health > 0
    def teleport(self, new_x_coordinate: int, new_y_coordinate: int):
        """Move Alien object to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate
    def collision_detection(self, other):
        """Implementation TBD."""
        pass
    def alien_count(self) -> int:
        """Return the total number of Alien instances created."""
        return Alien.total_aliens_created
    

def new_aliens_collection(coordinates: list) -> list:
        """Create a collection of Alien objects from a list of coordinates."""
        return [Alien(x, y) for x, y in coordinates]


