def distance(s1, s2):
    return sum(a != b for a, b in zip(s1, s2))
