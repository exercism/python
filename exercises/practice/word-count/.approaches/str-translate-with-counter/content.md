# String Translate with Counter



```python
from collections import Counter

def count_words(phrase):
    cleaner = phrase.maketrans({key: ' ' for key in ".,:-_!@$%^&"})
    cleaned = phrase.translate(cleaner).lower().split()
    results = Counter((stripped for word in cleaned if 
              (stripped := word.strip("\"'"))))
    
    return results
```



This approach (somewhat unusually) uses `str.translate()` to filter out unwanted characters.

`collections.Counter` is then used to count the words.

The generator expression uses an assignment operator (_othewise know as the "walrus" operator `:=`_) to ensure that empty strings are excluded from the count.