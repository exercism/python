import unittest

from robot import Robot
import random


class RobotTest(unittest.TestCase):
    name_re = r'^[A-Z]{2}\d{3}$'

    def test_has_name(self):
        self.assertRegexpMatches(Robot().name, self.name_re)

    def test_name_sticks(self):
        robot = Robot()
        robot.name
        self.assertEqual(robot.name, robot.name)

    def test_different_robots_have_different_names(self):
        self.assertNotEqual(
            Robot().name,
            Robot().name
        )

    def test_reset_name(self):
        # Set a seed
        seed = "Totally random."

        # Initialize RNG using the seed
        random.seed(seed)

        # Call the generator
        robot = Robot()
        name = robot.name

        # Reinitialize RNG using seed
        random.seed(seed)

        # Call the generator again
        robot.reset()
        name2 = robot.name
        self.assertNotEqual(name, name2)
        self.assertRegexpMatches(name2, self.name_re)

if __name__ == '__main__':
    unittest.main()
