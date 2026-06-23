# Iterate Over Dictionary Keys and Use Dictionary Methods


```python
def transform(input_data):
    transformed = {}
    
    for key in input_data:
        for value in input_data.get(key):
            transformed.setdefault(value.lower(), key)
    return transformed
```