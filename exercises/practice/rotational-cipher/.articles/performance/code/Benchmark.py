import timeit
import sys
import itertools


print(sys.version)


AlPHABET = "abcdefghijklmnopqrstuvwxyz"
COMBINATIONS = itertools.combinations_with_replacement(f"{AlPHABET[:13]}{AlPHABET[:13].upper()} 12,", 2)
TEST_TEST = "".join([element for sublist in COMBINATIONS for element in sublist])

def rotate_ascii(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(letter) - 97 + key) % 26 + 97)
        else:
            result += letter
    return result


def rotate_alphabet(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += AlPHABET[(AlPHABET.index(letter.lower()) + key) % 26].upper()
            else:
                result += AlPHABET[(AlPHABET.index(letter) + key) % 26]
        else:
            result += letter
    return result


def rotate_translate(text, key):
    translator = AlPHABET[key:] + AlPHABET[:key]
    return text.translate(str.maketrans(AlPHABET + AlPHABET.upper(), translator + translator.upper()))


def rotate_recursion(text, key):
    if text == "":
        return ""
    first_letter, rest = text[0], text[1:]
    if first_letter.isalpha():
        if first_letter.isupper():
            return AlPHABET[(AlPHABET.index(first_letter.lower()) + key) % 26].upper() + rotate_recursion(rest, key)
        else:
            return AlPHABET[(AlPHABET.index(first_letter) + key) % 26] + rotate_recursion(rest, key)
    else:
        return first_letter + rotate_recursion(rest, key)



start_time = timeit.default_timer()
rotate_ascii(TEST_TEST, 25)
print("rotate ascii long :", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
rotate_alphabet(TEST_TEST, 25)
print("rotate alphabet long :", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
rotate_translate(TEST_TEST, 25)
print("rotate translate long :", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
rotate_recursion(TEST_TEST, 25)
print("rotate recursion long :", timeit.default_timer() - start_time)



start_time = timeit.default_timer()
rotate_ascii("abcABC -12", 11)
print("rotate ascii short :", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
rotate_alphabet("abcABC -12", 11)
print("rotate alphabet short :", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
rotate_translate("abcABC -12", 11)
print("rotate translate short :", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
rotate_recursion("abcABC -12", 11)
print("rotate recursion short :", timeit.default_timer() - start_time)
