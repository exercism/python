from collections.abc import Iterable


def flatten(iterable):
    """Flatten a list of lists."""
    flattened = []
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            flattened += flatten(item)
        elif item is not None:
            flattened.append(item)
    return flattened
