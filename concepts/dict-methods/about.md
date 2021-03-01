# Dictionary Methods in Python

A dictionary (`dict`) in Python is a data structure that associates [hashable][term-hashable] _keys_ to _values_ and is known in other programming languages as a [hash table or hashmap][hashtable-wikipedia].
In Python, it's considered a [mapping type][mapping-types-dict].
`dicts` enable the retrieval of a value in constant time (on average), given the key.

Compared to searching for a value within a list or array (_without knowing the index position_), a dictionary uses significantly more memory, but has very rapid retrieval.
It's especially useful in scenarios where the collection of items is large and must be accessed/updated frequently.

## Dictionary Methods

The `dict` class in Python provides many useful [methods][dict-methods] for working with dictionaries.
Some were introduced in the concept for `dicts`.
Here are a few more - along with some techniques for iterating through and manipulating `dicts`.

To quickly populate a dictionary with various `keys` and default values, the _class method_ [`dict.fromkeys(iterable, <default value>)`][fromkeys] will iterate through the `keys` and create a new `dict`.  All `values` will be set to the `default` value provided.

```python
>>> new_dict = dict.fromkeys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink'], 'fill in hex color here')
>>> new_dict
{'Grassy Green': 'fill in hex color here',
 'Purple Mountains Majesty': 'fill in hex color here',
 'Misty Mountain Pink': 'fill in hex color here'}
```

`dict.clear()` will removed all `key:value` pairs from the dictionary, leaving it empty and ready for new entries.

```python
>>> pallette_II = {'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}
>>> pallette_II.clear()
>>> pallette_II
{}
```

`dict.get(key, <default return value>)` works similarly to `dict[key]` -- but it will return the `default` if the `key` is not in the dictionary.
If no `default` is given, the method will return `None`.

```python
>>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}
>>> palette_I['Factory Stone Purple']
Traceback (most recent call last):

  line 1, in <module>
    palette_I['Factory Stone Purple']

KeyError: 'Factory Stone Purple'

>>> palette_I.get('Factory Stone Purple', 'That color was not found.')
'That color was not found.'

>>> palette_I.get('Factory Stone Purple', False)
False

>>> palette_I.get('Factory Stone Purple')
None
```

`dict.popitem()`  removes & returns a single `key:value` pair from the `dict`.
Pairs are returned in Last-in-First-out (LIFO) order.
If the dictionary is empty, calling `.dict.popitem` will raise a `KeyError`.

```python
>>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}
>>> palette_I.popitem()
('Misty Mountain Pink', '#f9c5bd')
>>> palette_I.popitem()
('Purple Mountains Majesty', '#8076a3')
>>> palette_I.popitem()
('Grassy Green', '#9bc400')
>>> palette_I.popitem()

Traceback (most recent call last):

  line 1, in <module>
    palette_I.popitem()

KeyError: 'popitem(): dictionary is empty'
```

While `dict.clear()` and `dict.popitem()` are  _destructive_ actions, the  `.keys()`, `.values()`, and `.items()` methods return [_iterable views_][dict-views].
These views can be used for looping over `dict` content without altering it and are  _dynamic_ -- when underlying dictionary data changes, the associated view object will reflect the change.

```python
>>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}
>>> palette_I.keys()
dict_keys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink'])

>>> palette_I.values()
dict_values(['#9bc400', '#8076a3', '#f9c5bd'])

>>> palette_I.items()
dict_items([('Grassy Green', '#9bc400'), ('Purple Mountains Majesty', '#8076a3'), ('Misty Mountain Pink', '#f9c5bd')])

>>> palette_I['Purple Mountains Majesty'] = (128, 118, 163)
>>> palette_I.values()
dict_values(['#9bc400', (128, 118, 163), '#f9c5bd'])

>>> palette_I['Deep Red'] = '#932432'
>>> palette_I.keys()
dict_keys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink', 'Deep Red'])

>>> palette_I.items()
dict_items([('Grassy Green', '#9bc400'), ('Purple Mountains Majesty', (128, 118, 163)), ('Misty Mountain Pink', '#f9c5bd'), ('Deep Red', '#932432')])
```

