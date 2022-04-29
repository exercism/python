try:
    from classes import Alien
except ImportError as err:
    raise ImportError("classes_standalone_function.py tried to import the 'Alien' class, but could not find it. "
                      "Did you remember to create it?") from err

def new_alien_list(positions):
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """

    pass
