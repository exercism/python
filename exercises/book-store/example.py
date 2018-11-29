from functools import reduce

BASE_COST = 800
discount = [1.0, 1.0, 0.95, 0.9, 0.8, 0.75]


def groupCost(g):
    return len(g) * discount[len(g)]


class Grouping:
    def __init__(self, groups=None):
        self.groups = [set()] if groups is None else groups

    def total(self):
        return sum(map(groupCost, self.groups)) * BASE_COST

    def dup(self):
        return Grouping(list(map(set, self.groups)))

    def add_to_valid(self, b):
        """Returns all possible groupings from current grouping adding book b
        """
        other = self.dup()
        other.groups.sort(key=lambda g: len(g))
        results = []
        for i, g in enumerate(other.groups):
            if b not in g:
                o2 = other.dup()
                o2.groups[i].add(b)
                results.append(o2)
        if not results:
            other.groups.append(set([b]))
            return [other]
        return results

    def __lt__(self, other):
        return self.total() < other.total()


def step(rs, b):
    return [g for r in rs for g in r.add_to_valid(b)]


def calculate_total(books):
    if len(books) == 0:
        return 0
    start = Grouping([{books[0]}])
    return round(min(reduce(step, books[1:], [start])).total())
