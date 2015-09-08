SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check_lists(l1, l2):
    if l1 == l2:
        return EQUAL
    if contains(l1, l2):
        return SUPERLIST
    if contains(l2, l1):
        return SUBLIST
    return UNEQUAL


def contains(l1, l2):
    if not l2:
        return True
    if len(l2) > len(l1):
        return False
    for i in range(len(l1) - len(l2) + 1):
        if l1[i] != l2[0]:
            continue
        for j in range(len(l2)):
            if l1[i + j] != l2[j]:
                break
        else:
            return True
    return False
