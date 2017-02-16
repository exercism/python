import itertools


class corners(object):
    def __init__(self, i, j):
        # i, j are position of corner
        self.i = i
        self.j = j

    def __str__(self):
        return "[" + str(self.i) + ", " + str(self.j) + "]"


# return corner on the same line
def same_line(index, list):
    for c in list:
        if c.i == index:
            return c


# return corner on the same column
def same_col(index, list):
    for c in list:
        if c.j == index:
            return c


def search_corners(input):
    corner_list = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if (input[i][j] == "+"):
                corner_list.append(corners(i, j))
    return corner_list


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
    for i in range(1, len(quartet)):
        if abs(quartet[i].i - mid_x) != dx or abs(quartet[i].j - mid_y) != dy:
            return False
    return True


# validate path between two corners
def path(c1, c2, input):
    if c1.i == c2.i:
        for j in range(min(c1.j + 1, c2.j + 1), max(c1.j, c2.j)):
            if input[c1.i][j] != "-" and input[c1.i][j] != "+":
                return False
        return True
    elif c1.j == c2.j:
        for i in range(min(c1.i + 1, c2.i + 1), max(c1.i, c2.i)):
            if input[i][c1.j] != "|" and input[i][c1.j] != "+":
                return False
        return True


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
    nb_rect = 0
    # test empty str
    if lines == "":
        return nb_rect

    corners = search_corners(lines)
    # no corners in str
    if len(corners) == 0:
        return nb_rect

    # now let the magic begins
    # all combinations of 4 corners (python ftw)
    q = list(itertools.combinations(corners, r=4))
    rectangles = []
    for el in q:
        if (possible_rect(el)):
            rectangles.append(el)

    # validate path in found rectangles
    for rect in rectangles:
        if (validate_rect(rect, lines)):
            nb_rect = nb_rect + 1
    return nb_rect
