import unittest

from twelve_days import sing, verse, verses


class TwelveDaysTests(unittest.TestCase):
    def test_verse1(self):
        expected = ("On the first day of Christmas my true love gave to me, "
                    "a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(1), expected)

    def test_verse2(self):
        expected = ("On the second day of Christmas my true love gave to me, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(2), expected)

    def test_verse3(self):
        expected = ("On the third day of Christmas my true love gave to me, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(3), expected)

    def test_verse4(self):
        expected = ("On the fourth day of Christmas my true love gave to me, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(4), expected)

    def test_verse5(self):
        expected = ("On the fifth day of Christmas my true love gave to me, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(5), expected)

    def test_verse6(self):
        expected = ("On the sixth day of Christmas my true love gave to me, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(6), expected)

    def test_verse7(self):
        expected = ("On the seventh day of Christmas my true love gave to me, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(7), expected)

    def test_verse8(self):
        expected = ("On the eighth day of Christmas my true love gave to me, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(8), expected)

    def test_verse9(self):
        expected = ("On the ninth day of Christmas my true love gave to me, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(9), expected)

    def test_verse10(self):
        expected = ("On the tenth day of Christmas my true love gave to me, "
                    "ten Lords-a-Leaping, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(10), expected)

    def test_verse11(self):
        expected = ("On the eleventh day of Christmas "
                    "my true love gave to me, "
                    "eleven Pipers Piping, "
                    "ten Lords-a-Leaping, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(11), expected)

    def test_verse12(self):
        expected = ("On the twelfth day of Christmas my true love gave to me, "
                    "twelve Drummers Drumming, "
                    "eleven Pipers Piping, "
                    "ten Lords-a-Leaping, "
                    "nine Ladies Dancing, "
                    "eight Maids-a-Milking, "
                    "seven Swans-a-Swimming, "
                    "six Geese-a-Laying, "
                    "five Gold Rings, "
                    "four Calling Birds, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n")
        self.assertEqual(verse(12), expected)

    def test_multiple_verses(self):
        expected = ("On the first day of Christmas my true love gave to me, "
                    "a Partridge in a Pear Tree.\n\n"
                    "On the second day of Christmas my true love gave to me, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n\n"
                    "On the third day of Christmas my true love gave to me, "
                    "three French Hens, "
                    "two Turtle Doves, "
                    "and a Partridge in a Pear Tree.\n\n")
        self.assertEqual(verses(1, 3), expected)

    def test_the_whole_song(self):
        self.assertEqual(verses(1, 12), sing())


if __name__ == '__main__':
    unittest.main()
