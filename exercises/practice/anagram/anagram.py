def find_anagrams(word, candidates):
    resultado = []
    
    for anagrams in candidates:
        if word.lower() != anagrams.lower() and sorted(anagrams.lower()) == sorted(word.lower()):
            resultado.append(anagrams)
    return resultado