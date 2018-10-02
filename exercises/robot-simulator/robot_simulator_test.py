import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.3.0

class RobotSimulatorTest(unittest.TestCase):

    def test_invalid_instruction(self):
        robot = Robot()
        with self.assertRaises(Exception):
            robot.turn_around()

    def test_invalid_direction(self):
        with self.assertRaises(Exception):
            robot = Robot(NORTHWEST, 1, 1)

    def test_init(self):
        robot = Robot()
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    def test_setup(self):
        robot = Robot(NORTH, 1, 1)
        self.assertEqual(robot.coordinates, (1, 1))
        self.assertEqual(robot.bearing, NORTH)

    def test_neg_position(self):
        robot = Robot(SOUTH, -1, -1)
        self.assertEqual(robot.coordinates, (-1, -1))
        self.assertEqual(robot.bearing, SOUTH)

    def test_turn_right(self):
        direcA=[NORTH, EAST, SOUTH, WEST] 
        direcB=[EAST, SOUTH, WEST, NORTH]
        for x in range(len(direcA)):
            robot = Robot(direcA[x], 0, 0)
            robot.turn_right()
            self.assertEqual(robot.bearing, direcB[x])

    def test_turn_left(self):
        direcA=[NORTH, EAST, SOUTH, WEST]
        direcB=[WEST, NORTH, EAST, SOUTH]
        for x in direcA:
            robot = Robot(direcA[x], 0, 0)
            robot.turn_left()
            self.assertEqual(robot.bearing, direcB[x])

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
