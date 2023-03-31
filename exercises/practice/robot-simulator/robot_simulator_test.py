import unittest

from robot_simulator import (
    Robot,
    NORTH,
    EAST,
    SOUTH,
    WEST,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class RobotSimulatorTest(unittest.TestCase):

    # Test create robot
    def test_at_origin_facing_north(self):
        robot = Robot(NORTH, 0, 0)

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, NORTH)

    def test_at_negative_position_facing_south(self):
        robot = Robot(SOUTH, -1, -1)

        self.assertEqual(robot.coordinates, (-1, -1))
        self.assertEqual(robot.direction, SOUTH)

    # Test rotating clockwise
    def test_changes_north_to_east(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("R")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, EAST)

    def test_changes_east_to_south(self):
        robot = Robot(EAST, 0, 0)
        robot.move("R")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, SOUTH)

    def test_changes_south_to_west(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("R")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, WEST)

    def test_changes_west_to_north(self):
        robot = Robot(WEST, 0, 0)
        robot.move("R")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, NORTH)

    # Test rotating counter-clockwise
    def test_changes_north_to_west(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("L")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, WEST)

    def test_changes_west_to_south(self):
        robot = Robot(WEST, 0, 0)
        robot.move("L")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, SOUTH)

    def test_changes_south_to_east(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("L")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, EAST)

    def test_changes_east_to_north(self):
        robot = Robot(EAST, 0, 0)
        robot.move("L")

        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.direction, NORTH)

    # Test moving forward one
    def test_facing_north_increments_y(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("A")

        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.direction, NORTH)

    def test_facing_south_decrements_y(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("A")

        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.direction, SOUTH)

    def test_facing_east_increments_x(self):
        robot = Robot(EAST, 0, 0)
        robot.move("A")

        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.direction, EAST)

    def test_facing_west_decrements_x(self):
        robot = Robot(WEST, 0, 0)
        robot.move("A")

        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.direction, WEST)

    # Test follow series of instructions
    def test_moving_east_and_north_from_readme(self):
        robot = Robot(NORTH, 7, 3)
        robot.move("RAALAL")

        self.assertEqual(robot.coordinates, (9, 4))
        self.assertEqual(robot.direction, WEST)

    def test_moving_west_and_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("LAAARALA")

        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.direction, WEST)

    def test_moving_west_and_south(self):
        robot = Robot(EAST, 2, -7)
        robot.move("RRAAAAALA")

        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.direction, SOUTH)

    def test_moving_east_and_north(self):
        robot = Robot(SOUTH, 8, 4)
        robot.move("LAAARRRALLLL")

        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.direction, NORTH)
