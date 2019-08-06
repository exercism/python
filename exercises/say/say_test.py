import unittest

from say import say


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class SayTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(say(0), "zero")

    def test_one(self):
        self.assertEqual(say(1), "one")

    def test_fourteen(self):
        self.assertEqual(say(14), "fourteen")

    def test_twenty(self):
        self.assertEqual(say(20), "twenty")

    def test_twenty_two(self):
        self.assertEqual(say(22), "twenty-two")

    def test_one_hundred(self):
        self.assertEqual(say(100), "one hundred")

    # additional track specific test
    def test_one_hundred_twenty_three(self):
        self.assertEqual(say(123), "one hundred and twenty-three")

    def test_one_thousand(self):
        self.assertEqual(say(1000), "one thousand")

    def test_one_thousand_two_hundred_thirty_four(self):
        self.assertEqual(say(1234), "one thousand two hundred and thirty-four")

    def test_one_million(self):
        self.assertEqual(say(1000000), "one million")

    def test_1002345(self):
        self.assertEqual(
            say(1002345),
            "one million two thousand three hundred and forty-five")

    def test_one_billion(self):
        self.assertEqual(say(1000000000), "one billion")

    def test_987654321123(self):
        self.assertEqual(
            say(987654321123), ("nine hundred and eighty-seven billion "
                                "six hundred and fifty-four million "
                                "three hundred and twenty-one thousand "
                                "one hundred and twenty-three"))

    def test_number_too_large(self):
        with self.assertRaisesWithMessage(ValueError):
            say(1000000000000)

    def test_number_negative(self):
        with self.assertRaisesWithMessage(ValueError):
            say(-1)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
