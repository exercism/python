import timeit

loops = 1_000_000

val = timeit.timeit("""is_isogram("Emily Jung-Schwartzkopf")""",
                    """
def is_isogram(phrase):
    scrubbed = [ltr.lower() for ltr in phrase if ltr.isalpha()]
    return len(set(scrubbed)) == len(scrubbed)

""", number=loops) / loops

print(f"scrubbed comprehension: {val}")

val = timeit.timeit("""is_isogram("Emily Jung-Schwartzkopf")""",
                    """
def is_isogram(phrase):
    scrubbed = phrase.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))

""", number=loops) / loops

print(f"scrubbed replace:       {val}")

val = timeit.timeit("""is_isogram("Emily Jung-Schwartzkopf")""",
                    """
import re

def is_isogram(phrase):
    scrubbed = re.compile('[^a-zA-Z]').sub('', phrase).lower()
    return len(set(scrubbed)) == len(scrubbed)

""", number=loops) / loops

print(f"scrubbed regex:         {val}")

val = timeit.timeit("""is_isogram("Emily Jung-Schwartzkopf")""",
                    """
import re

def is_isogram(phrase):
    scrubbed = "".join(re.findall("[a-zA-Z]", phrase)).lower()
    return len(set(scrubbed)) == len(scrubbed)

""", number=loops) / loops

print(f"findall regex:          {val}")

val = timeit.timeit("""is_isogram("Emily Jung-Schwartzkopf")""",
                    """
A_LCASE = 97
Z_LCASE = 122
A_UCASE = 65
Z_UCASE = 90


def is_isogram(phrase):
    letter_flags = 0

    for ltr in phrase:
        letter = ord(ltr)
        if letter >= A_LCASE and letter <= Z_LCASE:
            if letter_flags & (1 << (letter - A_LCASE)) != 0:
                return False
            else:
                letter_flags |= 1 << (letter - A_LCASE)
        elif letter >= A_UCASE and letter <= Z_UCASE:
            if letter_flags & (1 << (letter - A_UCASE)) != 0:
                return False
            else:
                letter_flags |= 1 << (letter - A_UCASE)
    return True

""", number=loops) / loops

print(f"bitfield:               {val}")
