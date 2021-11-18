class CustomSet:
    def __init__(self, elements=None):
        self.elements = list(elements) if elements is not None else list([])

    def isempty(self):
        return not self.elements

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(idx in other for idx in self)

    def isdisjoint(self, other):
        return all(idx not in other for idx in self)

    def __eq__(self, other):
        return self.issubset(other) and other.issubset(self)

    def add(self, element):
        if element not in self:
            self.elements.append(element)

    def intersection(self, other):
        result = CustomSet()
        for idx in self:
            if idx in other:
                result.add(idx)
        return result

    def __sub__(self, other):
        result = CustomSet()
        for idx in self:
            if idx not in other:
                result.add(idx)
        return result

    def __add__(self, other):
        result = CustomSet(self.elements)
        for idx in other:
            result.add(idx)
        return result
