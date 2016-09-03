def binary_search(search_list, value):
    list_empty(search_list)
    list_sorted(search_list)
    low = 0
    high = len(search_list) - 1
    while low <= high:
        middle = (low + high) // 2
        if search_list[middle] > value:
            high = middle - 1
        elif search_list[middle] < value:
            low = middle + 1
        else:
            return middle
    return "Item not found."


def list_sorted(search_list):
    if not sorted(search_list) == search_list:
        raise ValueError("This list must be sorted.")


def list_empty(search_list):
    if not search_list
        raise ValueError('This list has no items.')
