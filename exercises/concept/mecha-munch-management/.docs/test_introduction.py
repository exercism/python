"""pytest file built from introduction.md"""


def session_00001_line_17():
    r"""
    >>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}

    # Looking for the value associated with key "Rock Brown".
    # The key does not exist, so it is added with the default value, and the value is returned.
    >>> palette_I.setdefault('Rock Brown', '#694605')
    '#694605'

    # The (key, default value) pair has now been added to the dictionary.
    >>> palette_I
    {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd', 'Rock Brown': '#694605'}
    """


def session_00002_line_35():
    r"""
    >>> new_dict = dict.fromkeys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink'], 'fill in hex color here')

    {'Grassy Green': 'fill in hex color here',
     'Purple Mountains Majesty': 'fill in hex color here',
     'Misty Mountain Pink': 'fill in hex color here'}
    """


def session_00003_line_50():
    r"""
    >>> palette_I = {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd'}

    # Using .keys() returns a list of keys.
    >>> palette_I.keys()
    dict_keys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink'])

    # Using .values() returns a list of values.
    >>> palette_I.values()
    dict_values(['#9bc400', '#8076a3', '#f9c5bd'])

    # Using .items() returns a list of (key, value) tuples.
    >>> palette_I.items()
    dict_items([('Grassy Green', '#9bc400'), ('Purple Mountains Majesty', '#8076a3'), ('Misty Mountain Pink', '#f9c5bd')])

    # Views are dynamic.  Changing values in the dict changes all of the associated views.
    >>> palette_I['Purple Mountains Majesty'] = (128, 118, 163)
    >>> palette_I['Deep Red'] = '#932432'

    >>> palette_I.values()
    dict_values(['#9bc400', (128, 118, 163), '#f9c5bd', '#932432'])

    >>> palette_I.keys()
    dict_keys(['Grassy Green', 'Purple Mountains Majesty', 'Misty Mountain Pink', 'Deep Red'])

    >>> palette_I.items()
    dict_items([('Grassy Green', '#9bc400'), ('Purple Mountains Majesty', (128, 118, 163)), ('Misty Mountain Pink', '#f9c5bd'), ('Deep Red', '#932432')])
    """


def session_00004_line_88():
    r"""
    >>> palette_II = {'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}

    # Iterating in insertion order (First in, first out)
    >>> for item in palette_II.items():
    ...     print(item)
    ...
    ('Factory Stone Purple', '#7c677f')
    ('Green Treeline', '#478559')
    ('Purple baseline', '#161748')


    # Iterating in the reverse direction. (Last in, first out)
    >>> for item in reversed(palette_II.items()):
    ...    print (item)
    ...
    ('Purple baseline', '#161748')
    ('Green Treeline', '#478559')
    ('Factory Stone Purple', '#7c677f')
    """


def session_00005_line_116():
    r"""
    # Default ordering for a dictionary is insertion order (First in, first out).
    >>> color_palette = {'Grassy Green': '#9bc400',
    ...                  'Purple Mountains Majesty': '#8076a3',
    ...                  'Misty Mountain Pink': '#f9c5bd',
    ...                  'Factory Stone Purple': '#7c677f',
    ...                  'Green Treeline': '#478559',
    ...                  'Purple baseline': '#161748'}
 
    # The default sort order for a dictionary uses the keys.
    >>> sorted_palette = dict(sorted(color_palette.items()))
    >>> sorted_palette
    {'Factory Stone Purple': '#7c677f', 'Grassy Green': '#9bc400', 'Green Treeline': '#478559', 'Misty Mountain Pink': '#f9c5bd', 'Purple Mountains Majesty': '#8076a3', 'Purple baseline': '#161748'}
    """


def session_00006_line_140():
    r"""
    >>> palette_I = {'Grassy Green': '#9bc400',
    ...              'Purple Mountains Majesty': '#8076a3',
    ...              'Misty Mountain Pink': '#f9c5bd'}

    >>> palette_II = {'Factory Stone Purple': '#7c677f',
    ...               'Green Treeline': '#478559',
    ...               'Purple Baseline': '#161748'}

    >>> palette_I.update(palette_II)

    # Note that new items from palette_II are added.
    >>> palette_I
    {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd', 'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple Baseline': '#161748'}
    """


def session_00007_line_158():
    r"""
    >>> palette_I =   {'Grassy Green': '#9bc400', 'Purple Mountains Majesty': '#8076a3', 'Misty Mountain Pink': '#f9c5bd', 
                       'Factory Stone Purple': '#7c677f', 'Green Treeline': '#478559', 'Purple baseline': '#161748'}
    >>> palette_III = {'Grassy Green': (155, 196, 0), 'Purple Mountains Majesty': (128, 118, 163),
                       'Misty Mountain Pink': (249, 197, 189)}
    >>> palette_I.update(palette_III)

    # Overlapping values in palette_I are replaced with values from palette_III
    >>> palette_I
    {'Grassy Green': (155, 196, 0),
      'Purple Mountains Majesty': (128, 118, 163), 
      'Misty Mountain Pink': (249, 197, 189), 
      'Factory Stone Purple': '#7c677f', 
      'Green Treeline': '#478559', 'Purple baseline': '#161748'}
    """


def session_00008_line_180():
    r"""
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
    """


def session_00009_line_196():
    r"""
    >>> palette_III = {'Grassy Green': (155, 196, 0),
    ...                'Purple Mountains Majesty': (128, 118, 163),
    ...                'Misty Mountain Pink': (249, 197, 189)}

    >>> new_dict |= palette_III
    >>> new_dict
    ...
    {'Grassy Green': (155, 196, 0),
    'Purple Mountains Majesty': (128, 118, 163),
    'Misty Mountain Pink': (249, 197, 189),
    'Factory Stone Purple': '#7c677f',
    'Green Treeline': '#478559',
    'Purple baseline': '#161748'}
    """
