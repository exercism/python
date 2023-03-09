# Tuple with str.join()

```python
def convert(num):
    drops = ('i', 3), ('a', 5), ('o', 7)
    sounds = ''.join(f'Pl{vowel}ng'
                      for vowel, factor in drops
                      if num % factor == 0)
    
    return  sounds or str(num)
```