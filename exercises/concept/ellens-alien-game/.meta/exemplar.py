"""Exemplar solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int):  Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int):  Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initialize a new Alien object and increment total_aliens_created by 1.

        Parameters:
            x_coordinate (int):  Position on the x-axis.
            y_coordinate (int): Position on the y-axis.
            health (int):  Number of health points.

        Attributes:
            x_coordinate (int):  Position on the x-axis.
            y_coordinate (int): Position on the y-axis.
            health (int):  Number of health points. Defaults to 3.

        Returns:
            Alien (Alien Object): New Alien.
        """

        Alien.total_aliens_created += 1

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

    def hit(self):
        """Decrement Alien health by 1.

        Returns:
            None
        """

        #There are two valid interpretations for this method/task.
        #The one below, and `self.health = max(0, self.health - 1)`
        #The tests for this task reflect this ambiguity.
        self.health -= 1

    def is_alive(self):
        """Return if the Alien is alive.

        Returns:
            bool:  Is the Alien Alive?
        """

        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Change Alien location.

        Parameters:
            new_x_coordinate (int): New location on x-axis.
            new_y_coordinate (int): New location on y-axis.

        Returns:
            None
        """

        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Detect collisions with another Alien.

        Parameters:
            other (object): Other Alien object.

        Returns:
            None
        """

        pass


def new_aliens_collection(positions):
    """Create a list of Alien instances from a list of coordinate tuples.

     Parameters:
        positions (list[tuple]): List of (x, y) coordinates in tuples..

     Returns:
         list[object]: List of Alien objects.
     """

    return [Alien(position[0], position[1]) for position in positions]
