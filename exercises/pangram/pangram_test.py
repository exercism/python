import unittest

from pangram import is_pangram

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class PangramTest(unittest.TestCase):
    def test_empty_sentence(self):
        self.assertIs(is_pangram(""), False)

    def test_perfect_lower_case(self):
        self.assertIs(is_pangram("abcdefghijklmnopqrstuvwxyz"), True)

    def test_only_lower_case(self):
        self.assertIs(is_pangram("the quick brown fox jumps over the lazy dog"), True)

    def test_missing_the_letter_x(self):
        self.assertIs(
            is_pangram("a quick movement of the enemy will jeopardize five gunboats"),
            False,
        )

    def test_missing_the_letter_h(self):
        self.assertIs(is_pangram("five boxing wizards jump quickly at it"), False)

    def test_with_underscores(self):
        self.assertIs(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True)

    def test_with_numbers(self):
        self.assertIs(
            is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True
        )

    def test_missing_letters_replaced_by_numbers(self):
        self.assertIs(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False)

    def test_mixed_case_and_punctuation(self):
        self.assertIs(is_pangram('"Five quacking Zephyrs jolt my wax bed."'), True)

    def test_case_insensitive(self):
        self.assertIs(is_pangram("the quick brown fox jumps over with lazy FX"), False)


if __name__ == "__main__":
    unittest.main()
