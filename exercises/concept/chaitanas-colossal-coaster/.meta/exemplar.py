def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    result = express_queue if ticket_type == 1 else normal_queue
    result.append(person_name)
    return result


def find_my_friend(queue, friend_name):
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """

     :param queue: list - names in the queue.
     :param index: int - the index at which to add the new name.
     :param person_name: str - the name to add.
     :return: list - queue updated with new name.
     """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """

     :param queue: list - names in the queue.
     :param person_name: str - name of mean person.
     :return:  list - queue update with the mean persons name removed.
     """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue):
    """

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue):
    """

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    new_queue = queue[:]
    new_queue.sort()
    return new_queue
