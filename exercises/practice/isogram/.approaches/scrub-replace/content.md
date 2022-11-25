# Scrub with `replace()`

```python
def is_isogram(phrase):
    scrubbed = phrase.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))

```
