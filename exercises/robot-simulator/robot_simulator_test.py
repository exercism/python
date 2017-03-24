import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


class RobotTests(unittest.TestCase):
    def test_init(self):
        robot = Robot()
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    def test_setup(self):
        robot = Robot(SOUTH, -1, 1)
        self.assertEqual(robot.coordinates, (-1, 1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_turn_right(self):
        robot = Robot()
        for direction in [EAST, SOUTH, WEST, NORTH]:
            robot.turn_right()
            self.assertEqual(robot.bearing, direction)

    def test_turn_left(self):
        robot = Robot()
        for direction in [WEST, SOUTH, EAST, NORTH]:
            robot.turn_left()
            self.assertEqual(robot.bearing, direction)

    def test_advance_positive_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.bearing, NORTH)

    def test_advance_positive_east(self):
        robot = Robot(EAST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.bearing, EAST)

    def test_advance_negative_south(self):
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_advance_positive_west(self):
        robot = Robot(WEST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.bearing, WEST)

    def test_simulate_prog1(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.bearing, WEST)

    def test_simulate_prog2(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.bearing, SOUTH)

    def test_simulate_prog3(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.bearing, NORTH)


if __name__ == '__main__':
    unittest.main()
