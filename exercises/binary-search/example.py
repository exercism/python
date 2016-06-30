
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
    if not all(search_list[i] <= search_list[i + 1] for i in range(len(search_list) - 1)):
        raise ValueError("This list must be sorted.")


def list_empty(search_list):
    if len(search_list) == 0:
        raise ValueError('This list has no items.')
