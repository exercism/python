import unittest

from ocr_numbers import convert

# Tests adapted from `problem-specifications//canonical-data.json`


class OcrNumbersTest(unittest.TestCase):
    def test_recognizes_0(self):
        self.assertEqual(convert([" _ ", "| |", "|_|", "   "]), "0")

    def test_recognizes_1(self):
        self.assertEqual(convert(["   ", "  |", "  |", "   "]), "1")

    def test_unreadable_but_correctly_sized_inputs_return(self):
        self.assertEqual(convert(["   ", "  _", "  |", "   "]), "?")

    def test_input_with_a_number_of_lines_that_is_not_a_multiple_of_four_raises_an_error(
        self
    ):
        with self.assertRaisesWithMessage(ValueError):
            convert([" _ ", "| |", "   "])

    def test_input_with_a_number_of_columns_that_is_not_a_multiple_of_three_raises_an_error(
        self
    ):
        with self.assertRaisesWithMessage(ValueError):
            convert(["    ", "   |", "   |", "    "])

    def test_recognizes_110101100(self):
        self.assertEqual(
            convert(
                [
                    "       _     _        _  _ ",
                    "  |  || |  || |  |  || || |",
                    "  |  ||_|  ||_|  |  ||_||_|",
                    "                           ",
                ]
            ),
            "110101100",
        )

    def test_garbled_numbers_in_a_string_are_replaced_with(self):
        self.assertEqual(
            convert(
                [
                    "       _     _           _ ",
                    "  |  || |  || |     || || |",
                    "  |  | _|  ||_|  |  ||_||_|",
                    "                           ",
                ]
            ),
            "11?10?1?0",
        )

    def test_recognizes_2(self):
        self.assertEqual(convert([" _ ", " _|", "|_ ", "   "]), "2")

    def test_recognizes_3(self):
        self.assertEqual(convert([" _ ", " _|", " _|", "   "]), "3")

    def test_recognizes_4(self):
        self.assertEqual(convert(["   ", "|_|", "  |", "   "]), "4")

    def test_recognizes_5(self):
        self.assertEqual(convert([" _ ", "|_ ", " _|", "   "]), "5")

    def test_recognizes_6(self):
        self.assertEqual(convert([" _ ", "|_ ", "|_|", "   "]), "6")

    def test_recognizes_7(self):
        self.assertEqual(convert([" _ ", "  |", "  |", "   "]), "7")

    def test_recognizes_8(self):
        self.assertEqual(convert([" _ ", "|_|", "|_|", "   "]), "8")

    def test_recognizes_9(self):
        self.assertEqual(convert([" _ ", "|_|", " _|", "   "]), "9")

    def test_recognizes_string_of_decimal_numbers(self):
        self.assertEqual(
            convert(
                [
                    "    _  _     _  _  _  _  _  _ ",
                    "  | _| _||_||_ |_   ||_||_|| |",
                    "  ||_  _|  | _||_|  ||_| _||_|",
                    "                              ",
                ]
            ),
            "1234567890",
        )

    def test_numbers_separated_by_empty_lines_are_recognized_lines_are_joined_by_commas(
        self
    ):
        self.assertEqual(
            convert(
                [
                    "    _  _ ",
                    "  | _| _|",
                    "  ||_  _|",
                    "         ",
                    "    _  _ ",
                    "|_||_ |_ ",
                    "  | _||_|",
                    "         ",
                    " _  _  _ ",
                    "  ||_||_|",
                    "  ||_| _|",
                    "         ",
                ]
            ),
            "123,456,789",
        )

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
