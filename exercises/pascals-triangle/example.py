def triangle(nth):
    return [row(i) for i in range(nth + 1)]


def is_triangle(t):
    new_t = triangle(len(t) - 1)
    return t == new_t


def row(nth):
    r = [1]
    for i in range(1, nth + 1):
        r.append(int(r[-1] * (nth - i + 1) / i))
    return " ".join([str(i) for i in r])
