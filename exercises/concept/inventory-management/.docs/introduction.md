# Introduction

A dictionary (`dict`) in Python is a data structure that associates [hashable][term-hashable] _keys_ to _values_ and is known in other programming languages as a resizable [hash table][hashtable-wikipedia], hashmap, or [associative array][associative-array].
Dictionaries are Python's only built-in [mapping type][mapping-types-dict].


`Keys` must be hashable and unique across the dictionary.
Key types can include `numbers`, `str`, or `tuples` (of _immutable_ values).
They cannot contain _mutable_ data structures such as `lists`, `dict`s, or `set`s.
As of Python 3.7, `dict` key order is guaranteed to be the order in which entries are inserted.

`values` can be of any data type or structure.
 Values can also nest _arbitrarily_, so they can include lists-of-lists, sub-dictionaries, and other custom or compound data structures.

Given a `key`, dictionaries can retrieve a `value` in (on average) constant time (_independent of the number of entries_).
Compared to searching for a value within a `list` or `array` (_without knowing the `index` position_), a `dict` uses significantly more memory, but has very rapid retrieval.
Dictionaries are especially useful in scenarios where the collection of items is large and must be accessed and updated frequently.


## Dictionary Construction

Dictionaries can be created in many ways.
The two most straightforward are using the `dict()`constructor or declaring a `dict` _literal_.

### The `dict()` Class Constructor

`dict()` (_the constructor for the dictionary class_) can be used with any iterable of `key`, `value` pairs or with a series of `<name>=<value>` _arguments_:

```python
#Passing a list of key,value tuples.
>>> wombat = dict([('name', 'Wombat'),('speed', 23),('land_animal', True)])
{'name': 'Wombat', 'speed': 23, 'land_animal': True}


#Using key=value arguments.
>>> bear = dict(name="Black Bear", speed=40, land_animal=True)
{'name': 'Black Bear', 'speed': 40, 'land_animal': True}
```

### Dictionary Literals

A `dict` can also be directly entered as a _dictionary literal_, using curly brackets (`{}`) enclosing `key : value` pairs:

```python
>>> whale = {"name": "Blue Whale", "speed": 35, "land_animal": False}
{'name': 'Blue Whale', 'speed': 35, 'land_animal': False}
```

## Accessing Values in a Dictionary

You can access an entry in a dictionary using a _key_ in square (`[]`) brackets.
If a `key` does not exist n the `dict`, a `KeyError` is thrown:

```python
>>> bear["speed"]
40

>>> bear["color"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'color'
```

Accessing an entry via the `.get(<key>, <default value>)` method can avoid the `KeyError`:

```python
>>> bear.get("color", 'not found')
'not found'
```

## Changing or Adding Dictionary Values

You can change an entry `value` by assigning to its _key_:

```python
#Assigning the value "Grizzly Bear" to the name key.
>>> bear["name"] = "Grizzly Bear"
{'name': 'Grizzly Bear', 'speed': 40, 'land_animal': True}

>>> whale["speed"] = 25
{'name': 'Blue Whale', 'speed': 25, 'land_animal': False}
```

New `key`:`value` pairs can be _added_ in the same fashion:

```python
# Adding an new "color" key with a new "tawney" value.
>>> bear["color"] = 'tawney'
{'name': 'Grizzly Bear', 'speed': 40, 'land_animal': True, 'color': 'tawney'}

>>> whale["blowholes"] = 1
{'name': 'Blue Whale', 'speed': 25, 'land_animal': False, 'blowholes': 1}
```

## Removing (Pop-ing) Dictionary Entries

You can use the `.pop(<key>)` method to delete a dictionary entry.
`.pop()` removes the (`key`, `value`) pair and returns the `value` for use.
Like `.get()`, `.pop(<key>)` accepts second argument (_`dict.pop(<key>, <default value>)`_) that will be returned if the `key` is not found.
This prevents a `KeyError` being raised:

```python
#Using .pop() removes both the key and value, returning the value.
>>> bear.pop("name")
'Grizzly Bear'


#The "name" key is now removed from the dictionary.
#Attempting .pop() a second time will throw a KeyError.
>>> bear.pop("name")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'


#Using a default argument with .pop() will prevent a KeyError from a missing key.
>>> bear.pop("name", "Unknown")
'Unknown'
```

## Looping through/Iterating over a Dictionary

Looping through a dictionary using `for item in dict` or `while item` will iterate over only the _keys _ by default.
You can access the _values_ within the same loop by using _square brackets_:

```python
>>> for key in bear:
>>>     print((key, bear[key])) #this forms a tuple of (key, value) and prints it.
('name', 'Black Bear')
('speed', 40)
('land_animal', True)
```

You can also use the `.items()` method, which returns (`key`, `value`) tuples automatically:

```python
#dict.items() forms (key, value tuples) that can be unpacked and iterated over.
>>> for key, value in whale.items():
>>>     print(key, ":", value)
name : Blue Whale
speed : 25
land_animal : False
blowholes : 1
```

Likewise, the `.keys()` method will return `keys` and the `.values()` method will return the `values`.

[associative-array]: https://en.wikipedia.org/wiki/Associative_array#:~:text=In%20computer%20science%2C%20an%20associative,a%20function%20with%20finite%20domain.
[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
