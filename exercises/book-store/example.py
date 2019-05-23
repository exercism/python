from functools import reduce

BASE_COST = 800
discount = [1.0, 1.0, 0.95, 0.9, 0.8, 0.75]


def group_cost(group):
    return len(group) * discount[len(group)]


class Grouping:
    def __init__(self, groups=None):
        self.groups = [set()] if groups is None else groups

    def total(self):
        return sum(map(group_cost, self.groups)) * BASE_COST

    def dup(self):
        return Grouping(list(map(set, self.groups)))

    def add_to_valid(self, book):
        """Returns all possible groupings from the
        current grouping adding book
        """
        other = self.dup()
        other.groups.sort(key=lambda g: len(g))
        results = []
        for index, group in enumerate(other.groups):
            if book not in group:
                other2 = other.dup()
                other2.groups[index].add(book)
                results.append(other2)
        if not results:
            other.groups.append(set([book]))
            return [other]
        return results

    def __lt__(self, other):
        return self.total() < other.total()


def step(basket, book):
    return [group for groupings in basket
            for group in groupings.add_to_valid(book)]


def total(basket):
    if len(basket) == 0:
        return 0
    start = Grouping([{basket[0]}])
    return round(min(reduce(step, basket[1:], [start])).total())
