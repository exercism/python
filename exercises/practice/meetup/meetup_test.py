from datetime import date
import unittest

from meetup import (
    meetup,
    MeetupDayException,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class MeetupTest(unittest.TestCase):
    def test_monteenth_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "teenth", "Monday"), date(2013, 5, 13))

    def test_monteenth_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "teenth", "Monday"), date(2013, 8, 19))

    def test_monteenth_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "teenth", "Monday"), date(2013, 9, 16))

    def test_tuesteenth_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "teenth", "Tuesday"), date(2013, 3, 19))

    def test_tuesteenth_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "teenth", "Tuesday"), date(2013, 4, 16))

    def test_tuesteenth_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "teenth", "Tuesday"), date(2013, 8, 13))

    def test_wednesteenth_of_january_2013(self):
        self.assertEqual(meetup(2013, 1, "teenth", "Wednesday"), date(2013, 1, 16))

    def test_wednesteenth_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "teenth", "Wednesday"), date(2013, 2, 13))

    def test_wednesteenth_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "teenth", "Wednesday"), date(2013, 6, 19))

    def test_thursteenth_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "teenth", "Thursday"), date(2013, 5, 16))

    def test_thursteenth_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "teenth", "Thursday"), date(2013, 6, 13))

    def test_thursteenth_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "teenth", "Thursday"), date(2013, 9, 19))

    def test_friteenth_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "teenth", "Friday"), date(2013, 4, 19))

    def test_friteenth_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "teenth", "Friday"), date(2013, 8, 16))

    def test_friteenth_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "teenth", "Friday"), date(2013, 9, 13))

    def test_saturteenth_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "teenth", "Saturday"), date(2013, 2, 16))

    def test_saturteenth_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "teenth", "Saturday"), date(2013, 4, 13))

    def test_saturteenth_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "teenth", "Saturday"), date(2013, 10, 19))

    def test_sunteenth_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "teenth", "Sunday"), date(2013, 5, 19))

    def test_sunteenth_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "teenth", "Sunday"), date(2013, 6, 16))

    def test_sunteenth_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "teenth", "Sunday"), date(2013, 10, 13))

    def test_first_monday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "first", "Monday"), date(2013, 3, 4))

    def test_first_monday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "first", "Monday"), date(2013, 4, 1))

    def test_first_tuesday_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "first", "Tuesday"), date(2013, 5, 7))

    def test_first_tuesday_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "first", "Tuesday"), date(2013, 6, 4))

    def test_first_wednesday_of_july_2013(self):
        self.assertEqual(meetup(2013, 7, "first", "Wednesday"), date(2013, 7, 3))

    def test_first_wednesday_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "first", "Wednesday"), date(2013, 8, 7))

    def test_first_thursday_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "first", "Thursday"), date(2013, 9, 5))

    def test_first_thursday_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "first", "Thursday"), date(2013, 10, 3))

    def test_first_friday_of_november_2013(self):
        self.assertEqual(meetup(2013, 11, "first", "Friday"), date(2013, 11, 1))

    def test_first_friday_of_december_2013(self):
        self.assertEqual(meetup(2013, 12, "first", "Friday"), date(2013, 12, 6))

    def test_first_saturday_of_january_2013(self):
        self.assertEqual(meetup(2013, 1, "first", "Saturday"), date(2013, 1, 5))

    def test_first_saturday_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "first", "Saturday"), date(2013, 2, 2))

    def test_first_sunday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "first", "Sunday"), date(2013, 3, 3))

    def test_first_sunday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "first", "Sunday"), date(2013, 4, 7))

    def test_second_monday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "second", "Monday"), date(2013, 3, 11))

    def test_second_monday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "second", "Monday"), date(2013, 4, 8))

    def test_second_tuesday_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "second", "Tuesday"), date(2013, 5, 14))

    def test_second_tuesday_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "second", "Tuesday"), date(2013, 6, 11))

    def test_second_wednesday_of_july_2013(self):
        self.assertEqual(meetup(2013, 7, "second", "Wednesday"), date(2013, 7, 10))

    def test_second_wednesday_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "second", "Wednesday"), date(2013, 8, 14))

    def test_second_thursday_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "second", "Thursday"), date(2013, 9, 12))

    def test_second_thursday_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "second", "Thursday"), date(2013, 10, 10))

    def test_second_friday_of_november_2013(self):
        self.assertEqual(meetup(2013, 11, "second", "Friday"), date(2013, 11, 8))

    def test_second_friday_of_december_2013(self):
        self.assertEqual(meetup(2013, 12, "second", "Friday"), date(2013, 12, 13))

    def test_second_saturday_of_january_2013(self):
        self.assertEqual(meetup(2013, 1, "second", "Saturday"), date(2013, 1, 12))

    def test_second_saturday_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "second", "Saturday"), date(2013, 2, 9))

    def test_second_sunday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "second", "Sunday"), date(2013, 3, 10))

    def test_second_sunday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "second", "Sunday"), date(2013, 4, 14))

    def test_third_monday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "third", "Monday"), date(2013, 3, 18))

    def test_third_monday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "third", "Monday"), date(2013, 4, 15))

    def test_third_tuesday_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "third", "Tuesday"), date(2013, 5, 21))

    def test_third_tuesday_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "third", "Tuesday"), date(2013, 6, 18))

    def test_third_wednesday_of_july_2013(self):
        self.assertEqual(meetup(2013, 7, "third", "Wednesday"), date(2013, 7, 17))

    def test_third_wednesday_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "third", "Wednesday"), date(2013, 8, 21))

    def test_third_thursday_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "third", "Thursday"), date(2013, 9, 19))

    def test_third_thursday_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "third", "Thursday"), date(2013, 10, 17))

    def test_third_friday_of_november_2013(self):
        self.assertEqual(meetup(2013, 11, "third", "Friday"), date(2013, 11, 15))

    def test_third_friday_of_december_2013(self):
        self.assertEqual(meetup(2013, 12, "third", "Friday"), date(2013, 12, 20))

    def test_third_saturday_of_january_2013(self):
        self.assertEqual(meetup(2013, 1, "third", "Saturday"), date(2013, 1, 19))

    def test_third_saturday_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "third", "Saturday"), date(2013, 2, 16))

    def test_third_sunday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "third", "Sunday"), date(2013, 3, 17))

    def test_third_sunday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "third", "Sunday"), date(2013, 4, 21))

    def test_fourth_monday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "fourth", "Monday"), date(2013, 3, 25))

    def test_fourth_monday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "fourth", "Monday"), date(2013, 4, 22))

    def test_fourth_tuesday_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "fourth", "Tuesday"), date(2013, 5, 28))

    def test_fourth_tuesday_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "fourth", "Tuesday"), date(2013, 6, 25))

    def test_fourth_wednesday_of_july_2013(self):
        self.assertEqual(meetup(2013, 7, "fourth", "Wednesday"), date(2013, 7, 24))

    def test_fourth_wednesday_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "fourth", "Wednesday"), date(2013, 8, 28))

    def test_fourth_thursday_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "fourth", "Thursday"), date(2013, 9, 26))

    def test_fourth_thursday_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "fourth", "Thursday"), date(2013, 10, 24))

    def test_fourth_friday_of_november_2013(self):
        self.assertEqual(meetup(2013, 11, "fourth", "Friday"), date(2013, 11, 22))

    def test_fourth_friday_of_december_2013(self):
        self.assertEqual(meetup(2013, 12, "fourth", "Friday"), date(2013, 12, 27))

    def test_fourth_saturday_of_january_2013(self):
        self.assertEqual(meetup(2013, 1, "fourth", "Saturday"), date(2013, 1, 26))

    def test_fourth_saturday_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "fourth", "Saturday"), date(2013, 2, 23))

    def test_fourth_sunday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "fourth", "Sunday"), date(2013, 3, 24))

    def test_fourth_sunday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "fourth", "Sunday"), date(2013, 4, 28))

    def test_last_monday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "last", "Monday"), date(2013, 3, 25))

    def test_last_monday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "last", "Monday"), date(2013, 4, 29))

    def test_last_tuesday_of_may_2013(self):
        self.assertEqual(meetup(2013, 5, "last", "Tuesday"), date(2013, 5, 28))

    def test_last_tuesday_of_june_2013(self):
        self.assertEqual(meetup(2013, 6, "last", "Tuesday"), date(2013, 6, 25))

    def test_last_wednesday_of_july_2013(self):
        self.assertEqual(meetup(2013, 7, "last", "Wednesday"), date(2013, 7, 31))

    def test_last_wednesday_of_august_2013(self):
        self.assertEqual(meetup(2013, 8, "last", "Wednesday"), date(2013, 8, 28))

    def test_last_thursday_of_september_2013(self):
        self.assertEqual(meetup(2013, 9, "last", "Thursday"), date(2013, 9, 26))

    def test_last_thursday_of_october_2013(self):
        self.assertEqual(meetup(2013, 10, "last", "Thursday"), date(2013, 10, 31))

    def test_last_friday_of_november_2013(self):
        self.assertEqual(meetup(2013, 11, "last", "Friday"), date(2013, 11, 29))

    def test_last_friday_of_december_2013(self):
        self.assertEqual(meetup(2013, 12, "last", "Friday"), date(2013, 12, 27))

    def test_last_saturday_of_january_2013(self):
        self.assertEqual(meetup(2013, 1, "last", "Saturday"), date(2013, 1, 26))

    def test_last_saturday_of_february_2013(self):
        self.assertEqual(meetup(2013, 2, "last", "Saturday"), date(2013, 2, 23))

    def test_last_sunday_of_march_2013(self):
        self.assertEqual(meetup(2013, 3, "last", "Sunday"), date(2013, 3, 31))

    def test_last_sunday_of_april_2013(self):
        self.assertEqual(meetup(2013, 4, "last", "Sunday"), date(2013, 4, 28))

    def test_last_wednesday_of_february_2012(self):
        self.assertEqual(meetup(2012, 2, "last", "Wednesday"), date(2012, 2, 29))

    def test_last_wednesday_of_december_2014(self):
        self.assertEqual(meetup(2014, 12, "last", "Wednesday"), date(2014, 12, 31))

    def test_last_sunday_of_february_2015(self):
        self.assertEqual(meetup(2015, 2, "last", "Sunday"), date(2015, 2, 22))

    def test_first_friday_of_december_2012(self):
        self.assertEqual(meetup(2012, 12, "first", "Friday"), date(2012, 12, 7))

    # Additional tests for this track

    def test_fifth_monday_of_march_2015(self):
        self.assertEqual(meetup(2015, 3, "fifth", "Monday"), date(2015, 3, 30))

    def test_nonexistent_fifth_monday_of_february_2015(self):
        with self.assertRaisesWithMessage(MeetupDayException):
            meetup(2015, 2, "fifth", "Monday")

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
