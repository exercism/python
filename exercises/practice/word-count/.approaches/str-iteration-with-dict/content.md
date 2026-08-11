# String Iteration with Dictionary



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

