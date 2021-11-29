from collections import Counter
from functools import partial

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def sum_of_numbers(number, dice):
    return sum(idx for idx in dice if idx == number)


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


functions = [
    yacht,
    partial(sum_of_numbers, 1),
    partial(sum_of_numbers, 2),
    partial(sum_of_numbers, 3),
    partial(sum_of_numbers, 4),
    partial(sum_of_numbers, 5),
    partial(sum_of_numbers, 6),
    full_house,
    four_of_a_kind,
    little_straight,
    big_straight,
    sum,
]


def score(dice, category):
    try:
        return functions[category](dice)
    except IndexError as error:
        raise ValueError('No such category.') from error
