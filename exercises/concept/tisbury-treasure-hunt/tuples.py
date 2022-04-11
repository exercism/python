"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: (str, str) - a tuple with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    pass


def convert_coordinate(coordinate):
    """Create and return a tuple containing two characters from the treasure coordinate.

    :param coordinate: str - a string map coordinate
    :return: (str, str) - the string coordinate seperated into its individual components.
    """

    pass


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if the coordinates match.

    :param azara_record: (str, str) - a (treasure, coordinate) pair.
    :param rui_record: (str, (str, str), str) - a (location, coordinate, quadrant) trio.
    :return: bool - returns True if coordinates match, False otherwise.
    """

    pass


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group, else return "not a match".

    :param azara_record: (str, str) - a (treasure, coordinate) pair.
    :param rui_record: (str, (str, str), str) - a (location, coordinate, quadrant) trio.
    :return: (str, str, str, (str, str), str) or str - combined record, or "not a match" if the records are incompatible.
    """

    pass


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: ((str, str, str, (str, str), str), ...) - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
    """

    pass
