import unittest

from robot_simulator import Robot, Bearing


class RobotTests(unittest.TestCase):

    def test_setup(self):
        robot = Robot(Bearing.NORTH, [0, 0])
        self.assertEqual([0, 0], robot.coordiantes)
        self.assertEqual(Bearing.NORTH, robot.bearing)

    def test_turn_right(self):
        robot = Robot()
        for direction in [Bearing.EAST, Bearing.SOUTH, Bearing.WEST, Bearing.NORTH]:
            robot.turn_right()
            self.assertEqual(robot.bearing, direction)

    def test_turn_left(self):
        robot = Robot()
        for direction in [Bearing.WEST, Bearing.SOUTH, Bearing.EAST, Bearing.NORTH]:
            robot.turn_left()
            self.assertEqual(robot.bearing, direction)

    def test_advance_positive_north(self):
        robot = Robot(Bearing.NORTH, [0, 0])
        robot.advance()
        self.assertEqual([0, 1], robot.coordiantes)
        self.assertEqual(Bearing.NORTH, robot.bearing)

    def test_advance_positive_east(self):
        robot = Robot(Bearing.EAST, [0, 0])
        robot.advance()
        self.assertEqual([1, 0], robot.coordiantes)
        self.assertEqual(Bearing.EAST, robot.bearing)

    def test_advance_negative_south(self):
        robot = Robot(Bearing.SOUTH, [0, 0])
        robot.advance()
        self.assertEqual([0, -1], robot.coordiantes)
        self.assertEqual(Bearing.SOUTH, robot.bearing)

    def test_advance_positive_west(self):
        robot = Robot(Bearing.WEST, [0, 0])
        robot.advance()
        self.assertEqual([-1, 0], robot.coordiantes)
        self.assertEqual(Bearing.WEST, robot.bearing)

    def test_simulate_prog1(self):
        robot = Robot(Bearing.NORTH, [0, 0])
        robot.simulate("LAAARALA")
        self.assertEqual([-4, 1], robot.coordiantes)
        self.assertEqual(Bearing.WEST, robot.bearing)

    def test_simulate_prog2(self):
        robot = Robot(Bearing.EAST, [2, -7])
        robot.simulate("RRAAAAALA")
        self.assertEqual([-3, -8], robot.coordiantes)
        self.assertEqual(Bearing.SOUTH, robot.bearing)

    def test_simulate_prog3(self):
        robot = Robot(Bearing.SOUTH, [8, 4])
        robot.simulate("LAAARRRALLLL")
        self.assertEqual([11, 5], robot.coordiantes)
        self.assertEqual(Bearing.NORTH, robot.bearing)

if __name__ == '__main__':
    unittest.main()
