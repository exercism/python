import regex

def reverse_korean(text):
    ''.join(regex.findall(u'\X', text)[::-1])
