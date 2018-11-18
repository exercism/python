import unittest

from bob import hey


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.4.0

class BobTest(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual("Whatever.", hey("Tom-ay-to, tom-aaaah-to."))

    def test_shouting(self):
        self.assertEqual("Whoa, chill out!", hey("WATCH OUT!"))

    def test_shouting_gibberish(self):
        self.assertEqual("Whoa, chill out!", hey("FCECDFCAAB"))

    def test_asking_a_question(self):
        self.assertEqual(
            "Sure.", hey("Does this cryogenic chamber make me look fat?"))

    def test_asking_a_numeric_question(self):
        self.assertEqual("Sure.", hey("You are, what, like 15?"))

    def test_asking_gibberish(self):
        self.assertEqual("Sure.", hey("fffbbcbeab?"))

    def test_talking_forcefully(self):
        self.assertEqual(
            "Whatever.", hey("Let's go make out behind the gym!"))

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            "Whatever.",
            hey("It's OK if you don't want to go to the DMV."))

    def test_forceful_question(self):
        self.assertEqual(
            "Calm down, I know what I'm doing!",
            hey("WHAT THE HELL WERE YOU THINKING?"))

    def test_shouting_numbers(self):
        self.assertEqual("Whoa, chill out!", hey("1, 2, 3 GO!"))

    def test_no_letters(self):
        self.assertEqual("Whatever.", hey("1, 2, 3"))

    def test_question_with_no_letters(self):
        self.assertEqual("Sure.", hey("4?"))

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            "Whoa, chill out!",
            hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"))

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual("Whoa, chill out!", hey("I HATE THE DMV"))

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            "Whatever.", hey("Ending with ? means a question."))

    def test_non_letters_with_question(self):
        self.assertEqual("Sure.", hey(":) ?"))

    def test_prattling_on(self):
        self.assertEqual(
            "Sure.", hey("Wait! Hang on. Are you going to be OK?"))

    def test_silence(self):
        self.assertEqual("Fine. Be that way!", hey(""))

    def test_prolonged_silence(self):
        self.assertEqual("Fine. Be that way!", hey("          "))

    def test_alternate_silence(self):
        self.assertEqual("Fine. Be that way!", hey("\t\t\t\t\t\t\t\t\t\t"))

    def test_multiple_line_question(self):
        self.assertEqual(
            "Whatever.",
            hey("\nDoes this cryogenic chamber make me look fat?\nNo."))

    def test_starting_with_whitespace(self):
        self.assertEqual("Whatever.", hey("         hmmmmmmm..."))

    def test_ending_with_whitespace(self):
        self.assertEqual(
            "Sure.", hey("Okay if like my  spacebar  quite a bit?   "))

    def test_other_whitespace(self):
        self.assertEqual("Fine. Be that way!", hey("\n\r \t"))

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            "Whatever.",
            hey("This is a statement ending with whitespace      "),)


if __name__ == '__main__':
    unittest.main()
