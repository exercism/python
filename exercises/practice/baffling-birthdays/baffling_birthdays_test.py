# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/baffling-birthdays/canonical-data.json
# File last updated on 2026-03-28

import unittest

from baffling_birthdays import (
    estimated_probability_of_shared_birthday,
    random_birthdates,
    shared_birthday,
)

from calendar import isleap


class BafflingBirthdaysTest(unittest.TestCase):
    # shared birthday

    def test_one_birthdate(self):
        self.assertIs(shared_birthday(["2000-01-01"]), False)

    def test_two_birthdates_with_same_year_month_and_day(self):
        self.assertIs(shared_birthday(["2000-01-01", "2000-01-01"]), True)

    def test_two_birthdates_with_same_year_and_month_but_different_day(self):
        self.assertIs(shared_birthday(["2012-05-09", "2012-05-17"]), False)

    def test_two_birthdates_with_same_month_and_day_but_different_year(self):
        self.assertIs(shared_birthday(["1999-10-23", "1988-10-23"]), True)

    def test_two_birthdates_with_same_year_but_different_month_and_day(self):
        self.assertIs(shared_birthday(["2007-12-19", "2007-04-27"]), False)

    def test_two_birthdates_with_different_year_month_and_day(self):
        self.assertIs(shared_birthday(["1997-08-04", "1963-11-23"]), False)

    def test_multiple_birthdates_without_shared_birthday(self):
        self.assertIs(
            shared_birthday(["1966-07-29", "1977-02-12", "2001-12-25", "1980-11-10"]),
            False,
        )

    def test_multiple_birthdates_with_one_shared_birthday(self):
        self.assertIs(
            shared_birthday(["1966-07-29", "1977-02-12", "2001-07-29", "1980-11-10"]),
            True,
        )

    def test_multiple_birthdates_with_more_than_one_shared_birthday(self):
        self.assertIs(
            shared_birthday(
                ["1966-07-29", "1977-02-12", "2001-12-25", "1980-07-29", "2019-02-12"]
            ),
            True,
        )

    # random birthdates

    def test_random_birthdates_generate_requested_number_of_birthdates(self):
        self.assertTrue(
            all(
                len(random_birthdates(groupsize)) == groupsize
                for groupsize in range(1, 20)
            )
        )

    def test_random_birthdates_are_not_in_leap_years(self):
        self.assertFalse(
            any([isleap(randyear.year) for randyear in random_birthdates(100)])
        )

    def test_random_birthdates_appear_random(self):
        birthdates = random_birthdates(500)
        months = set([bdate.month for bdate in birthdates])
        days = set([bdate.day for bdate in birthdates])
        self.assertTrue(len(months) >= 10)
        self.assertTrue(len(days) >= 28)

    # estimated probability of at least one shared birthday

    def test_for_one_person(self):

        self.assertAlmostEqual(
            estimated_probability_of_shared_birthday(1), 0.0, delta=0.1
        )

    def test_among_ten_people(self):

        self.assertAlmostEqual(
            estimated_probability_of_shared_birthday(10), 0.11694818, delta=0.5
        )

    def test_among_twenty_three_people(self):

        self.assertAlmostEqual(
            estimated_probability_of_shared_birthday(23), 0.50729723, delta=0.5
        )

    def test_among_seventy_people(self):

        self.assertAlmostEqual(
            estimated_probability_of_shared_birthday(70), 0.99915958, delta=0.1
        )
