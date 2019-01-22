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
        dir_a = [EAST, SOUTH, WEST, NORTH]
        dir_b = [SOUTH, WEST, NORTH, EAST]
        for x, direction in enumerate(dir_a):
            robot = Robot(direction, 0, 0)
            robot.turn_right()
            self.assertEqual(robot.bearing, dir_b[x])

    def test_rotate_simulate_right(self):
        instructions = [NORTH, EAST, SOUTH, WEST]
        expected = [EAST, SOUTH, WEST, NORTH]
        for x, instruction in enumerate(instructions):
            robot = Robot(instruction, 0, 0)
            robot.simulate("R")
            self.assertEqual(robot.bearing, expected[x])

    def test_rotate_simulate_left(self):
        instructions = [NORTH, WEST, SOUTH, EAST]
        expected = [WEST, SOUTH, EAST, NORTH]
        for x, instruction in enumerate(instructions):
            robot = Robot(instruction, 0, 0)
            robot.simulate("L")
            self.assertEqual(robot.bearing, expected[x])

    def test_rotate_turn_left(self):
        dir_a = [EAST, SOUTH, WEST, NORTH]
        dir_b = [NORTH, EAST, SOUTH, WEST]
        for x, direction in enumerate(dir_a):
            robot = Robot(direction, 0, 0)
            robot.turn_left()
            self.assertEqual(robot.bearing, dir_b[x])

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

    def test_move_east_north_from_readme(self):
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
