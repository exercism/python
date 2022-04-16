"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - is the sentence punctuated correctly?
    """

    return sentence.endswith(".")


def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    clean_sentence = sentence.strip()
    return clean_sentence


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    better_sentence = sentence.replace(old_word, new_word)
    return better_sentence
