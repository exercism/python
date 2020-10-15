import unittest

from bob import response

# Tests adapted from `problem-specifications//canonical-data.json`


class BobTest(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(response("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(response("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(response("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            response("Does this cryogenic chamber make me look fat?"), "Sure."
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(response("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(response("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(response("Hi there!"), "Whatever.")

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            response("It's OK if you don't want to go work for NASA."), "Whatever."
        )

    def test_forceful_question(self):
        self.assertEqual(
            response("WHAT'S GOING ON?"), "Calm down, I know what I'm doing!"
        )

    def test_shouting_numbers(self):
        self.assertEqual(response("1, 2, 3 GO!"), "Whoa, chill out!")

    def test_no_letters(self):
        self.assertEqual(response("1, 2, 3"), "Whatever.")

    def test_question_with_no_letters(self):
        self.assertEqual(response("4?"), "Sure.")

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!",
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(response("I HATE THE DENTIST"), "Whoa, chill out!")

    def test_statement_containing_question_mark(self):
        self.assertEqual(response("Ending with ? means a question."), "Whatever.")

    def test_non_letters_with_question(self):
        self.assertEqual(response(":) ?"), "Sure.")

    def test_prattling_on(self):
        self.assertEqual(response("Wait! Hang on. Are you going to be OK?"), "Sure.")

    def test_silence(self):
        self.assertEqual(response(""), "Fine. Be that way!")

    def test_prolonged_silence(self):
        self.assertEqual(response("          "), "Fine. Be that way!")

    def test_alternate_silence(self):
        self.assertEqual(response("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    def test_multiple_line_question(self):
        self.assertEqual(
            response("\nDoes this cryogenic chamber make me look fat?\nNo."),
            "Whatever.",
        )

    def test_starting_with_whitespace(self):
        self.assertEqual(response("         hmmmmmmm..."), "Whatever.")

    def test_ending_with_whitespace(self):
        self.assertEqual(
            response("Okay if like my  spacebar  quite a bit?   "), "Sure."
        )

    def test_other_whitespace(self):
        self.assertEqual(response("\n\r \t"), "Fine. Be that way!")

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            response("This is a statement ending with whitespace      "), "Whatever."
        )


if __name__ == "__main__":
    unittest.main()
