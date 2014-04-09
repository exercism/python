SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check_lists(l1, l2):
    if l1 == l2:
        return EQUAL
    if l1 == []:
        return SUBLIST
    if l2 == []:
        return SUPERLIST
    if is_sublist(l1, l2):
        return SUBLIST
    if is_sublist(l2, l1):
        return SUPERLIST
    return UNEQUAL


def is_sublist(l1, l2):
    if len(l1) > len(l2):
        return False
    idx = -1
    while 1:
        try:
            idx = l2.index(l1[0], idx+1)
        except ValueError:
            return False
        if len(l1) > len(l2) - idx:
            return False
        if all(el1 == el2 for el1, el2 in zip(l1, l2[idx:])):
            return True
