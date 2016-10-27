import unittest

from say import say


class SayTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual("one", say(1))

    def test_fourteen(self):
        self.assertEqual("fourteen", say(14))

    def test_twenty(self):
        self.assertEqual("twenty", say(20))

    def test_twenty_two(self):
        self.assertEqual("twenty-two", say(22))

    def test_one_hundred(self):
        self.assertEqual("one hundred", say(100))

    def test_one_hundred_twenty(self):
        self.assertEqual("one hundred and twenty", say(120))

    def test_one_hundred_twenty_three(self):
        self.assertEqual("one hundred and twenty-three", say(123))

    def test_one_thousand(self):
        self.assertEqual("one thousand", say(1000))

    def test_one_thousand_two_hundred_thirty_four(self):
        self.assertEqual("one thousand two hundred and thirty-four",
                         say(1234))

    def test_one_million(self):
        self.assertEqual("one million", say(1e6))

    def test_one_million_two(self):
        self.assertEqual("one million and two", say(1000002))

    def test_1002345(self):
        self.assertEqual(
            "one million two thousand three hundred and forty-five",
            say(1002345))

    def test_one_billion(self):
        self.assertEqual("one billion", say(1e9))

    def test_number_to_large(self):
        with self.assertRaises(AttributeError):
            say(1e12)

    def test_number_negative(self):
        with self.assertRaises(AttributeError):
            say(-42)

    def test_zero(self):
        self.assertEqual("zero", say(0))

    def test_987654321123(self):
        self.assertEqual("nine hundred and eighty-seven billion " +
                         "six hundred and fifty-four million " +
                         "three hundred and twenty-one thousand " +
                         "one hundred and twenty-three",
                         say(987654321123))

if __name__ == '__main__':
    unittest.main()
