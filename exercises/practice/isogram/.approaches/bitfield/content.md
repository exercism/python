# Bitfield to keep track of used letters

```python
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

```
