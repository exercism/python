import itertools


class Corners:
    def __init__(self, i, j):
        # i, j are position of corner
        self.i = i
        self.j = j

    def __str__(self):
        return "[" + str(self.i) + ", " + str(self.j) + "]"


# return corner on the same line
def same_line(index, list):
    for corner in list:
        if corner.i == index:
            return corner


# return corner on the same column
def same_col(index, list):
    for corner in list:
        if corner.j == index:
            return corner


def search_corners(input):

    return [Corners(item, element) for item in range(len(input))
            for element in range(len(input[item]))
            if (input[item][element] == "+")]


# validate that 4 points form a rectangle by
# comparing distance to centroid of the rectangle for all corners
def possible_rect(quartet):
    mid_x = 0
    mid_y = 0

    for centroid in quartet:
        mid_x = mid_x + centroid.i / 4.0
        mid_y = mid_y + centroid.j / 4.0

    # reference distance using first corner
    dx = abs(quartet[0].i - mid_x)
    dy = abs(quartet[0].j - mid_y)

    # Check all the same distance from centroid are equals
    for i in range(1, len(quartet)):
        if abs(quartet[i].i - mid_x) != dx or abs(quartet[i].j - mid_y) != dy:
            return False
    return True


# validate path between two corners
def path(corner1, corner2, input):
    if corner1.i == corner2.i:
        for j in range(min(corner1.j + 1, corner2.j + 1),
                       max(corner1.j, corner2.j)):
            if input[corner1.i][j] != "-" and input[corner1.i][j] != "+":
                return False
        return True

    elif corner1.j == corner2.j:
        for i in range(min(corner1.i + 1, corner2.i + 1),
                       max(corner1.i, corner2.i)):
            if input[i][corner1.j] != "|" and input[i][corner1.j] != "+":
                return False
        return True


# validate path of rectangle
def validate_rect(rectangle, input):
    # validate connection at every corner
    # with neighbours on the same line and col
    for i in range(0, len(rectangle)):
        line = same_line(rectangle[i].i, rectangle[0:i] + rectangle[i + 1:])
        column = same_col(rectangle[i].j, rectangle[0:i] + rectangle[i + 1:])

        if ((not path(rectangle[i], line, input)) or
                (not path(rectangle[i], column, input))):
            return False

    return True


# count number of rectangles inside ASCII in input lines
def rectangles(strings=""):
    rectangle_total = 0
    # test empty str
    if not strings:
        return rectangle_total

    corners = search_corners(strings)

    # no corners in str
    if not len(corners):
        return rectangle_total

    # all combinations of 4 corners
    quartets = list(itertools.combinations(corners, r=4))
    paths = (quartet for quartet in quartets if possible_rect(quartet))

    # validate paths
    for path in paths:
        if validate_rect(path, strings):
            rectangle_total += 1
    return rectangle_total
