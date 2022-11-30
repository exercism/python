import timeit

loops = 1_000_000

val = timeit.timeit("""is_pangram("Victor jagt zwölf_(12) Boxkämpfer quer über den großen Sylter Deich.")""",
                    """
from string import ascii_lowercase
def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)

""", number=loops) / loops

print(f"all:   {val}")

val = timeit.timeit("""is_pangram("Victor jagt zwölf_(12) Boxkämpfer quer über den großen Sylter Deich.")""",
                    """
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(sentence):
    return ALPHABET.issubset(sentence.lower())

""", number=loops) / loops

print(f"set:   {val}")

val = timeit.timeit("""is_pangram("Victor jagt zwölf_(12) Boxkämpfer quer über den großen Sylter Deich.")""",
                    """
def is_pangram(sentence):
    return len([ltr for ltr in set(sentence.lower()) if ltr.isalpha()]) == 26

""", number=loops) / loops

print(f"len:   {val}")

val = timeit.timeit("""is_pangram("Victor jagt zwölf_(12) Boxkämpfer quer über den großen Sylter Deich.")""",
                    """
A_LCASE = 97;
A_UCASE = 65;
ALL_26_BITS_SET = 67108863;

def is_pangram(sentence):
    letter_flags = 0
    for letter in sentence:
        if letter >= 'a' and letter <= 'z':
            letter_flags |= 1 << (ord(letter) - A_LCASE)
        elif letter >= 'A' and letter <= 'Z':
            letter_flags |= 1 << (ord(letter) - A_UCASE)
    return letter_flags == ALL_26_BITS_SET

""", number=loops) / loops

print(f"bit:   {val}")
