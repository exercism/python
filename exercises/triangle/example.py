def valid(sides):
    return (
        sum(sorted(sides)[:2]) >= sorted(sides)[2] and
        all(s > 0 for s in sides)
    )


def is_equilateral(sides):
    return valid(sides) and all(sides[0] == s for s in sides)


def is_isosceles(sides):
    return (
        valid(sides) and
        any(s1 == s2 for s1, s2 in zip(sorted(sides), sorted(sides)[1:]))
    )


def is_scalene(sides):
    return valid(sides) and not is_isosceles(sides)
