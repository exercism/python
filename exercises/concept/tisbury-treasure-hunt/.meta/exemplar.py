"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: (str, str) - a tuple with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Create and return a tuple containing two characters from the treasure coordinate.

    :param coordinate: str - a string map coordinate
    :return: (str, str) - the string coordinate seperated into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if the coordinates match.

    :param azara_record: (str, str) - a (treasure, coordinate) pair.
    :param rui_record: (str, (str, str), str) - a (location, coordinate, quadrant) trio.
    :return: bool - returns True if coordinates match, False otherwise.
    """

    return convert_coordinate(azara_record[1]) in rui_record


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group, else return "not a match".

    :param azara_record: (str, str) - a (treasure, coordinate) pair.
    :param rui_record: (str, (str, str), str) - a (location, coordinate, quadrant) trio.
    :return: (str, str, str, (str, str), str) or str - combined record, or "not a match" if the records are incompatible.
    """

    result = "not a match"

    if compare_records(azara_record, rui_record):
        result = azara_record + rui_record

    return result


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: ((str, str, str, (str, str), str), ...) - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
    """

    report = ""

    for item in combined_record_group:
        report += f"{(item[0], item[2], item[3], item[4])}\n"

    return report
