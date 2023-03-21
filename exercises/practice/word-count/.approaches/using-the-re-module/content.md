# Using the Re Module



```python
import re
from collections import Counter
from string import punctuation


def count_words(phrase):
  conditions = re.compile(r"[^_\s,:]+")
  return Counter((match.group().strip(punctuation) for match in 
                  re.finditer(conditions, phrase.lower())))
```




```python
import re
from collections import Counter


def count_words(phrase):
  conditions = re.compile(r"[a-z0-9]+(?:'[a-z]+)?")
  return Counter(conditions.findall(phrase.lower()))
```





```python
import re
from collections import Counter


def count_words(sentence):
  conditions = re.compile(r"[\s_,\"]+")
  words =     (re.sub(r'\A\W+', '', re.sub(r'\W+\Z', '', word)) 
               for word in conditions.split(sentence.lower()) if word)
    
  return Counter(words)
```



There are many variations that can be used in a regular expressions.

This approach shows several different regexs, in combination with several different `re` methods.

The first variation uses `re.findite()` to return a lazy iterator that is then fed to `collections.Counter`.

The second variation uses `re.findall()`to return a list that is fed to `collections.Counter`

The final variation uses `re.sub()` and `re.split()`to return a generator that is fed to `collections.Counter`.