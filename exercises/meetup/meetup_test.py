import unittest

from datetime import date

from meetup import meetup_day

try:
    from meetup import MeetupDayException
except ImportError:
    MeetupDayException = Exception


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class MeetupTest(unittest.TestCase):
    def test_monteenth_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Monday', 'teenth'), date(2013, 5, 13))

    def test_monteenth_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Monday', 'teenth'), date(2013, 8, 19))

    def test_monteenth_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Monday', 'teenth'), date(2013, 9, 16))

    def test_tuesteenth_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Tuesday', 'teenth'), date(2013, 3, 19))

    def test_tuesteenth_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Tuesday', 'teenth'), date(2013, 4, 16))

    def test_tuesteenth_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Tuesday', 'teenth'), date(2013, 8, 13))

    def test_wednesteenth_of_january_2013(self):
        self.assertEqual(
            meetup_day(2013, 1, 'Wednesday', 'teenth'), date(2013, 1, 16))

    def test_wednesteenth_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Wednesday', 'teenth'), date(2013, 2, 13))

    def test_wednesteenth_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Wednesday', 'teenth'), date(2013, 6, 19))

    def test_thursteenth_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Thursday', 'teenth'), date(2013, 5, 16))

    def test_thursteenth_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Thursday', 'teenth'), date(2013, 6, 13))

    def test_thursteenth_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Thursday', 'teenth'), date(2013, 9, 19))

    def test_friteenth_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Friday', 'teenth'), date(2013, 4, 19))

    def test_friteenth_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Friday', 'teenth'), date(2013, 8, 16))

    def test_friteenth_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Friday', 'teenth'), date(2013, 9, 13))

    def test_saturteenth_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Saturday', 'teenth'), date(2013, 2, 16))

    def test_saturteenth_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Saturday', 'teenth'), date(2013, 4, 13))

    def test_saturteenth_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Saturday', 'teenth'), date(2013, 10, 19))

    def test_sunteenth_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Sunday', 'teenth'), date(2013, 5, 19))

    def test_sunteenth_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Sunday', 'teenth'), date(2013, 6, 16))

    def test_sunteenth_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Sunday', 'teenth'), date(2013, 10, 13))

    def test_first_monday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Monday', '1st'), date(2013, 3, 4))

    def test_first_monday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Monday', '1st'), date(2013, 4, 1))

    def test_first_tuesday_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Tuesday', '1st'), date(2013, 5, 7))

    def test_first_tuesday_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Tuesday', '1st'), date(2013, 6, 4))

    def test_first_wednesday_of_july_2013(self):
        self.assertEqual(
            meetup_day(2013, 7, 'Wednesday', '1st'), date(2013, 7, 3))

    def test_first_wednesday_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Wednesday', '1st'), date(2013, 8, 7))

    def test_first_thursday_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Thursday', '1st'), date(2013, 9, 5))

    def test_first_thursday_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Thursday', '1st'), date(2013, 10, 3))

    def test_first_friday_of_november_2013(self):
        self.assertEqual(
            meetup_day(2013, 11, 'Friday', '1st'), date(2013, 11, 1))

    def test_first_friday_of_december_2013(self):
        self.assertEqual(
            meetup_day(2013, 12, 'Friday', '1st'), date(2013, 12, 6))

    def test_first_saturday_of_january_2013(self):
        self.assertEqual(
            meetup_day(2013, 1, 'Saturday', '1st'), date(2013, 1, 5))

    def test_first_saturday_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Saturday', '1st'), date(2013, 2, 2))

    def test_first_sunday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Sunday', '1st'), date(2013, 3, 3))

    def test_first_sunday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Sunday', '1st'), date(2013, 4, 7))

    def test_second_monday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Monday', '2nd'), date(2013, 3, 11))

    def test_second_monday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Monday', '2nd'), date(2013, 4, 8))

    def test_second_tuesday_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Tuesday', '2nd'), date(2013, 5, 14))

    def test_second_tuesday_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Tuesday', '2nd'), date(2013, 6, 11))

    def test_second_wednesday_of_july_2013(self):
        self.assertEqual(
            meetup_day(2013, 7, 'Wednesday', '2nd'), date(2013, 7, 10))

    def test_second_wednesday_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Wednesday', '2nd'), date(2013, 8, 14))

    def test_second_thursday_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Thursday', '2nd'), date(2013, 9, 12))

    def test_second_thursday_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Thursday', '2nd'), date(2013, 10, 10))

    def test_second_friday_of_november_2013(self):
        self.assertEqual(
            meetup_day(2013, 11, 'Friday', '2nd'), date(2013, 11, 8))

    def test_second_friday_of_december_2013(self):
        self.assertEqual(
            meetup_day(2013, 12, 'Friday', '2nd'), date(2013, 12, 13))

    def test_second_saturday_of_january_2013(self):
        self.assertEqual(
            meetup_day(2013, 1, 'Saturday', '2nd'), date(2013, 1, 12))

    def test_second_saturday_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Saturday', '2nd'), date(2013, 2, 9))

    def test_second_sunday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Sunday', '2nd'), date(2013, 3, 10))

    def test_second_sunday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Sunday', '2nd'), date(2013, 4, 14))

    def test_third_monday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Monday', '3rd'), date(2013, 3, 18))

    def test_third_monday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Monday', '3rd'), date(2013, 4, 15))

    def test_third_tuesday_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Tuesday', '3rd'), date(2013, 5, 21))

    def test_third_tuesday_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Tuesday', '3rd'), date(2013, 6, 18))

    def test_third_wednesday_of_july_2013(self):
        self.assertEqual(
            meetup_day(2013, 7, 'Wednesday', '3rd'), date(2013, 7, 17))

    def test_third_wednesday_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Wednesday', '3rd'), date(2013, 8, 21))

    def test_third_thursday_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Thursday', '3rd'), date(2013, 9, 19))

    def test_third_thursday_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Thursday', '3rd'), date(2013, 10, 17))

    def test_third_friday_of_november_2013(self):
        self.assertEqual(
            meetup_day(2013, 11, 'Friday', '3rd'), date(2013, 11, 15))

    def test_third_friday_of_december_2013(self):
        self.assertEqual(
            meetup_day(2013, 12, 'Friday', '3rd'), date(2013, 12, 20))

    def test_third_saturday_of_january_2013(self):
        self.assertEqual(
            meetup_day(2013, 1, 'Saturday', '3rd'), date(2013, 1, 19))

    def test_third_saturday_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Saturday', '3rd'), date(2013, 2, 16))

    def test_third_sunday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Sunday', '3rd'), date(2013, 3, 17))

    def test_third_sunday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Sunday', '3rd'), date(2013, 4, 21))

    def test_fourth_monday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Monday', '4th'), date(2013, 3, 25))

    def test_fourth_monday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Monday', '4th'), date(2013, 4, 22))

    def test_fourth_tuesday_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Tuesday', '4th'), date(2013, 5, 28))

    def test_fourth_tuesday_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Tuesday', '4th'), date(2013, 6, 25))

    def test_fourth_wednesday_of_july_2013(self):
        self.assertEqual(
            meetup_day(2013, 7, 'Wednesday', '4th'), date(2013, 7, 24))

    def test_fourth_wednesday_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Wednesday', '4th'), date(2013, 8, 28))

    def test_fourth_thursday_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Thursday', '4th'), date(2013, 9, 26))

    def test_fourth_thursday_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Thursday', '4th'), date(2013, 10, 24))

    def test_fourth_friday_of_november_2013(self):
        self.assertEqual(
            meetup_day(2013, 11, 'Friday', '4th'), date(2013, 11, 22))

    def test_fourth_friday_of_december_2013(self):
        self.assertEqual(
            meetup_day(2013, 12, 'Friday', '4th'), date(2013, 12, 27))

    def test_fourth_saturday_of_january_2013(self):
        self.assertEqual(
            meetup_day(2013, 1, 'Saturday', '4th'), date(2013, 1, 26))

    def test_fourth_saturday_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Saturday', '4th'), date(2013, 2, 23))

    def test_fourth_sunday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Sunday', '4th'), date(2013, 3, 24))

    def test_fourth_sunday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Sunday', '4th'), date(2013, 4, 28))

    def test_last_monday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Monday', 'last'), date(2013, 3, 25))

    def test_last_monday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Monday', 'last'), date(2013, 4, 29))

    def test_last_tuesday_of_may_2013(self):
        self.assertEqual(
            meetup_day(2013, 5, 'Tuesday', 'last'), date(2013, 5, 28))

    def test_last_tuesday_of_june_2013(self):
        self.assertEqual(
            meetup_day(2013, 6, 'Tuesday', 'last'), date(2013, 6, 25))

    def test_last_wednesday_of_july_2013(self):
        self.assertEqual(
            meetup_day(2013, 7, 'Wednesday', 'last'), date(2013, 7, 31))

    def test_last_wednesday_of_august_2013(self):
        self.assertEqual(
            meetup_day(2013, 8, 'Wednesday', 'last'), date(2013, 8, 28))

    def test_last_thursday_of_september_2013(self):
        self.assertEqual(
            meetup_day(2013, 9, 'Thursday', 'last'), date(2013, 9, 26))

    def test_last_thursday_of_october_2013(self):
        self.assertEqual(
            meetup_day(2013, 10, 'Thursday', 'last'), date(2013, 10, 31))

    def test_last_friday_of_november_2013(self):
        self.assertEqual(
            meetup_day(2013, 11, 'Friday', 'last'), date(2013, 11, 29))

    def test_last_friday_of_december_2013(self):
        self.assertEqual(
            meetup_day(2013, 12, 'Friday', 'last'), date(2013, 12, 27))

    def test_last_saturday_of_january_2013(self):
        self.assertEqual(
            meetup_day(2013, 1, 'Saturday', 'last'), date(2013, 1, 26))

    def test_last_saturday_of_february_2013(self):
        self.assertEqual(
            meetup_day(2013, 2, 'Saturday', 'last'), date(2013, 2, 23))

    def test_last_sunday_of_march_2013(self):
        self.assertEqual(
            meetup_day(2013, 3, 'Sunday', 'last'), date(2013, 3, 31))

    def test_last_sunday_of_april_2013(self):
        self.assertEqual(
            meetup_day(2013, 4, 'Sunday', 'last'), date(2013, 4, 28))

    def test_last_wednesday_of_february_2012(self):
        self.assertEqual(
            meetup_day(2012, 2, 'Wednesday', 'last'), date(2012, 2, 29))

    def test_last_wednesday_of_december_2014(self):
        self.assertEqual(
            meetup_day(2014, 12, 'Wednesday', 'last'), date(2014, 12, 31))

    def test_last_sunday_of_february_2015(self):
        self.assertEqual(
            meetup_day(2015, 2, 'Sunday', 'last'), date(2015, 2, 22))

    def test_first_friday_of_december_2012(self):
        self.assertEqual(
            meetup_day(2012, 12, 'Friday', '1st'), date(2012, 12, 7))

    # additional track specific tests
    def test_fifth_monday_of_march_2015(self):
        self.assertEqual(
            meetup_day(2015, 3, 'Monday', '5th'), date(2015, 3, 30))

    def test_nonexistent_fifth_monday_of_february_2015(self):
        with self.assertRaises(MeetupDayException):
            meetup_day(2015, 2, 'Monday', '5th')


if __name__ == '__main__':
    unittest.main()
