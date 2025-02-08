# Dictionary Constructor with Generator Expression

```python
def transform(legacy_data):
    new_data = dict((letter.lower(), score)
                    for score, tiles in 
                    legacy_data.items() 
                    for letter in tiles)
    return new_data
```