from string import ascii_lowercase, ascii_uppercase


ALPHA_LEN = len(ascii_lowercase)


def rotate(message, key):
    coded_message = ''
    for char in message:
        if char in ascii_lowercase:
            char = ascii_lowercase[(ascii_lowercase.index(char) + key) % ALPHA_LEN]
        elif char in ascii_uppercase:
            char = ascii_uppercase[(ascii_uppercase.index(char) + key) % ALPHA_LEN]
        coded_message += char
    return coded_message
