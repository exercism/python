import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


# Tests adapted from `problem-specifications//canonical-data.json` @ v3.2.0

class RobotSimulatorTest(unittest.TestCase):

    def test_create_robot_at_origin_facing_north(self):
        robot = Robot(NORTH, 0, 0)
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    def test_create_robot_at_negative_position_facing_south(self):
        robot = Robot(SOUTH, -1, -1)
        self.assertEqual(robot.coordinates, (-1, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_rotating_clockwise(self):
        dirA = [NORTH, EAST, SOUTH, WEST]
        dirB = [EAST, SOUTH, WEST, NORTH]
        for x in range(len(dirA)):
            robot = Robot(dirA[x], 0, 0)
            robot.turn_right()
            self.assertEqual(robot.bearing, dirB[x])

    def test_rotating_clockwise_by_simulate_R(self):
        A = [NORTH, EAST, SOUTH, WEST]
        B = [EAST, SOUTH, WEST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("R")
            self.assertEqual(robot.bearing, B[x])

    def test_rotating_counter_clockwise(self):
        dirA = [NORTH, EAST, SOUTH, WEST]
        dirB = [WEST, NORTH, EAST, SOUTH]
        for x in range(len(dirA)):
            robot = Robot(dirA[x], 0, 0)
            robot.turn_left()
            self.assertEqual(robot.bearing, dirB[x])

    def test_rotating_counter_clockwise_by_simulate_L(self):
        A = [NORTH, WEST, SOUTH, EAST]
        B = [WEST, SOUTH, EAST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("L")
            self.assertEqual(robot.bearing, B[x])

    def test_moving_forward_one_facing_north_increments_Y(self):
        robot = Robot(NORTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.bearing, NORTH)

    def test_moving_forward_one_facing_south_decrements_Y(self):
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_moving_forward_one_facing_east_increments_X(self):
        robot = Robot(EAST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.bearing, EAST)

    def test_moving_forward_one_facing_west_decrements_X(self):
        robot = Robot(WEST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.bearing, WEST)

    def test_series_of_instructions_moving_east_and_north_from_README(self):
        robot = Robot(NORTH, 7, 3)
        robot.simulate("RAALAL")
        self.assertEqual(robot.coordinates, (9, 4))
        self.assertEqual(robot.bearing, WEST)

    def test_series_of_instructions_moving_west_and_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.bearing, WEST)

    def test_series_of_instructions_moving_west_and_south(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.bearing, SOUTH)

    def test_series_of_instructions_moving_east_and_north(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.bearing, NORTH)


if __name__ == '__main__':
    unittest.main()
