# Dictionary Comprehension

```python
def transform(input_dict):
        return {value.lower():key for key in 
                input_dict for 
                value in input_dict[key]}
```