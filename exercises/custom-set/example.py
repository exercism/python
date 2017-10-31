class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements = list(elements)

    def empty(self):
        return not any(self.elements)

    def __iter__(self):
        return iter(self.elements)

    def subset(self, other):
        return all(x in other for x in self)

    def disjoint(self, other):
        return all(x not in other for x in self)

    def __eq__(self, other):
        return self.subset(other) and other.subset(self)

    def add(self, element):
        if element not in self:
            self.elements.append(element)

    def intersection(self, other):
        result = CustomSet()
        for x in self:
            if x in other:
                result.add(x)
        return result

    def difference(self, other):
        result = CustomSet()
        for x in self:
            if x not in other:
                result.add(x)
        return result

    def union(self, other):
        result = CustomSet(self.elements)
        for x in other:
            result.add(x)
        return result
