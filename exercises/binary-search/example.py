
def binary_search(search_list, value):
    if not list_sorted(search_list):
        raise ValueError("The list must be sorted")
    else:
        low = 0
        high = len(search_list) - 1
        while low <= high:
            middle = (low + high ) // 2
            if search_list[middle] > value:
                high = middle - 1
            elif search_list[middle] < value:
                low = middle + 1
            else:
                return middle
        return "Item not found"


def list_sorted(search_list):
    return all(search_list[i] <= search_list[i+1] for i in xrange(len(search_list) - 1))
