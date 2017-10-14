import unittest

from say import say


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

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
    def test_one_hundred_twenty(self):
        self.assertEqual(say(120), "one hundred and twenty")

    def test_one_hundred_twenty_three(self):
        self.assertEqual(say(123), "one hundred and twenty-three")

    def test_one_thousand(self):
        self.assertEqual(say(1000), "one thousand")

    def test_one_thousand_two_hundred_thirty_four(self):
        self.assertEqual(say(1234), "one thousand two hundred and thirty-four")

    # additional track specific test
    def test_eight_hundred_and_ten_thousand(self):
        self.assertEqual(say(810000), "eight hundred and ten thousand")

    def test_one_million(self):
        self.assertEqual(say(1e6), "one million")

    # additional track specific test
    def test_one_million_two(self):
        self.assertEqual(say(1000002), "one million and two")

    def test_1002345(self):
        self.assertEqual(
            say(1002345),
            "one million two thousand three hundred and forty-five")

    def test_one_billion(self):
        self.assertEqual(say(1e9), "one billion")

    def test_987654321123(self):
        self.assertEqual(
            say(987654321123), ("nine hundred and eighty-seven billion "
                                "six hundred and fifty-four million "
                                "three hundred and twenty-one thousand "
                                "one hundred and twenty-three"))

    def test_number_to_large(self):
        with self.assertRaises(AttributeError):
            say(1e12)

    def test_number_negative(self):
        with self.assertRaises(AttributeError):
            say(-1)


if __name__ == '__main__':
    unittest.main()
