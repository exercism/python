import unittest

from zebra_puzzle import solution


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class ZebraPuzzleTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(),
                         ("It is the Norwegian who drinks the water.\n"
                          "The Japanese keeps the zebra."))


if __name__ == '__main__':
    unittest.main()
