def is_isogram(string):
    characters_lower = [c.lower() for c in string if c.isalpha()]
    return len(set(characters_lower)) == len(characters_lower)
