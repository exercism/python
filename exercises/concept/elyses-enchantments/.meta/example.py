def to_list(arg1, arg2, arg3, arg4, arg5):
    return [arg1, arg2, arg3, arg4, arg5]


def list_twice(cards):
    return [cards, list(cards)]


def concatenate_lists(deck1, deck2):
    return deck1 + deck2


def list_contains_object(cards, card):
    return card in cards


def first_and_last(cards):
    return [cards[0], cards[-1]]


def interior_of_list(cards):
    return cards[1:-1]


def even_elements(cards):
    return cards[::2]


def odd_elements(cards):
    return cards[1::2]


def unshuffle(cards):
    return cards[::2] + cards[1::2]


def print_list(cards):
    for card in cards:
        print(card)


def multitype_list():
    return [1, '1', 1.0]


def swap_first_and_last(cards):
    cards[0], cards[-1] = cards[-1], cards[0]
