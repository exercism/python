def is_pangram(sentence):
    return len(set(ltr for ltr in sentence.lower() if ltr.isalpha())) == 26
