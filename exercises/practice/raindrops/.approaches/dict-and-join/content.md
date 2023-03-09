# `dict` and `str.join()`

```python
def convert(number):
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    results = ''.join(sounds[divisor] for 
                      divisor, sound in sounds.items()
                      if number % divisor == 0)

    return results or str(number)
```

A [dictionary][dict] called **sounds** is created with factors as `keys` and sound strings as `values`.
A [generator-expression][generator-expressions] inside of `str.join()` loops through [`sounds.items()`][dict.items()], which is a series of (key, value) `tuples`.
 Each `value` is looked up for every factor where number % divisor == 0.
 `str.join()` then concatenates the results.

This is the equivalent of:

```python
results = []

for divisor, sound in sounds.items():
  if number % divisor == 0:
    results.append(sounds[divisor]) # Looks up the value by the divisor key and appends to the results list.
    
result = ''.join(results) # Iterates over the results list and concatenates the strings.
```

 The advantage of the generator expression is that no intermediary `list` is created in memory.
This will definitely save memory, and might also be slightly faster than a "classic" loop that appends to a `list`.



[dict.items()]: https://docs.python.org/3/library/stdtypes.html#dict.items
[dict]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[generator-expressions]: https://www.pythonmorsels.com/how-write-generator-expression/
[str.join]: https://docs.python.org/3/library/stdtypes.html#str.join