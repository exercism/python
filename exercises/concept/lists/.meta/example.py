def to_list(arg1, arg2, arg3, arg4, arg5):
    return [arg1, arg2, arg3, arg4, arg5]


def list_twice(_list):
    return [_list, list(_list)]


def concatenate_lists(list1, list2):
    return list1 + list2


def list_contains_object(_list, _object):
    return _object in _list


def first_and_last(_list):
    return [_list[0], _list[-1]]


def interior_of_list(_list):
    return _list[1:-1]


def even_elements(_list):
    return _list[::2]


def odd_elements(_list):
    return _list[1::2]


def unshuffle(_list):
    return _list[::2] + _list[1::2]


def print_list(_list):
    for element in _list:
        print(element)


def multitype_list():
    return [1, '1', 1.0]


def swap_first_and_last(_list):
    _list[0], _list[-1] = _list[-1], _list[0]
