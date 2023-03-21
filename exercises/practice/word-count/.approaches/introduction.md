# Introduction

There are many Pythonic ways to solve the Word Count exercise.
Among them are:

- String iteration with `dict.get()`
- `str.replace()` for cleaning with:
  -  `collections.Counter` or  `collections.defaultdict()`
  -  `dict.get()`or  `dict.setdefault()`
  - `list-comprehension` with `dictionary-comprehension`
- Regex (`re`) for cleaning  (using`finditer`, `findall`, or `split`):
- `str.translate()` with `collections.Counter` and `walrus operator`
- `filter()` and `collections.Counter`

Various parts of these strategies can also be combined or re-combined.


## General guidance


The goal of the Word Count exercise is to count the number of words used in a given phrase.

Before an accurate count can be done, the phrase needs to be cleaned of non-word characters (punctuation, whitespace, tabs, etc.) and lowercased.

This can be thought of in three parts:

1.  Remove unwanted characters from the phrase,
2.  Lowercase and split the phrase into a list of words,
3.  Count up the word groups in the word list.

Because strings are immutable in Python, any cleaning action will return a new string.


Most idiomatic solutions use either a chain of  `str.replace()`, or a regex via the `re` module to clean the phrase.
`str.srtip()` is also very useful for dropping unwanted characters.

For efficiency, it is best to either lowercase the phrase prior to cleaning, or just before splitting.
Otherwise you risk adding overhead as you call `str.lower()` on individual words.

To split, `str.split()` or `findall()`| `finditer()`| `split()` from the `re` module are usually the best strategies.
However, it is entirely possible to complete this exercise without splitting the phrase into a word list.

Counting words most often employs the `Counter()` from `collections`, although `collections.defaultdict()`, `dict.get()` , `dict.setdefault()`, or a `dictionary comprehension` work just as well.


The temptation here is to go straight to regex, but `str.replace()` and `str.strip()` are surprisingly performant, and also easier to read for those unfamiliar with regex.



## Approach: String Iteration with `dict.get()` or `dict.setdefault()`



```python
def count_words(sentence):
    sentence = sentence.lower() + '\n' #lowercase the sentence and add a carriage return to it.
    word_list = {}
    new_word = ''
    
    for pos, value in enumerate(sentence): #enumerate() hands back both index and value
        if value.isalpha() or value.isdigit():
            new_word += value
        elif new_word and value == "'" and sentence[pos + 1].isalpha():
            new_word += value
        else:
            if new_word:
                word_list[new_word] = word_list.get(new_word, 0) + 1
            new_word = ''
    
    return word_list
```


This approach avoids splitting the phrase into a word list by iterating over each _character_ in the sentence to determine if  it belongs in a valid word (_only letters and numbers are allowed_).

As each valid word is built up, it is added to the dictionary.

Using `word_list.get()` allows for setting newly added words to value 1 while incrementing values for words already added to the dictionary.

Once added to the dictionary, the variable `new_word` is reset to empty, ready for the next word.



## Approach: `str.replace()` and `dict.get()` or  `dict.setdefault()`



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





## Approach: `str.replace()` and `comprehensions`



```python
IGNORE = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

def count_words(phrase):
    cleaned = (phrase.replace(',', ' ')
                     .replace('_', ' ')
                     .lower()
                     .split()) #Returns a list
    
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





## Approach: `str.replace()` and `collections`



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



This a



## Approach:  Using the `re` module



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



## Approach:  `str.translate()`with `collections.Counter()`



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



## Approach `filter()` with `collections.Counter()`



```pyth
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





This approach uses the built-in `filter()` to clean the phrase and `collections.Counter` to count the words.

Filter is fed the same general generator expression that uses `str.replace()`, `str.lower()`, and `str.split()` seen in other approaches.



For more information, see the [Filter with ]





## Which approach to use?



The most performant of these approaches is __ for longer text, and __ for smaller text.  Memory-wise, ___ has the lease overhead.

Overall, using `str.replace()` with a `Counter` or `dict` might be the most readable to those unfamiliar with regex, and iterating through the string might be more readable to those not familiar with Python.



To compare the performance and other tradeoffs of the approaches, take a look at the [Performance article][article-performance].





[approach-string-iteration-with-dict]:  https://exercism.org/tracks/python/exercises/word-count/approaches/string-iteration-with-dict
[approach-str-replace-with-dict]:  https://exercism.org/tracks/python/exercises/word-count/approaches/str-replace-with-dict
[approach-str-replace-with-comprehensions]:  https://exercism.org/tracks/python/exercises/word-count/approaches/str-replace-with-comprehensions
[approach-str-replace-with-collections]:  https://exercism.org/tracks/python/exercises/word-count/approaches/str-replace-with-collections
[approach-using-the-re-module]:  https://exercism.org/tracks/python/exercises/word-count/approaches/using-the-re-module
[approach-str-translate-with-counter]:  https://exercism.org/tracks/python/exercises/word-count/approaches/str-translate-with-counter
[approach-filter-with-counter]:  https://exercism.org/tracks/python/exercises/word-count/approaches/filter-with-counter
[article-performance]:https://exercism.org/tracks/python/exercises/word-count/articles/performance