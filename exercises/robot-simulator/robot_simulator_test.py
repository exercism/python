import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


# Tests adapted from `problem-specifications//canonical-data.json` @ v3.0.0

class RobotSimulatorTest(unittest.TestCase):
    def test_init(self):
        robot = Robot()
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    def test_setup(self):
        robot = Robot(SOUTH, -1, -1)
        self.assertEqual(robot.coordinates, (-1, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_change_direction_right(self):
        A = [NORTH, EAST, SOUTH, WEST]
        B = [EAST, SOUTH, WEST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("R")
            self.assertEqual(robot.bearing, B[x])

    def test_change_direction_left(self):
        A = [NORTH, WEST, SOUTH, EAST]
        B = [WEST, SOUTH, EAST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("L")
            self.assertEqual(robot.bearing, B[x])

    def test_advance_positive_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("A")
        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.bearing, NORTH)

    def test_advance_negative_south(self):
        robot = Robot(SOUTH, 0, 0)
        robot.simulate('A')
        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_advance_positive_east(self):
        robot = Robot(EAST, 0, 0)
        robot.simulate('A')
        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.bearing, EAST)

    def test_advance_negative_west(self):
        robot = Robot(WEST, 0, 0)
        robot.simulate('A')
        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.bearing, WEST)

    def test_simulate_prog1(self):
        robot = Robot(NORTH, 7, 3)
        robot.simulate("RAALAL")
        self.assertEqual(robot.coordinates, (9, 4))
        self.assertEqual(robot.bearing, WEST)

    def test_simulate_prog2(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.bearing, WEST)

    def test_simulate_prog3(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.bearing, SOUTH)

    def test_simulate_prog4(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.bearing, NORTH)

if __name__ == '__main__':
    unittest.main()
