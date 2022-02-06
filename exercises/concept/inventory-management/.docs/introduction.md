# Introduction

A _**dictionary**_ is Python's primary mapping type that associates a _hashable key_ with a value. The lookup by key is more efficient than searching through an array, but does require more memory.

## Dict construction

Dictionaries can be created in various ways. Two simple options are the use the `dict()` class constructor or the dict literal declaration with key-value pairs.

### Use the `dict()` constructor

```python
>>> bear = dict(name="Black Bear", speed=40, land_animal=True)
{'name': 'Black Bear', 'speed': 40, 'land_animal': True}
```

### Declare a _dict_ literal

```python
>>> whale = {"name": "Blue Whale", "speed": 35, "land_animal": False}
{'name': 'Blue Whale', 'speed': 35, 'land_animal': False}
```

With the dict literal declaration keep in mind that _keys_ are of _data types_ `str` and the colon `:` is used instead of an equal sign `=`.

## Accessing values

You can access an item in a dictionary using the _key_ of the value.

### Using _square brackets_ after the dict object

```python
>>> bear["speed"]
40
```

### Using `.get()`

```python
>>> whale.get("name")
'Blue Whale'
```

## Changing values

You can easily change a value of an item using its _key_.

```python
>>> bear["name"] = "Grizzly Bear"
{'name': 'Grizzly Bear', 'speed': 40, 'land_animal': True}

>>> whale["speed"] = 25
{'name': 'Blue Whale', 'speed': 25, 'land_animal': False}
```

## Deleting values using keys

You can delete an item from a dictionary using `dict.pop(<key>)`. This will remove the (`key`, `value`) pair from the dictionary and return the `value` for use. `dict.pop(<key>)` accepts second argument, `default` that is returned if the `key` is not found  (`dict.pop(<key>, <default>)`). Otherwise, a `KeyError` will be raised for any `key` that is missing.

```python
>>> bear.pop("name")
'Grizzly Bear'
>>> bear.pop("name", "Unknown")
'Unknown'
>>> bear.pop("name")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'
```

## Looping through a dictionary

Looping through a dictionary using `for item in dict` will iterate over the _keys_, but you can access the _values_ by using _square brackets_.

```python
>>> for key in bear:
>>>     (key, bear[key])
('name', 'Black Bear')
('speed', 40)
('land_animal', True)
```
