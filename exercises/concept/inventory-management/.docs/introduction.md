# Introduction

A dictionary (`dict`) is a data structure that associates [hashable][term-hashable] _keys_ to _values_.
It is known in other programming languages as a resizable [hash table][hashtable-wikipedia], hashmap, or [associative array][associative-array].
Dictionaries are Python's only built-in [mapping type][mapping-types-dict].


`Keys` can include `numbers`, `str`, `tuples` (of _immutable_ values), or `frozensets`, but must be hashable and unique across the dictionary.
  `values` can be of any or multiple data type(s) or structures, including other dictionaries, built-in types, custom types, or even objects like functions.
As of Python 3.7, key order is guaranteed to be the order in which entries are inserted.


`dict`s enable the retrieval of a `value` in (on average) constant O(1) time, given the `key`.
Compared to searching for a value within a `list` or `array` (_without knowing the `index` position_), a dictionary uses significantly more memory, but has very rapid retrieval.
Dictionaries are especially useful in scenarios where the collection of items is large and must be accessed/updated frequently.


## Dictionary Construction

Dictionaries can be created in many ways.
The two most straightforward are using the `dict()`constructor or declaring a `dict` _literal_.


### The `dict()` Class Constructor

`dict()` can be used with any iterable of key, value pairs or with a series of `<name>=<value>` _arguments_:

```python
#Here we pass a list of key,value tuples.
>>> wombat = dict([('name', 'Wombat'),('speed', 23),('land_animal', True)])
{'name': 'Wombat', 'speed': 23, 'land_animal': True}


#Here we use key=value arguments.
>>> bear = dict(name="Black Bear", speed=40, land_animal=True)
{'name': 'Black Bear', 'speed': 40, 'land_animal': True}


```

### Dictionary Literals

A dictionary can also be directly entered as a _dictionary literal_:

```python
>>> whale = {"name": "Blue Whale", "speed": 35, "land_animal": False}
{'name': 'Blue Whale', 'speed': 35, 'land_animal': False}
```

## Accessing Values in a `dict`

You can access an item in a dictionary using a _key_ in square brackets.
If a key does not exist, a `KeyError` is thrown:

```python
>>> bear["speed"]
40

>>> bear["color"]
Traceback (most recent call last):

  File "/var/folders/../../T/sample.py", line 1, in <cell line: 1>
    bear["color"]

KeyError: 'color'
```

Accessing a item via the `get(<key>, <default value>)` method can avoid the `KeyError`:

```python
>>> bear.get("color", 'not found')
'not found'
```


## Changing or Adding Dictionary Values

You can easily change a `value` by assigning a new one to its _key_:

```python
>>> bear["name"] = "Grizzly Bear"
{'name': 'Grizzly Bear', 'speed': 40, 'land_animal': True}

>>> whale["speed"] = 25
{'name': 'Blue Whale', 'speed': 25, 'land_animal': False}
```

Values can be added in the same fashion:

```python
>>> bear["color"] = 'tawney'
{'name': 'Grizzly Bear', 'speed': 40, 'land_animal': True, 'color': 'tawney'}

>>> whale["blowholes"] = 1 
{'name': 'Blue Whale', 'speed': 25, 'land_animal': False, 'blowholes': 1}
```


## Removing/Pop-ing Dictionary Entries

You can use `dict.pop(<key>)` to delete a dictionary entry.
`pop()` removes the (`key`, `value`) pair and returns the `value` for use.
 Like `get()`, `dict.pop(<key>)` accepts second argument (_`dict.pop(<key>, <default value>)`_) that will be returned if the `key` is not found.
 This prevents a `KeyError` being raised:

```python
#Using pop removes both the key and value, returning the value.
>>> bear.pop("name")
'Grizzly Bear'


#The name key is now gone, so a KeyError is thrown.
>>> bear.pop("name")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'


#The name key is gone, but using a default argument with pop() will prevent a KeyError.
>>> bear.pop("name", "Unknown")
'Unknown'
```


## Looping through/Iterating over a Dictionary

Looping through a dictionary using `for item in dict` will iterate over the _keys_, but you can access the _values_ by using _square brackets_:

```python
>>> for key in bear:
>>>     (key, bear[key]) #this forms a tuple of (key, value)
('name', 'Black Bear')
('speed', 40)
('land_animal', True)
```

[associative-array]: https://en.wikipedia.org/wiki/Associative_array#:~:text=In%20computer%20science%2C%20an%20associative,a%20function%20with%20finite%20domain.
[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
