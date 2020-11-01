A _dictionary_ is Python's primary mapping type that connects _hashable keys_ with values. The looking up of keys is more efficient than searching through an array, but does require more memory.

## Dict construction

Dictionaries can be created in various ways. You can either use the `dict()` class constructor or the literal declaration of a _dict_.

### Use the `dict()` constructor

```python
>>> bear = dict(name="Black Bear", amount=5, land_animal=True)
{'name': 'Panda', 'amount': 15, 'land_animal': True}
```

### Declare a _dict_ literal

```python
>>> whale = {"name":"Blue Whale", "amount":2, "land_animal":False}
{'name': 'Dolphin', 'amount': 2, 'land_animal': False}
```

With literal declaration keep in mind that _keys_ are replaced with _data types_ and the `=` is replaced with a `:`.

## Accessing values

You can access items in a dictionary in two ways, using the _key_ of the value.

### Using _square brackets_ after the dict object

```python
>>> request_brackets = bear["amount"]
5
```

### Using `.get()`

```python
>>> request_get = whale.get("name")
Blue Whale
```

## Changing values

You can easily change a value of an item using it's _key_.

```python
>>> bear["name"] = "Grizzly Bear"
{'name': 'Grizzly Bear', 'amount': 5, 'land_animal': True}

>>> whale["amount"] = 7
{'name': 'Blue Whale', 'amount': 7, 'land_animal': False}
```

## Looping through a dictionary

Looping through a dictionary using a `for` loop only returns the _keys_ of the items.

```python
>>> for key in bear:
>>>     print(key)
name
amount
land_animal
```

But you can also make a `for` loop return the _values_ of a dictionary with a simple trick.

```python
>>> for key in whale:
>>>    print(whale[key])
Blue Whale
7
False
```
