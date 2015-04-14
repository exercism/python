import unittest

from leap import is_leap_year


class YearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertIs(is_leap_year(1996), True)

    @unittest.skip("")
    def test_non_leap_year(self):
        self.assertIs(is_leap_year(1997), False)

    @unittest.skip("")
    def test_non_leap_even_year(self):
        self.assertIs(is_leap_year(1998), False)

    @unittest.skip("")
    def test_century(self):
        self.assertIs(is_leap_year(1900), False)

    @unittest.skip("")
    def test_exceptional_century(self):
        self.assertIs(is_leap_year(2400), True)

if __name__ == '__main__':
    unittest.main()
