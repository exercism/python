# String Replace with Comprehensions



```python
IGNORE = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

def count_words(phrase):
    cleaned = (phrase.replace(',', ' ')
                     .replace('_', ' ')
                     .lower().split()) #Returns a list
    
    words = [word.strip(IGNORE) for word in cleaned] #Reprocesses cleaned, dropping unwaned characters.

    return {word : words.count(word) for word in words}
  
  
 ###Alternatively, lines 4 and 9 can be combined###
  
  def count_words(phrase):
    cleaned = [word.strip(IGNORE) for word in 
               phrase.replace(',', ' ')
                     .replace('_', ' ')
                     .lower()
                     .split() if word]

    return {word : cleaned.count(word) for word in cleaned}
```



This approach replaces the `for` loop in the previous approach with a `list comprehension`.

The `dictionary comprehension` then processes the words list, calling word.count(word) for each word (key) in the words list.

Note that a `generator expression` cannot be used in this scenario due to the use of `count()` in the dictionary comprehension.