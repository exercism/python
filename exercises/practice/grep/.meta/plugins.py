import re

RGX_ILLEGAL_CHARS = re.compile(r"\||-")
RGX_LINEBREAK = re.compile(r"\s*\n\s*")


def strip_illegal(s):
    return RGX_ILLEGAL_CHARS.sub("", s)


def clean_filetext(text):
    text = strip_illegal(text)
    text = RGX_ILLEGAL_CHARS.sub("", text)
    text = RGX_LINEBREAK.sub("\n", text)
    return text.strip()
