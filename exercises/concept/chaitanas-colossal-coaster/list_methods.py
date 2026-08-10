"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    Parameters:
        express_queue (list): The names in the Fast-track queue.
        normal_queue (list): The names in the normal queue.
        ticket_type (int): Type of ticket. 1 = express, 0 = normal.
        person_name (str): The name of person to add to a queue.

    Returns:
        list: The (updated) queue the name was added to.
    """

    pass


def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    Parameters:
        queue (list): The names in the queue.
        friend_name (str): The name of friend to find.

    Returns:
        int: The index at which the friends name was found.
    """

    pass


def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    Parameters:
        queue (list): The names in the queue.
        index (int): The index at which to add the new name.
        person_name (str): The name to add.

    Returns:
        list: The queue updated with new name.
    """

    pass


def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name of mean person.

    Returns:
        list: The queue updated with the mean persons name removed.
    """

    pass


def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name you wish to count or track.

    Returns:
        int: The number of times the name appears in the queue.
    """

    pass


def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        str: The name that has been removed from the end of the queue.
    """

    pass


def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        list: A copy of the queue in alphabetical order.
    """

    pass
