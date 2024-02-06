# Dict and str.join()


```python
def convert(number):
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    results = ''.join(sounds[divisor] for 
                      divisor in sounds.keys()
                      if number % divisor == 0)

    return results or str(number)
```

This approach uses a [dictionary][dict] called 'sounds' with factors as `keys` and sound strings as `values`.
A [generator-expression][generator-expressions] inside of [`str.join()`][str.join] loops through the [dictionary view object][dict-view-object] [`sounds.keys()`][dict.keys()], which is a sequence of all the dictionary keys.
 Each `value` is looked up for every factor (key) where `number % divisor == 0`.
 `str.join()` then compiles the results.

This is the equivalent of:

```python
def convert(number):
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    results = []

    for divisor in sounds.keys():
        if number % divisor == 0:
            # Looks up the value by the divisor key and appends to the results list.
            results.append(sounds[divisor]) 
    
    return ''.join(results) or str(number)
```

The advantage of the generator expression is that no intermediary `list` is created in memory.
This will definitely save memory, and might also be slightly faster than a "classic" loop that appends to a `list`.

Finally, this could all be done as a 'one liner'.
But this becomes both harder to read and harder to maintain:

```python
def convert(number):
    return ''.join(sound for divisor, sound in 
                   {3: 'Pling', 5: 'Plang', 7: 'Plong'}.items()
                   if (number % divisor == 0)) or str(number)
```

[dict-view-object]: https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
[dict.keys()]: https://docs.python.org/3/library/stdtypes.html#dict.keys
[dict]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[generator-expressions]: https://www.pythonmorsels.com/how-write-generator-expression/
[str.join]: https://docs.python.org/3/library/stdtypes.html#str.join

