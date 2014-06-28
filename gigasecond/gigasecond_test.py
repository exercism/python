from datetime import date
import unittest

from gigasecond import add_gigasecond


class GigasecondTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            date(2043, 1, 1),
            add_gigasecond(date(2011, 4, 25))
        )

    def test_2(self):
        self.assertEqual(
            date(2009, 2, 19),
            add_gigasecond(date(1977, 6, 13))
        )

    def test_3(self):
        self.assertEqual(
            date(1991, 3, 27),
            add_gigasecond(date(1959, 7, 19))
        )

    def test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = date(1970, 1, 1)
        your_gigasecond = date(2001, 9, 9)

        self.assertEqual(
            your_gigasecond,
            add_gigasecond(your_birthday)
        )

if __name__ == '__main__':
    unittest.main()
