def to_rounds(number):
    """Return a list of rounds that includes `number` and the next two."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds1, rounds2):
    """Return a list of rounds that combines `rounds1` and `rounds2`."""
    return rounds1 + rounds2


def list_contains_round(rounds, number):
    """Return whether `rounds` includes the `number` round."""
    return number in rounds


def card_average(hand):
    """Return the average of the hand."""
    total = 0
    count = 0
    for card in hand:
      total += card
      count += 1
    return total / count


def approx_average_is_average(hand):
    """Return whether the average of the first and last card is the average."""
    return card_average([hand[0], hand[-1]]) == card_average(hand)


def average_even_is_average_odd(hand):
    """Return whether the average of the even cards is the same as that odd cards."""
    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand):
    """Double the value of the last card if it is a Jack (11)."""
    if hand[-1] == 11:
      hand[-1] *= 2
