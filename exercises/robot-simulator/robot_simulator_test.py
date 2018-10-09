import unittest

from robot_simulator import Robot, NORTH, EAST, SOUTH, WEST


# Tests adapted from `problem-specifications//canonical-data.json` @ v3.1.0

class RobotSimulatorTest(unittest.TestCase):
    # Case1: A robot is created with a position and a direction
    #  - Robots are created with a position and direction
    def test_init(self):
        robot = Robot(NORTH, 0, 0)
        self.assertEqual(robot.coordinates, (0, 0))
        self.assertEqual(robot.bearing, NORTH)

    #  - Negative positions are allowed
    def test_setup(self):
        robot = Robot(SOUTH, -1, 1)
        self.assertEqual(robot.coordinates, (-1, 1))
        self.assertEqual(robot.bearing, SOUTH)
    # Case2: Rotates the robot's direction 90 degrees clockwise
    #  - checks right rotation with turn_right()

    def test_turn_right(self):
        dirA = [EAST, SOUTH, WEST, NORTH]
        dirB = [SOUTH, WEST, NORTH, EAST]
        for x in range(len(dirA)):
            robot = Robot(dirA[x], 0, 0)
            robot.turn_right()
            self.assertEqual(robot.bearing, dirB[x])
    #  - checks right rotation with simulate("R")

    def test_change_direction_right(self):
        A = [NORTH, EAST, SOUTH, WEST]
        B = [EAST, SOUTH, WEST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("R")
            self.assertEqual(robot.bearing, B[x])
    # Case3: Rotates the robot's direction 90 degrees counter-clockwise
    #  - checks left rotation with simulate("L")

    def test_change_direction_left(self):
        A = [NORTH, WEST, SOUTH, EAST]
        B = [WEST, SOUTH, EAST, NORTH]
        for x in range(len(A)):
            robot = Robot(A[x], 0, 0)
            robot.simulate("L")
            self.assertEqual(robot.bearing, B[x])
    #  - checks right rotation with turn_right()

    def test_turn_left(self):
        dirA = [EAST, SOUTH, WEST, NORTH]
        dirB = [NORTH, EAST, SOUTH, WEST]
        for x in range(len(dirA)):
            robot = Robot(dirA[x], 0, 0)
            robot.turn_left()
            self.assertEqual(robot.bearing, dirB[x])
    # Case4: moves the robot forward 1 space in the direction it is pointing
    #  - increases the y coordinate one when facing north

    def test_advance_positive_north(self):
        robot = Robot(NORTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, 1))
        self.assertEqual(robot.bearing, NORTH)
    #  - decreases the y coordinate one when facing south

    def test_advance_negative_south(self):
        robot = Robot(SOUTH, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (0, -1))
        self.assertEqual(robot.bearing, SOUTH)
    #  - increases the x coordinate one when facing east

    def test_advance_positive_east(self):
        robot = Robot(EAST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (1, 0))
        self.assertEqual(robot.bearing, EAST)
    #  - decreases the x coordinate one when facing west

    def test_advance_negative_west(self):
        robot = Robot(WEST, 0, 0)
        robot.advance()
        self.assertEqual(robot.coordinates, (-1, 0))
        self.assertEqual(robot.bearing, WEST)
    # Case5: Where R = Turn Right, L = Turn Left and A = Advance,
    # the robot can follow a series of instructions
    # and end up with the correct position and direction
    #  - instructions to move east and north from README

    def test_simulate_prog1(self):
        robot = Robot(NORTH, 7, 3)
        robot.simulate("RAALAL")
        self.assertEqual(robot.coordinates, (9, 4))
        self.assertEqual(robot.bearing, WEST)
    #  - instructions to move west and north

    def test_simulate_prog2(self):
        robot = Robot(NORTH, 0, 0)
        robot.simulate("LAAARALA")
        self.assertEqual(robot.coordinates, (-4, 1))
        self.assertEqual(robot.bearing, WEST)
    #  - instructions to move west and south

    def test_simulate_prog3(self):
        robot = Robot(EAST, 2, -7)
        robot.simulate("RRAAAAALA")
        self.assertEqual(robot.coordinates, (-3, -8))
        self.assertEqual(robot.bearing, SOUTH)
    #  - instructions to move east and north

    def test_simulate_prog4(self):
        robot = Robot(SOUTH, 8, 4)
        robot.simulate("LAAARRRALLLL")
        self.assertEqual(robot.coordinates, (11, 5))
        self.assertEqual(robot.bearing, NORTH)


if __name__ == '__main__':
    unittest.main()
