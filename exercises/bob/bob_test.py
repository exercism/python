import unittest

from bob import hey


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

class BobTest(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(hey("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(hey("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(hey("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            hey("Does this cryogenic chamber make me look fat?"), "Sure.")

    def test_asking_a_numeric_question(self):
        self.assertEqual(hey("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(hey("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(
            hey("Let's go make out behind the gym!"), "Whatever.")

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            hey("It's OK if you don't want to go to the DMV."),
            "Whatever.")

    def test_forceful_question(self):
        self.assertEqual(
            hey("WHAT THE HELL WERE YOU THINKING?"),
            "Calm down, I know what I'm doing!"
        )

    def test_shouting_numbers(self):
        self.assertEqual(hey("1, 2, 3 GO!"), "Whoa, chill out!")

    def test_no_letters(self):
        self.assertEqual(hey("1, 2, 3"), "Whatever.")

    def test_question_with_no_letters(self):
        self.assertEqual(hey("4?"), "Sure.")

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!")

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(hey("I HATE THE DMV"), "Whoa, chill out!")

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            hey("Ending with ? means a question."), "Whatever.")

    def test_non_letters_with_question(self):
        self.assertEqual(hey(":) ?"), "Sure.")

    def test_prattling_on(self):
        self.assertEqual(
            hey("Wait! Hang on. Are you going to be OK?"), "Sure.")

    def test_silence(self):
        self.assertEqual(hey(""), "Fine. Be that way!")

    def test_prolonged_silence(self):
        self.assertEqual(hey("          "), "Fine. Be that way!")

    def test_alternate_silence(self):
        self.assertEqual(hey("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    def test_multiple_line_question(self):
        self.assertEqual(
            hey("\nDoes this cryogenic chamber make me look fat?\nNo."),
            "Whatever.")

    def test_starting_with_whitespace(self):
        self.assertEqual(hey("         hmmmmmmm..."), "Whatever.")

    def test_ending_with_whitespace(self):
        self.assertEqual(
            hey("Okay if like my  spacebar  quite a bit?   "), "Sure.")

    def test_other_whitespace(self):
        self.assertEqual(hey("\n\r \t"), "Fine. Be that way!")

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            hey("This is a statement ending with whitespace      "),
            "Whatever.")


if __name__ == '__main__':
    unittest.main()
