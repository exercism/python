class CustomSet:
    def __init__(self, elements=[]):
        self.elements = list(elements)

    def isempty(self):
        return not self.elements

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(x in other for x in self)

    def isdisjoint(self, other):
        return all(x not in other for x in self)

    def __eq__(self, other):
        return self.issubset(other) and other.issubset(self)

    def add(self, element):
        if element not in self:
            self.elements.append(element)

    def intersection(self, other):
        result = CustomSet()
        for x in self:
            if x in other:
                result.add(x)
        return result

    def __sub__(self, other):
        result = CustomSet()
        for x in self:
            if x not in other:
                result.add(x)
        return result

    def __add__(self, other):
        result = CustomSet(self.elements)
        for x in other:
            result.add(x)
        return result
