SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if contains(list_one, list_two):
        return SUPERLIST
    if contains(list_two, list_one):
        return SUBLIST
    return UNEQUAL


def contains(list_one, list_two):
    if not list_two:
        return True
    if len(list_two) > len(list_one):
        return False
    for idx in range(len(list_one) - len(list_two) + 1):
        if list_one[idx] != list_two[0]:
            continue
        for edx, _ in enumerate(list_two):
            if list_one[idx + edx] != list_two[edx]:
                break
        else:
            return True
    return False
