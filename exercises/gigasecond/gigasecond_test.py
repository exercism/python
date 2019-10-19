import unittest

from gigasecond import add

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class GigasecondTest(unittest.TestCase):
    def date_only_specification_of_time(self):
        test_value = "2011-04-25"
        expected = "2043-01-01T01:46:40"
        self.assertEqual(add(test_value), expected)

    def second_test_for_date_only_specification_of_time(self):
        test_value = "1977-06-13"
        expected = "2009-02-19T01:46:40"
        self.assertEqual(add(test_value), expected)

    def third_test_for_date_only_specification_of_time(self):
        test_value = "1959-07-19"
        expected = "1991-03-27T01:46:40"
        self.assertEqual(add(test_value), expected)

    def full_time_specified(self):
        test_value = "2015-01-24T22:00:00"
        expected = "2046-10-02T23:46:40"
        self.assertEqual(add(test_value), expected)

    def full_time_with_day_roll_over(self):
        test_value = "2015-01-24T23:59:59"
        expected = "2046-10-03T01:46:39"
        self.assertEqual(add(test_value), expected)


if __name__ == "__main__":
    unittest.main()