`dict_one.update(<dict_two>)` can be used to _combine_ two dictionaries.
This method will take the `key:value` pairs of `dict_two` and write them into `dict_one`.

```python
>>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}
>>> palette_II = {'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}
>>> palette_I.update(palette_II)
>>> palette_I
...

{'Grassy Green': '#9bc400',
 'Purple Mountains Majesty': '#8076a3',
 'Misty Mountain Pink': '#f9c5bd',
 'Factory Stone Purple': '#7c677f',
 'Green Treeline': '#478559', 
 'Purple baseline': '#161748'}
```

Where keys in the two dictionaries _overlap_, the `value` in `dict_one` will be _overwritten_ by the corresponding `value` from `dict_two`.

```python
>>> palette_I =   {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd', 
                   'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}
>>> palette_III = {'Grassy Green': (155, 196, 0), 'Purple Mountains Majesty': (128, 118, 163),
                   'Misty Mountain Pink': (249, 197, 189)}
>>> palette_I.update(palette_III)
>>> palette_I
{'Grassy Green': (155, 196, 0),
  'Purple Mountains Majesty': (128, 118, 163), 
  'Misty Mountain Pink': (249, 197, 189), 
  'Factory Stone Purple': '#7c677f', 
  'Green Treeline': '#478559', 'Purple baseline': '#161748'}
```

Python 3.9 introduces a different means of merging `dicts`:  the `union` operators.
`dict | other_dict` will create a **new** `dict`, made up of the `key:value` pairs of `dict` and `other_dict`.
When both dictionaries share keys, the `other_dict` values will take precedence.
`dict |= other` will behave similar to `dict.update()`, but in this case, `other` can be either a `dict` or an iterable of `key:value` pairs.

```python
>>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}
>>> palette_II = {'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}
>>> new_dict = palette_I | palette_II
>>> new_dict
...
{'Grassy Green': '#9bc400',
 'Purple Mountains Majesty': '#8076a3',
 'Misty Mountain Pink': '#f9c5bd',
 'Factory Stone Purple': '#7c677f',
 'Green Treeline': '#478559',
 'Purple baseline': '#161748'}
 
 >>> palette_III = {'Grassy Green': (155, 196, 0), 'Purple Mountains Majesty': (128, 118, 163), 'Misty Mountain Pink': (249, 197, 189)}
 >>> new_dict |= palette_III
 >>> new_dict
 ...
 {'Grassy Green': (155, 196, 0),
 'Purple Mountains Majesty': (128, 118, 163),
 'Misty Mountain Pink': (249, 197, 189),
 'Factory Stone Purple': '#7c677f',
 'Green Treeline': '#478559',
 'Purple baseline': '#161748'}
```

## Tips and Tricks

As of Python 3.6, `dicts` preserve the order in which items are inserted, allowing ordered iteration using `.items()`.  As of Python 3.8, `dict` _views_ are reversible, allowing keys, values or items to be iterated over reverse of insertion order by using `reversed(dict.keys())`, `reversed(dict.values())`, or `reversed(dict.items())`.

```python
>>> palette_II = {'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}
>>> for item in palette_II.items():
...     print(item)
...
('Factory Stone Purple', '#7c677f')
('Green Treeline', '#478559')
('Purple baseline', '#161748')

>>> for item in reversed(palette_II.items()):
...    print (item)
...
('Purple baseline', '#161748')
('Green Treeline', '#478559')
('Factory Stone Purple', '#7c677f')

```

While `dict` does not have a built-in sorting method, it is possible to sort a dictionary _view_ by keys or values using the built-in `sorted()` with `dict.items()`.  The sorted view can then be used to create a new, sorted dictionary.  Unless a _sort key_ is specified, the default sort is over dictionary keys.

