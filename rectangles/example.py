import itertools


class corners():
    def __init__(self, i, j):
        # i, j are position of corner
        self.i = i
        self.j = j

    def __str__(self):
        return "[" + str(self.i) + ", " + str(self.j) + "]"


# return corner on the same line
def same_line(index, items):
    return next((c for c in items if c.i == index), None)


# return corner on the same column
def same_col(index, items):
    return next((c for c in items if c.j == index), None)


def search_corners(table):
    return [corners(i, j) for i, row in enumerate(table)
            for j, col in enumerate(row)
            if col == "+"]


# validate that 4 points form a
# rectangle by comparing distance to
# centroid of the rectangle for all corners
def possible_rect(quartet):
    mid_x = 0
    mid_y = 0

    # centroid
    for c in quartet:
        mid_x = mid_x + c.i / 4.0
        mid_y = mid_y + c.j / 4.0

    # reference distance using first corner
    dx = abs(quartet[0].i - mid_x)
    dy = abs(quartet[0].j - mid_y)

    # Check all the same distance from centroid are equals
    return all(dx == abs(c.i - mid_x) and dy == abs(c.j - mid_y)
               for c in quartet[1:])


# validate path between two corners
def path(c1, c2, table):
    if c1.i == c2.i:
        bounds = (min(c1.j + 1, c2.j + 1), max(c1.j, c2.j))
        return all(table[c1.i][j] in "-+" for j in range(*bounds))
    elif c1.j == c2.j:
        bounds = (min(c1.i + 1, c2.i + 1), max(c1.i, c2.i))
        return all(table[i][c1.j] in "|+" for i in range(*bounds))
    else:
        return False


# validate path of rectangle
def validate_rect(rect, input):
    # validate connection at every corner
    # with neighbours on the same line and col
    for i in range(0, len(rect)):
        l = same_line(rect[i].i, rect[0:i] + rect[i + 1:])
        c = same_col(rect[i].j, rect[0:i] + rect[i + 1:])
        if not path(rect[i], l, input) or not path(rect[i], c, input):
            return False
    return True


# count number of rectangles
# inside ASCII in input lines
def count(lines=""):
    # test empty str
    if not lines:
        return 0

    corners = search_corners(lines)

    # now let the magic begin
    # all combinations of 4 corners (python ftw)
    rectangles = (c for c in itertools.combinations(corners, r=4)
                  if possible_rect(c))

    # validate path in found rectangles
    return len([r for r in rectangles if validate_rect(r, lines)])
