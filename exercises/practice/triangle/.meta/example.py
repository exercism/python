def valid(sides):
    return sum(sorted(sides)[:2]) >= sorted(sides)[2] and all(
        side > 0 for side in sides
    )


def equilateral(sides):
    return valid(sides) and all(sides[0] == side for side in sides)


def isosceles(sides):
    return valid(sides) and any(
        side_1 == side_2 for side_1, side_2 in zip(sorted(sides), sorted(sides)[1:])
    )


def scalene(sides):
    return valid(sides) and not isosceles(sides)
