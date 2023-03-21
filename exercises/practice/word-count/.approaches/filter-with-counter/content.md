# Filter with Counter


```python
from collections import Counter
import string

def count_words(sentence):
    words = filter(None, (word.strip(string.punctuation) 
                          for word in sentence
                          .lower()
                          .replace("_"," ")
                          .replace(",", " ")
                          .split())
                  ) 
    return Counter(words)
```


