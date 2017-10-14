import unittest

from leap import is_leap_year


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class YearTest(unittest.TestCase):
    def test_year_not_divisible_by_4(self):
        self.assertIs(is_leap_year(2015), False)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertIs(is_leap_year(2016), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertIs(is_leap_year(2100), False)

    def test_year_divisible_by_400(self):
        self.assertIs(is_leap_year(2000), True)


if __name__ == '__main__':
    unittest.main()
