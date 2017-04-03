from string import ascii_lowercase as alpha_lower
from string import ascii_uppercase as alpha_upper
ALPHA_LEN = len(alpha_lower)


def rotate(message, key):
    coded_message = ""
    for char in message:
        if char in alpha_lower:
            char = alpha_lower[(alpha_lower.index(char) + key) % ALPHA_LEN]
        elif char in alpha_upper:
            char = alpha_upper[(alpha_upper.index(char) + key) % ALPHA_LEN]
        coded_message += char
    return coded_message
