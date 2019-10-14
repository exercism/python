import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST

# Tests adapted from `problem-specifications//canonical-data.json` @ v3.2.0


class RobotSimulatorTest(unittest.TestCase):

    # Test create robot
    def test_at_origin_facing_north(self):
        robot = Robot(NORTH, 0, 0)

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(NORTH, robot.direction)

    def test_at_negative_position_facing_south(self):
        robot = Robot(SOUTH, -1, -1)

        self.assertEqual(-1, robot.coordinates["x"])
        self.assertEqual(-1, robot.coordinates["y"])
        self.assertEqual(SOUTH, robot.direction)

    # Test rotating clockwise
    def test_changes_north_to_east(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("R")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(EAST, robot.direction)

    def test_changes_east_to_south(self):
        robot = Robot(EAST, 0, 0)
        robot.move("R")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(SOUTH, robot.direction)

    def test_changes_south_to_west(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("R")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(WEST, robot.direction)

    def test_changes_west_to_north(self):
        robot = Robot(WEST, 0, 0)
        robot.move("R")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(NORTH, robot.direction)

    # Test rotating counter-clockwise
    def test_changes_north_to_west(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("L")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(WEST, robot.direction)

    def test_changes_west_to_south(self):
        robot = Robot(WEST, 0, 0)
        robot.move("L")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(SOUTH, robot.direction)

    def test_changes_south_to_east(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("L")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(EAST, robot.direction)

    def test_changes_east_to_north(self):
        robot = Robot(EAST, 0, 0)
        robot.move("L")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(NORTH, robot.direction)

    # Test moving forward one
    def test_facing_north_increments_y(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("A")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(1, robot.coordinates["y"])
        self.assertEqual(NORTH, robot.direction)

    def test_facing_south_decrements_y(self):
        robot = Robot(SOUTH, 0, 0)
        robot.move("A")

        self.assertEqual(0, robot.coordinates["x"])
        self.assertEqual(-1, robot.coordinates["y"])
        self.assertEqual(SOUTH, robot.direction)

    def test_facing_east_increments_x(self):
        robot = Robot(EAST, 0, 0)
        robot.move("A")

        self.assertEqual(1, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(EAST, robot.direction)

    def test_facing_west_decrements_x(self):
        robot = Robot(WEST, 0, 0)
        robot.move("A")

        self.assertEqual(-1, robot.coordinates["x"])
        self.assertEqual(0, robot.coordinates["y"])
        self.assertEqual(WEST, robot.direction)

    # Test follow series of instructions
    def test_moving_east_and_north_from_readme(self):
        robot = Robot(NORTH, 7, 3)
        robot.move("RAALAL")

        self.assertEqual(9, robot.coordinates["x"])
        self.assertEqual(4, robot.coordinates["y"])
        self.assertEqual(WEST, robot.direction)

    def test_moving_west_and_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.move("LAAARALA")

        self.assertEqual(-4, robot.coordinates["x"])
        self.assertEqual(1, robot.coordinates["y"])
        self.assertEqual(WEST, robot.direction)

    def test_moving_west_and_south(self):
        robot = Robot(EAST, 2, -7)
        robot.move("RRAAAAALA")

        self.assertEqual(-3, robot.coordinates["x"])
        self.assertEqual(-8, robot.coordinates["y"])
        self.assertEqual(SOUTH, robot.direction)

    def test_moving_east_and_north(self):
        robot = Robot(SOUTH, 8, 4)
        robot.move("LAAARRRALLLL")

        self.assertEqual(11, robot.coordinates["x"])
        self.assertEqual(5, robot.coordinates["y"])
        self.assertEqual(NORTH, robot.direction)


if __name__ == "__main__":
    unittest.main()
