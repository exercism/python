import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


# Tests adapted from `problem-specifications//canonical-data.json` @ v3.1.0

class RobotSimulatorTest(unittest.TestCase):

    def test_robot_created_with_position_and_direction(self):
        robot = Robot(NORTH, 0, 0)
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    def test_robot_created_with_negative_position_values(self):
        robot = Robot(SOUTH, -1, 1)
        self.assertEqual(robot.coordinates, (-1, 1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_rotate_turn_right(self):
        dirA = [EAST, SOUTH, WEST, NORTH]
        dirB = [SOUTH, WEST, NORTH, EAST]
        for x in range(len(dirA)):
            robot = Robot(dirA[x], 0, 0)
            robot.turn_right()
            self.assertEqual(robot.bearing, dirB[x])

    def test_rotate_simulate_R(self):
        A = [NORTH, EAST, SOUTH, WEST]
        B = [EAST, SOUTH, WEST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("R")
            self.assertEqual(robot.bearing, B[x])

    def test_rotate_simulate_L(self):
        A = [NORTH, WEST, SOUTH, EAST]
        B = [WEST, SOUTH, EAST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("L")
            self.assertEqual(robot.bearing, B[x])

    def test_rotate_turn_left(self):
        dirA = [EAST, SOUTH, WEST, NORTH]
        dirB = [NORTH, EAST, SOUTH, WEST]
        for x in range(len(dirA)):
            robot = Robot(dirA[x], 0, 0)
            robot.turn_left()
            self.assertEqual(robot.bearing, dirB[x])

    def test_advance_positive_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.bearing, NORTH)

    def test_advance_negative_south(self):
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_advance_positive_east(self):
        robot = Robot(EAST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.bearing, EAST)

    def test_advance_negative_west(self):
        robot = Robot(WEST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.bearing, WEST)

    def test_move_east_north_from_README(self):
        robot = Robot(NORTH, 7, 3)
        robot.simulate("RAALAL")
        self.assertEqual(robot.coordinates, (9, 4))
        self.assertEqual(robot.bearing, WEST)

    def test_move_west_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.bearing, WEST)

    def test_move_west_south(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.bearing, SOUTH)

    def test_move_east_north(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.bearing, NORTH)


if __name__ == '__main__':
    unittest.main()
