def is_isogram(string):
    characters_lower = [char.lower() for char in string if char.isalpha()]
    return len(set(characters_lower)) == len(characters_lower)
