def sublist(list_one, list_two):
    if list_one == list_two:
        return "equal"
    if contains(list_one, list_two):
        return "superlist"
    if contains(list_two, list_one):
        return "sublist"
    return "unequal"


def contains(list_one, list_two):
    if not list_two:
        return True
    if len(list_two) > len(list_one):
        return False
    for i in range(len(list_one) - len(list_two) + 1):
        if list_one[i] != list_two[0]:
            continue
        for j in range(len(list_two)):
            if list_one[i + j] != list_two[j]:
                break
        else:
            return True
    return False
