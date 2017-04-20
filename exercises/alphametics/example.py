from itertools import combinations, permutations


def check_leading_zeros(*numbers):
    return any(n[0] == '0' for n in numbers)


def test_equation(puzzle, substitutions):
    equation = ''.join(substitutions.get(char) or char for char in puzzle)
    left, right = equation.split(' == ')
    left_numbers = left.split(' + ')

    if check_leading_zeros(right, *left_numbers):
        return False

    return sum(map(int, left_numbers)) == int(right)


def solve(puzzle):
    letters = set(char for char in puzzle if char.isupper())
    numbers = map(str, range(10))

    for c in combinations(numbers, len(letters)):
        for p in permutations(c):
            substitutions = dict(zip(letters, p))
            if test_equation(puzzle, substitutions):
                return {k: int(v) for k, v in substitutions.items()}

    return {}  # no solution found
