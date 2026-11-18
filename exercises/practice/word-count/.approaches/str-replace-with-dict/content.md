# String Replace with Dictionary


```python
IGNORE = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

def count_words(phrase):
    words = (phrase.replace(',', ' ')
                   .replace('_', ' ')
                   .lower()
                   .split()) #Returns a list, ready for further processing.

    counts = {}
    
    for word in words:
        word = word.strip(IGNORE)
        if word:
            # counts[word] = counts.setdefault(word, 0) + 1 can be used here instead.
            # https://stackoverflow.com/questions/7423428/python-dict-get-vs-setdefault
            counts[word] = counts.get(word, 0) + 1 

    return counts
```



This approach replaces unwanted characters and lowercases the phrase before splitting it into a word list.

It then loops through the word list and uses `str.strip()` to remove characters from the IGNORE string.

If there is a word left after the `str.strip()`operation, it is added to the _counts_ dictionary.