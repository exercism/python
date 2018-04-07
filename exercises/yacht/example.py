from collections import Counter
from functools import partial


def ns(number, dice):
    return number * len([n for n in dice if n == number])


def full_house(dice):
    counter = Counter(dice)
    return sum(dice) if set(counter.values()) == {3, 2} else 0


def four_of_a_kind(dice):
    counter = Counter(dice)
    number, count = counter.most_common()[0]
    return 4 * number if count >= 4 else 0


def little_straight(dice):
    return 30 if set(dice) == {1, 2, 3, 4, 5} else 0


def big_straight(dice):
    return 30 if set(dice) == {2, 3, 4, 5, 6} else 0


def yacht(dice):
    return 50 if len(set(dice)) == 1 else 0


categories = {
    "ones": partial(ns, 1),
    "twos": partial(ns, 2),
    "threes": partial(ns, 3),
    "fours": partial(ns, 4),
    "fives": partial(ns, 5),
    "sixes": partial(ns, 6),
    "full house": full_house,
    "four of a kind": four_of_a_kind,
    "little straight": little_straight,
    "big straight": big_straight,
    "choice": sum,
    "yacht": yacht,
}


def score(dice, category):
    try:
        return categories[category](dice)
    except IndexError:
        raise ValueError("no such category")
