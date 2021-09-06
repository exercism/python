def capitalize_title(title):
    """

    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """

    return title.title()


def check_sentence_ending(sentence):
    """

    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """

    return sentence.endswith(".")


def clean_up_spacing(sentence):
    """

    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """

    clean_sentence = sentence.strip()
    return clean_sentence


def replace_word_choice(sentence, new_word, old_word):
    """

    :param sentence: str a sentence to replace words in.
    :param new_word: str replacement word
    :param old_word: str word to replace
    :return:  str input sentence with new words in place of old words
    """

    better_sentence = sentence.replace(new_word, old_word)
    return better_sentence
