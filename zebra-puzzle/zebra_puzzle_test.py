import unittest

from zebra_puzzle import solution


class ZebraPuzzleTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(("It is the Norwegian who drinks the water.\n"
                          "The Japanese keeps the zebra."),
                         solution())


if __name__ == '__main__':
    unittest.main()
