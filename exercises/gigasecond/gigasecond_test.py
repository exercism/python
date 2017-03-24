from datetime import datetime
import unittest

from gigasecond import add_gigasecond


class GigasecondTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            add_gigasecond(datetime(2011, 4, 25)),
            datetime(2043, 1, 1, 1, 46, 40))

    def test_2(self):
        self.assertEqual(
            add_gigasecond(datetime(1977, 6, 13)),
            datetime(2009, 2, 19, 1, 46, 40))

    def test_3(self):
        self.assertEqual(
            add_gigasecond(datetime(1959, 7, 19)),
            datetime(1991, 3, 27, 1, 46, 40))

    def test_4(self):
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0)),
            datetime(2046, 10, 2, 23, 46, 40))

    def test_5(self):
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59)),
            datetime(2046, 10, 3, 1, 46, 39))

    def test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)

        self.assertEqual(add_gigasecond(your_birthday), your_gigasecond)


if __name__ == '__main__':
    unittest.main()
