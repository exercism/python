import unittest

from isbn_verifier import verify, isbn_generator, isbn13_generator_from_isbn10


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class IsbnVerifierTests(unittest.TestCase):

    def test_valid_isbn(self):
        self.assertIs(verify('3-598-21508-8'), True)

    def test_invalid_check_digit(self):
        self.assertIs(verify('3-598-21508-9'), False)

    def test_valid_with_X_check_digit(self):
        self.assertIs(verify('3-598-21507-X'), True)

    def test_invalid_check_digit_other_than_X(self):
        self.assertIs(verify('3-598-21507-A'), False)

    def test_invalid_character_in_isbn(self):
        self.assertIs(verify('3-598-2K507-0'), False)

    def test_invalid_X_other_than_check_digit(self):
        self.assertIs(verify('3-598-2X507-0'), False)

    def test_valid_isbn_without_separating_dashes(self):
        self.assertIs(verify('3598215088'), True)

    def test_valid_isbn_without_separating_dashes_with_X_check_digit(self):
        self.assertIs(verify('359821507X'), True)

    def test_invalid_isbn_without_check_digit_and_dashes(self):
        self.assertIs(verify('359821507'), False)

    def test_invalid_too_long_isbn_with_no_dashes(self):
        self.assertIs(verify('3598215078X'), False)

    def test_invalid_isbn_without_check_digit(self):
        self.assertIs(verify('3-598-21507'), False)

    def test_invalid_too_long_isbn(self):
        self.assertIs(verify('3-598-21507-XA'), False)

    def test_invalid_check_digit_X_used_for_0(self):
        self.assertIs(verify('3-598-21515-X'), False)


class IsbnGeneratorTests(unittest.TestCase):

    def test_valid_isbn(self):
        self.assertEqual(isbn_generator('3-598-21508-8'), '3-598-21508-8')

    def test_valid_isbn_without_separating_dashes_with_X_check_digit(self):
        self.assertEqual(isbn_generator('359821507X'), '3-598-21507-X')

    def test_valid_isbn_without_check_digit(self):
        self.assertEqual(isbn_generator('359821508'), '3-598-21508-8')

    def test_invalid_isbn_too_short(self):
        with self.assertRaises(Exception):
            isbn_generator('3-598-2350')

    def test_invalid_isbn_too_long(self):
        with self.assertRaises(Exception):
            isbn_generator('359723508XA')


class Isbn13GeneratorTests(unittest.TestCase):

    def test_valid_isbn(self):
        self.assertEqual(isbn13_generator_from_isbn10(
            '3-598-21508-8'), '978-3-59-821508-7')

    def test_valid_isbn_without_separating_dashes_with_X_check_digit(self):
        self.assertEqual(isbn13_generator_from_isbn10(
            '359821507X'), '978-3-59-821507-0')

    def test_invalid_isbn_too_short(self):
        with self.assertRaises(Exception):
            isbn13_generator_from_isbn10('3-598-23506')

    def test_invalid_isbn_too_long(self):
        with self.assertRaises(Exception):
            isbn13_generator_from_isbn10('3597235089X')


if __name__ == '__main__':
    unittest.main()
