"""This solution for the Zebra Puzzle is adapted from a solution
by Peter Norvig for the course "Design of Computer Programs" on Udacity.
https://www.udacity.com/course/cs212
"""

from itertools import permutations


def just_right_of(x, y):
    return x - y == 1


def next_to(x, y):
    return abs(x - y) == 1


def solution():
    houses = first, _, middle, _, _ = range(5)
    orderings = list(permutations(houses))
    result = next(
        [{
            Englishman: "Englishman",
            Spaniard: "Spaniard",
            Ukrainian: "Ukrainian",
            Japanese: "Japanese",
            Norwegian: "Norwegian"
        }[x] for x in (water, zebra)]
        for (red, green, ivory, yellow, blue) in orderings
        if just_right_of(green, ivory)
        for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
        if Englishman is red if Norwegian is first if next_to(Norwegian, blue)
        for (coffee, tea, milk, oj, water) in orderings if coffee is green
        if Ukrainian is tea if milk is middle
        for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
             ) in orderings if Kools is yellow if LuckyStrike is oj
        if Japanese is Parliaments
        for (dog, snails, fox, horse, zebra) in orderings if Spaniard is dog
        if OldGold is snails if next_to(Chesterfields, fox)
        if next_to(Kools, horse))
    return result


def drinks_water():
    ans, _ = solution()
    return ans


def owns_zebra():
    _, ans = solution()
    return ans