```python
>>> color_palette = {'Grassy Green': '#9bc400', 
                    'Purple Mountains Majesty': '#8076a3', 
                    'Misty Mountain Pink': '#f9c5bd', 
                    'Factory Stone Purple': '#7c677f', 
                    'Green Treeline': '#478559', 
                    'Purple baseline': '#161748'}
 
 
>>> sorted_palette = dict(sorted(color_palette.items()))
>>> sorted_palette
{'Factory Stone Purple': '#7c677f',
 'Grassy Green': '#9bc400',
 'Green Treeline': '#478559',
 'Misty Mountain Pink': '#f9c5bd',
 'Purple Mountains Majesty': '#8076a3',
 'Purple baseline': '#161748'}
 
>>> value_sorted_palette = dict(sorted(color_palette.items(), key=lambda color: color[1]))
>>> value_sorted_palette
{'Purple baseline': '#161748',
 'Green Treeline': '#478559',
 'Factory Stone Purple': '#7c677f',
 'Purple Mountains Majesty': '#8076a3',
 'Grassy Green': '#9bc400',
 'Misty Mountain Pink': '#f9c5bd'} 

```

Swapping keys and values reliably in a dictionary takes a little more work, but can be accomplished via a loop using `dict.items()`.  But if the values stored in the `dict` are not unique, extra checks are required.  Both methods assume that `dict` keys and values are _hashable_.

```python


color_reference = {'Purple Mountains Majesty': '#8076a3',
                   'Misty Mountain Pink': '#f9c5bd',
                   'Factory Stone Purple': '#7c677f',
                   'Green Treeline': '#478559',
                   'Purple baseline': '#161748',
                   'Pink highlight': '#f95d9b',
                   'Bluewater lowlight': '#39a0ca',
                   'Bright Red': '#DE354C',
                   'Deep Red': '#932432',
                   'Pure Purple': '#3C1874',
                   'Purple Tinged Grey': '#283747',
                   'Cloud': '#F3F3F3'}

>>> reversed_color_reference = {}
>>> for key, value in color_reference.items():
...     reversed_color_reference[value] = key

>>> reversed_color_reference
{'#8076a3': 'Purple Mountains Majesty',
 '#f9c5bd': 'Misty Mountain Pink',
 '#7c677f': 'Factory Stone Purple',
 '#478559': 'Green Treeline',
 '#161748': 'Purple baseline',
 '#f95d9b': 'Pink highlight',
 '#39a0ca': 'Bluewater lowlight',
 '#DE354C': 'Bright Red',
 '#932432': 'Deep Red',
 '#3C1874': 'Pure Purple',
 '#283747': 'Purple Tinged Grey',
 '#F3F3F3': 'Cloud'}
    

>>> extended_color_reference = {'#8076a3': 'Purple Mountains Majesty',(128, 118, 163): 'Purple Mountains Majesty',
                                (21, 28, 0, 36): 'Purple Mountains Majesty','#f9c5bd': 'Misty Mountain Pink',
                                (249, 197, 189): 'Misty Mountain Pink',(0, 21, 24, 2): 'Misty Mountain Pink',
                                '#7c677f': 'Factory Stone Purple',(124, 103, 127): 'Factory Stone Purple',
                                (2, 19, 0, 50): 'Factory Stone Purple','#478559': 'Green Treeline',
                                (71, 133, 89): 'Green Treeline',(47, 0, 33, 48): 'Green Treeline',
                                '#161748': 'Purple baseline',(22, 23, 72): 'Purple baseline',
                                (69, 68, 0, 72): 'Purple baseline','#f95d9b': 'Pink highlight',
                                (249, 93, 155): 'Pink highlight',(0, 63, 38, 2): 'Pink highlight',
                                '#39a0ca': 'Bluewater lowlight',(57, 160, 202): 'Bluewater lowlight',
                                (72, 21, 0, 21): 'Bluewater lowlight','#DE354C': 'Bright Red',
                                (222, 53, 76): 'Bright Red',(0, 76, 66, 13): 'Bright Red',
                                '#932432': 'Deep Red',(147, 36, 50): 'Deep Red',
                                (0, 76, 66, 42): 'Deep Red','#3C1874': 'Pure Purple',
                                (60, 24, 116): 'Pure Purple',(48, 79, 0, 55): 'Pure Purple',
                                '#283747': 'Purple Tinged Grey',(40, 55, 71): 'Purple Tinged Grey',
                                (44, 23, 0, 72): 'Purple Tinged Grey','#F3F3F3': 'Cloud',
                                (243, 243, 243): 'Cloud',(0, 0, 0, 5): 'Cloud'}

>>> consolidated_colors = {}
>>> for key, value in extended_color_reference.items():
...    if value in consolidated_colors:
...        consolidated_colors[value].append(key)
...    else:
...        consolidated_colors[value] = [key]

>>> consolidated_colors
{'Purple Mountains Majesty': ['#8076a3', (128, 118, 163), (21, 28, 0, 36)],
 'Misty Mountain Pink': ['#f9c5bd', (249, 197, 189), (0, 21, 24, 2)],
 'Factory Stone Purple': ['#7c677f', (124, 103, 127), (2, 19, 0, 50)],
 'Green Treeline': ['#478559', (71, 133, 89), (47, 0, 33, 48)],
 'Purple baseline': ['#161748', (22, 23, 72), (69, 68, 0, 72)],
 'Pink highlight': ['#f95d9b', (249, 93, 155), (0, 63, 38, 2)],
 'Bluewater lowlight': ['#39a0ca', (57, 160, 202), (72, 21, 0, 21)],
 'Bright Red': ['#DE354C', (222, 53, 76), (0, 76, 66, 13)],
 'Deep Red': ['#932432', (147, 36, 50), (0, 76, 66, 42)],
 'Pure Purple': ['#3C1874', (60, 24, 116), (48, 79, 0, 55)],
 'Purple Tinged Grey': ['#283747', (40, 55, 71), (44, 23, 0, 72)],
 'Cloud': ['#F3F3F3', (243, 243, 243), (0, 0, 0, 5)]}
        
```

