def find_anagrams(word, candidates):
    return [candidate
            for candidate in candidates
            if _letters(candidate) == _letters(word)
            if candidate.lower() != word.lower()]

def _letters(word):
	# lower is convert string to lowercase and sorted converted the string to 
	# list with elements arranged in sorted order
    return sorted(word.lower())
