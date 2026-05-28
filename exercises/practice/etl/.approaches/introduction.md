# Introduction

There are multiple  Pythonic ways to solve the ETL exercise.
Among them are:

- Iterate over `dict.keys()` & lowercase all values in a `generator-expression` before inserting into the new dict.
- Iterate over  `dict.keys()` & use `dict` methods `dict.get()` and `dict.setdefault()` to retrieve values and insert keys into new dict.
- Iterate over`dict.items()`  and deal with lowercasing the values `list` in a nested loop.
- Use the  `dict()` constructor  with a `generator expression` to unpack and lowercase values in a nested loop.
- Use a dictionary comprehension



## General guidance

The goal of the ETL exercise is to:

*   **E**xtract the data from the 'legacy' dictionary given as input. It has numeric **keys** with a `list`of uppercased strings as **values**.
*   **T**ransform the data, by turning the `list` of **values** into individual lowercased **keys**, with the former **keys** used as **values**.
*   **L**oad the data into a new dictionary and return it.


The challenge here is to deal efficiently with lowercasing the **values**, which are `lists` containing strings.
Unfortunately, there is no way to avoid an extra loop for lowercasing the string values, so all current approaches to this exercise have equivalent performance.

But there may be other considerations such as readability, or  how to deal with duplicate data in **values** (_and whether that is necessary or not_) when selecting an approach.

Additionally, while the test data for this exercise does not contain any [unhashable][unhashable] values, if this code were to be used in a situation where the legacy values were of an unknown datatype, measures would need to be taken to test the values before attempting to create keys with them.


## Approach: Iterate over `dict.keys()` & Lowercase values in a generator or list comprehension.

```python
def transform(input_dict):
    result = {}
    
    for key in input_dict:
        values = (item.lower() for item in input_dict[key])
        for value in values:
            result[value] = key
    return result
  
  ##OR##
  
  def transform(input_dict):
    result = {}
    
    for key in input_dict:
        values = [item.lower() for item in input_dict[key]]
        for value in values:
            result[value] = key
    return result
```


This approach iterates over `dict.keys()` ,  converting all the strings in the returned values `list` to lowercase via `generator expression` or `list comprehension`.
Once the values are converted to lowercase, they are iterated through in an inner loop.
Each value is then inserted into the new dictionary as a key, with the 'old' key (_from the outer loop_) used as the value.
For more details, see the [dictionary keys and generator][dict-keys-and-generator ] approach.


## Approach: Use Dictionary Methods `dict.get()` and `dict.setdefault()`

```python
def transform(input_data):
    transformed = {}
    
    for key in input_data:
        for value in input_data.get(key):
            transformed.setdefault(value.lower(), key)
    return transformed
```


As with the approach described above, this iterates through the keys of `input_data`.
Each value `list` is looked up via `input_data.get(key)`, and the new dictionary (_transformed_) is updated via `dict.setdefault(value.lower(), key)`.
For details, read the [dictionary keys and dictionary methods][dict-keys-and-dict-methods] approach.


## Approach: Iterate over `dict.items()`

```python
def transform(input_dict):
    new_data = {}
    
    for key, value in input_dict.items():
        for item in value:
            new_data[item.lower()] = key
    return new_data
```


This approach iterates over both keys and values via `dict.items()`.
The inner loop then iterates over the values `list`, transforming each string and inserting it into the `new_data` dictionary using _bracket notation_, with the lowercased string as key and the former key as the new value.
For more details, see the [dictionary items][dict-items] approach.


## Approach: Use a generator with the Dictionary Constructor

```python
def transform(legacy_data):
    new_data = dict((letter.lower(), score)
                    for score, tiles in 
                    legacy_data.items() 
                    for letter in tiles)
    return new_data
```


This approach encapsulates the loops described in prior approaches within a `generator expression`.
The generator includes a nested loop to iterate over the strings within the value `list`, lowercasing them.
The generator is then passed to the `dict()` constructor, which unpacks it and creates a new dictionary.
For more information, see the [dictionary constructor with generator][dict-constructor-and-generator]  approach.


## Approach: Use a Dictionary Comprehension

```python
def transform(input_dict):
        return {value.lower():key for key in 
                input_dict for 
                value in input_dict[key]}
```



This approach is very similar to the one above, but uses a `dictionary comprehension` format instead of a generator fed to a constructor.
For more details, see the [dictionary comprehension][dictionary-comprehension] approach.



## Other approaches

Besides these five idiomatic approaches, there are a multitude of possible variations using different string or dictionary methods or strategies for extracting and lowercasing the input dictionary values.

The strategy below employs `zip_longest` with `dict.items()` to re-package keys and values.

```python
from itertools import zip_longest

def transform(input_dict):
    
    lowercased = (zip_longest([element.lower() for element in item], 
                              key, fillvalue=key) for 
                  key, item in input_dict.items())

    return dict(lowercased)
```


But note that it still has the nested loop all of these solutions share -- as the values returned by `dict.items()` still needs to be unpacked and lowercased before anything can be added to the new dictionary.



## Which approach to use?

All of these approaches are roughly equivalent given that the values in the input dictionary are a list of strings that must be lowercased.
This demands that those values be looped through, making all strategies loop-within-loop.
Using generators or comprehensions might still give a slight performance boost, but they may also be harder to read or understand for others.


[dict-constructor-and-generator]:  https://exercism.org/tracks/python/exercises/etl/approaches/dict-constructor-and-generator
[dict-items]:  https://exercism.org/tracks/python/exercises/etl/approaches/dict-items
[dict-keys-and-dict-methods]:  https://exercism.org/tracks/python/exercises/etl/approaches/dict-keys-and-dict-methods
[dict-keys-and-generator ]:  https://exercism.org/tracks/python/exercises/etl/approaches/dict-keys-and-generator
[dictionary-comprehension]:  https://exercism.org/tracks/python/exercises/etl/approaches/dictionary-comprehension
[unhashable]: https://docs.python.org/3/glossary.html#term-hashable