For a detailed explanation of dictionaries and methods for working with them, the [official tutorial][dicts-docs] and the [official library reference][mapping-types-dict] are excellent starting places.
For more on sorting, see the [Sorting HOW TO][sorting-howto] in the python docs.
 [Real Python][how-to-dicts] and [Finxter][fi-dict-guide] also have very thorough articles on Python dictionaries.

## Extending Dictionaries: The collections module

The [`collections`][collections-docs] module adds more functionality to Python's standard collection-based datatypes (`dictionary`, `set`, `list`, `tuple`).
A popular `dict`-oriented member of this module is the [`Counter`][counter-dicts], which automatically counts items and returns them a `dict` with the items as keys and their counts as values.
There is also the [`OrderedDict`][ordered-dicts-docs], which has methods specialized for re-arranging the order of a dictionary.
Finally, there is the [`defaultdict`][default-dicts], a subclass of the built-in `dict` module that, based on a factory method, sets a default value if a key is not found when trying to retrieve or assign the value.

[term-hashable]: https://docs.python.org/3/glossary.html#term-hashable
[hashtable-wikipedia]: https://en.wikipedia.org/wiki/Hash_table
[mapping-types-dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[dicts-docs]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[how-to-dicts]: https://www.w3schools.com/python/python_dictionaries.asp
[fromkeys]: https://docs.python.org/3/library/stdtypes.html#dict.fromkeys
[collections-docs]: https://docs.python.org/3/library/collections.html
[counter-dicts]: https://docs.python.org/3/library/collections.html#collections.Counter
[ordered-dicts-docs]: https://docs.python.org/3/library/collections.html#collections.OrderedDict
[default-dicts]: https://docs.python.org/2/library/collections.html#collections.defaultdict
[dict-views]: https://docs.python.org/3/library/stdtypes.html#dict-views
[dict-methods]: https://docs.python.org/3/library/stdtypes.html#dict
[fi-dict-guide]: https://blog.finxter.com/python-dictionary
[sorting-howto]: https://docs.python.org/3/howto/sorting.html
