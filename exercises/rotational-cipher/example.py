def rotational_cipher(message, key):
    import string
    alpha_lower = list(string.ascii_lowercase)
    alpha_upper = list(string.ascii_uppercase)
    coded_message = ""
    for char in list(message):
        if char in alpha_lower:
            char = alpha_lower[(alpha_lower.index(char) + key) % 26]
        elif char in alpha_upper:
            char = alpha_upper[(alpha_upper.index(char) + key) % 26]
        coded_message = coded_message + char
    return coded_message
