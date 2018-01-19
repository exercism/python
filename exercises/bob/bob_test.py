import unittest

import bob


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class BobTests(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(bob.hey("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(bob.hey("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(bob.hey("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            bob.hey("Does this cryogenic chamber make me look fat?"), "Sure.")

    def test_asking_a_numeric_question(self):
        self.assertEqual(bob.hey("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(bob.hey("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(
            bob.hey("Let's go make out behind the gym!"), "Whatever.")

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            bob.hey("It's OK if you don't want to go to the DMV."),
            "Whatever.")

    def test_forceful_question(self):
        self.assertEqual(
            bob.hey("WHAT THE HELL WERE YOU THINKING?"),
            "Calm down, I know what I'm doing!"
        )

    def test_shouting_numbers(self):
        self.assertEqual(bob.hey("1, 2, 3 GO!"), "Whoa, chill out!")

    def test_only_numbers(self):
        self.assertEqual(bob.hey("1, 2, 3"), "Whatever.")

    def test_question_with_only_numbers(self):
        self.assertEqual(bob.hey("4?"), "Sure.")

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            bob.hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!")

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(bob.hey("I HATE YOU"), "Whoa, chill out!")

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            bob.hey("Ending with ? means a question."), "Whatever.")

    def test_non_letters_with_question(self):
        self.assertEqual(bob.hey(":) ?"), "Sure.")

    def test_prattling_on(self):
        self.assertEqual(
            bob.hey("Wait! Hang on. Are you going to be OK?"), "Sure.")

    def test_silence(self):
        self.assertEqual(bob.hey(""), "Fine. Be that way!")

    def test_prolonged_silence(self):
        self.assertEqual(bob.hey("          "), "Fine. Be that way!")

    def test_alternate_silence(self):
        self.assertEqual(bob.hey("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    def test_multiple_line_question(self):
        self.assertEqual(
            bob.hey("\nDoes this cryogenic chamber make me look fat?\nno"),
            "Whatever.")

    def test_starting_with_whitespace(self):
        self.assertEqual(bob.hey("         hmmmmmmm..."), "Whatever.")

    def test_ending_with_whitespace(self):
        self.assertEqual(
            bob.hey("Okay if like my  spacebar  quite a bit?   "), "Sure.")

    def test_other_whitespace(self):
        self.assertEqual(bob.hey("\n\r \t"), "Fine. Be that way!")

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            bob.hey("This is a statement ending with whitespace      "),
            "Whatever.")


if __name__ == '__main__':
    unittest.main()
