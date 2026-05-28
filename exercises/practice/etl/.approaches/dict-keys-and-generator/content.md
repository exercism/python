# Iterate over Dictionary Keys and Process Values in a Generator

```python
def transform(input_dict):
    result = {}
    
    for key in input_dict:
        values = (item.lower() for item in input_dict[key])
        for value in values:
            result[value] = key
    return result
```