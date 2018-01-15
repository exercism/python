class TriangleError(Exception):
    pass


class Triangle(object):
    def __init__(self, x, y, z):
        self.sides = (x, y, z)

        if self._invalid_lengths() or self._violates_inequality():
            raise TriangleError("Side lengths are invalid for a triangle")

    def _invalid_lengths(self):
        return any([side <= 0 for side in self.sides])

    def _violates_inequality(self):
        x, y, z = self.sides
        return any([
            x + y <= z,
            x + z <= y,
            y + z <= x,
        ])

    def kind(self):
        distinct = len(set(self.sides))
        if distinct == 1:
            return 'equilateral'
        elif distinct == 2:
            return 'isosceles'
        else:
            return 'scalene'
