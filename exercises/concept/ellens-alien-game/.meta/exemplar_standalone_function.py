try:
    from exemplar import Alien
except ImportError as err:
    raise ImportError("classes_standalone_function.py tried to import the 'Alien' class, but could not find it. "
                      "Did you remember to create it?") from err

def new_aliens_collection(positions):
    """Creates a list of Alien instances from a list of coordinate tuples.

     :param positions: list - a list of tuples of (x, y) coordinates.
     :return: list - a list of Alien objects.
     """
    return [Alien(position[0], position[1]) for position in positions]
