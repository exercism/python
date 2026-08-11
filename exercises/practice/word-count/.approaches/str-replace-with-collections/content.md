# String Replace with Collections


```python
from string import punctuation, whitespace
from collections import Counter

IGNORE = punctuation + whitespace

def count_words(phrase):
    words = (word.strip(IGNORE) for word in 
             phrase.replace(',', ' ')
             .replace('_', ' ')
             .lower()
             .split() if word)
             
    return Counter(words)
```

This approach uses a `generator expression` to lowercase, clean, strip, and split the input phrase into words.

Words is then consumed by the `Counter()` from the collections module, which counts up the words.

For convenience, `string.punctuation`  `string.whitespace` are imported to replace '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'.



Alternatively, `collections.defaultdict()` can be used, but requires that the words generator  be iterated through in an explicit  loop:

```python
from string import punctuation, whitespace
from collections import defaultdict

IGNORE = punctuation + whitespace

def count_words(phrase):
    words = (word.strip(IGNORE) for word in 
             phrase.replace(',', ' ')
             .replace('_', ' ')
             .lower()
             .split() if word)

    counts = defaultdict(int)

    for word in words:
      counts[word] +=1

    return counts
```

