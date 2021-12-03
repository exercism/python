"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""

from itertools import permutations


def just_right_of(width, height):
    return width - height == 1


def next_to(width, height):
    return abs(width - height) == 1


def solution():
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))

    # The following you are about to witness is code from someone who loves 'comprehensions'.
    # I just fixed the PEP-8 violations...
    # Someone please write this in a way that it is actually read-able?
    # Anyways, enjoy.
    # - J08K <3 (1:05 AM, nov 29th, 2021)

    result = next(
        [{
            english_man: 'Englishman',
            spaniard: 'Spaniard',
            ukrainian: 'Ukrainian',
            japanese: 'Japanese',
            norwegian: 'Norwegian'
        }[idx] for idx in (water, zebra)]
        for (red, green, ivory, yellow, blue) in orderings
        if just_right_of(green, ivory)
        for (english_man, spaniard, ukrainian, japanese, norwegian) in orderings
        if english_man is red if norwegian is first if next_to(norwegian, blue)
        for (coffee, tea, milk, orange_juice, water) in orderings if coffee is green
        if ukrainian is tea if milk is middle
        for (old_gold, kools, chesterfields, lucky_strike, parliaments
             ) in orderings if kools is yellow if lucky_strike is orange_juice
        if japanese is parliaments
        for (dog, snails, fox, horse, zebra) in orderings if spaniard is dog
        if old_gold is snails if next_to(chesterfields, fox)
        if next_to(kools, horse))
    return result


def drinks_water():
    answer, _ = solution()
    return answer


def owns_zebra():
    _, answer = solution()
    return answer
