def capitalize_title(title):
    return title.title()

def check_sentence_ending(sentence):
    return sentence.endswith(".")

def clean_up_spacing(sentence):
    clean_sentence = sentence.strip()
    return clean_sentence

def replace_word_choice(sentence, new_word, old_word):
    better_sentence = sentence.replace(new_word, old_word)
    return better_sentence
