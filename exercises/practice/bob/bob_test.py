from bob import (
    response,
)

# Tests adapted from `problem-specifications//canonical-data.json`


def test_stating_something():
    assert response("Tom-ay-to, tom-aaaah-to.") == "Whatever."


def test_shouting():
    response("WATCH OUT!") == "Whoa, chill out!"


def test_shouting_gibberish():
    response("FCECDFCAAB") == "Whoa, chill out!"


def test_asking_a_question():

    response("Does this cryogenic chamber make me look fat?") == "Sure."


def test_asking_a_numeric_question():
    response("You are, what, like 15?") == "Sure."


def test_asking_gibberish():
    response("fffbbcbeab?") == "Sure."


def test_talking_forcefully():
    response("Hi there!") == "Whatever."


def test_using_acronyms_in_regular_speech():

    response("It's OK if you don't want to go work for NASA.") == "Whatever."


def test_forceful_question():

    response("WHAT'S GOING ON?") == "Calm down, I know what I'm doing!"


def test_shouting_numbers():
    response("1, 2, 3 GO!") == "Whoa, chill out!"


def test_no_letters():
    response("1, 2, 3") == "Whatever."


def test_question_with_no_letters():
    response("4?") == "Sure."


def test_shouting_with_special_characters():
    response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!") == "Whoa, chill out!",


def test_shouting_with_no_exclamation_mark():
    response("I HATE THE DENTIST") == "Whoa, chill out!"


def test_statement_containing_question_mark():
    response("Ending with ? means a question.") == "Whatever."


def test_non_letters_with_question():
    response(":) ?") == "Sure."


def test_prattling_on():
    response("Wait! Hang on. Are you going to be OK?") == "Sure."


def test_silence():
    response("") == "Fine. Be that way!"


def test_prolonged_silence():
    response("          ") == "Fine. Be that way!"


def test_alternate_silence():
    response("\t\t\t\t\t\t\t\t\t\t") == "Fine. Be that way!"


def test_multiple_line_question():
    response("\nDoes this cryogenic chamber make me look fat?\nNo.") == "Whatever.",


def test_starting_with_whitespace():
    response("         hmmmmmmm...") == "Whatever."


def test_ending_with_whitespace():
    response("Okay if like my  spacebar  quite a bit?   ") == "Sure."


def test_other_whitespace():
    response("\n\r \t") == "Fine. Be that way!"


def test_non_question_ending_with_whitespace():
    response("This is a statement ending with whitespace      ") == "Whatever."
