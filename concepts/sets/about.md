# Sets

A [`set`][type-set] is a mutable and _unordered_ collection of _hashable_ objects.
Items within a `set` are distinct and duplicate members are not allowed.
Like most collections, `sets` can hold any (or multiple) data type(s) -- as long as those types can be [hashed][hashable].
Sets also come in an _immutable_ [`frozenset`][type-frozenset] flavor.

Like other collection types, `sets` support membership testing through `in`, length calculation through `len()`, shallow copies through `copy()`, and iteration via `for item in <set>`.
_Unlike_ sequence types (_`string`, `list` & `tuple`_), `sets` are **neither ordered nor indexed**, and _do not support_ slicing, sorting, or other sequence-type behaviors.

`sets` are most commonly used to quickly dedupe groups of items.
They're also used for fast membership testing, finding supersets & subsets of items, and performing "set math" (_calculating union, intersection, difference & symmetric difference between groups of items._).

Checking membership in a `set` has only O(1) time complexity versus checking for membership in a `list` or `string`, which has worst-case O(n) time complexity.
Operations such as `<set>.union()`, `<set>.intersection()`, or `<set>.difference()` have an average O(n) time complexity.

## Construction

A `set` can be declared as a _set literal_ with curly `{}` brackets and commas between elements.
Duplicates are silently omitted:

```python
>>> one_element = {'😀'}
>>> one_element
{'😀'}

>>> multiple_elements = {'Hello!', '¡Hola!', 'Привет!', 'こんにちは！'}
>>> multiple_elements
{'こんにちは！', '¡Hola!', 'Hello!', 'Привет!'}

>>> multiple_duplicates =  {'Hello!', '¡Hola!', 'Привет!', 'こんにちは！', '¡Hola!', 'Привет!'}
>>> multiple_duplicates
{'こんにちは！', '¡Hola!', 'Hello!', 'Привет!'}
```

Set literals use the same curly braces as `dict` literals, so the `set()` constructor must be used to declare an empty `set`.

The `set()` constructor can also be used with any _iterable_ passed as an argument.
Elements are cycled through by the constructor and added to the `set` individually.
Order is not preserved and duplicates are silently omitted:

```python
>>> no_elements = set()
>>> no_elements
set()

# The tuple is unpacked and each distinct element is added.  Duplicates are removed.
>>> multiple_elements_from_tuple = set(("Parrot", "Bird", 334782, "Bird", "Parrot"))
>>> multiple_elements_from_tuple
{334782, 'Bird', 'Parrot'}

# The list is unpacked and each distinct element is added.
>>> multiple_elements_from_list = set([2, 3, 2, 3, 3, 3, 5, 7, 11, 7, 11, 13, 13])
>>> multiple_elements_from_set
{2, 3, 5, 7, 11, 13}
```

Results when using a set constructor with a string or dictionary may be surprising:

```python
# String elements (Unicode code points) are iterated through and added *individually*.
>>> multiple_elements_string = set("Timbuktu")
>>> multiple_elements_string
{'T', 'b', 'i', 'k', 'm', 't', 'u'}

# Unicode separators and positioning code points are also added *individually*.
>>> multiple_code_points_string = set('अभ्यास')
>>> multiple_code_points_string
{'अ', 'भ', 'य', 'स', 'ा', '्'}

# The iteration default for dictionaries is over the keys.
>>> source_data = {"fish": "gold", "monkey": "brown", "duck" : "white", "crow": "black"}
>>> set(source_data)
{'crow', 'duck', 'fish', 'monkey'}
```

Sets can hold heterogeneous datatypes, but all `set` elements must be _hashable_:

```python

>>> lists_as_elements = {['😅','🤣'], ['😂','🙂','🙃'], ['😜', '🤪', '😝']}

Traceback (most recent call last):

  File "<ipython-input-24-1bb7c3d22c52>", line 1, in <module>
    lists_as_elements = {['😅','🤣'], ['😂','🙂','🙃'], ['😜', '🤪', '😝']}

TypeError: unhashable type: 'list'

# standard sets are mutable, so they cannot be hashed.
>>> sets_as_elements = {{'😅','🤣'}, {'😂','🙂','🙃'}, {'😜', '🤪', '😝'}}
Traceback (most recent call last):

  File "<ipython-input-25-92f22c7541b1>", line 1, in <module>
    sets_as_elements = {{'😅','🤣'}, {'😂','🙂','🙃'}, {'😜', '🤪', '😝'}}

TypeError: unhashable type: 'set'
```

Therefore, to create a `set` of `sets`, the contained sets must be of type `frozenset()`

```python
# frozensets don't have a literal form
>>> set_1 = frozenset({'😜', '😝', '🤪'})
>>> set_2 = frozenset({'😅', '🤣'})
>>> set_3 = frozenset({'😂', '🙂', '🙃'})

>>> frozen_sets_as_elements = {set_1, set_2, set_3}
>>> frozen_sets_as_elements
{frozenset({'😜', '😝', '🤪'}), frozenset({'😅', '🤣'}), frozenset({'😂', '🙂', '🙃'})}
```

## Working with Sets

Elements can be added/removed using `<set>.add(<item>)` / `<set>.remove(<item>)`.
`remove(<item>)` will raise a `KeyError` if the item is not present in the `set`.

```python
>>> creatures = {'crow', 'duck', 'fish', 'monkey', 'elephant'}
>>> creatures.add('beaver')
>>> creatures.remove('duck')
>>> creatures
{'beaver', 'crow', 'elephant', 'fish', 'monkey'}

# Trying to remove an item that is not present will raise a KeyError
>>> creatures.remove('bear')
Traceback (most recent call last):

  File "<ipython-input-51-00c49fd3fe67>", line 1, in <module>
    creatures.remove('bear')

KeyError: 'bear'
```

`<set>.discard(<item>)` will also remove an item from the `set`, but will **not** raise a `KeyError` if the item is not present.
`<set>.clear()` will remove all items.
`<set>.pop()` will remove and _return_ an **arbitrary** item and raises a `KeyError` if the `set` is empty.

## Set Methods

Sets implement methods that generally mimic [mathematical set operations][mathematical-sets].
Most (_though not all_) of these methods can be performed using either operator(s) or method call(s).
Using operators requires that both inputs be `sets` or `frozensets`, while methods will generally take any iterable as an argument.

### Fast Membership Testing Between Groups

The `<set>.isdisjoint(<other_collection>)` method is used to test if a `set` has **no elements in common** with another set or iterable.
It will accept any `iterable` or `set` as an arugment, returning `True` if they are **disjoint**, `False` otherwise.
Note that for `dcts`, the iteration default is over`<dict>.keys()`.

```python
>>>  mammals = {'squirrel','dog','cat','cow', 'tiger', 'elephant'}
>>>  birds   = {'crow','sparrow','eagle','chicken', 'albatross'}

# Dictionary of animal names with colors
>>> animals = {'chicken': 'white','sparrow': 'grey','eagle': 'brown and white',
                'albatross': 'grey and white','crow': 'black','elephant': 'grey',
                'dog': 'rust','cow': 'black and white','tiger': 'orange and black',
                'cat': 'grey','squirrel': 'black'}

# List of additonal animals
>>> additional_animals = ['pangolin', 'panda', 'parrot', 'lemur', 'tiger', 'pangolin']
...

>>> mammals.isdisjoint(birds)
True

>>> mammals.isdisjoint(animals)
False

>>> birds.isdisjoint(additional_animals)
True

>>> set(additional_animals).isdisjoint(animals)
False
```

`<set>.issubset(<other_collection>)` | `<set> <= <other_set>` are used to check if every element in `<set>` is also in `<other>`.
`<set>.issuperset(<other_collection>)` | `<set> >= <other_set>` are used to check the inverse -- if every element in `<other>` is also in `<set>`.

```python
>>> animals = {'chicken': 'white','sparrow': 'grey','eagle': 'brown and white',
                'albatross': 'grey and white','crow': 'black','elephant': 'grey',
                'dog': 'rust','cow': 'black and white','tiger': 'organge and black',
                'cat': 'grey','squirrel': 'black'}

>>>  mammals = {'squirrel','dog','cat','cow', 'tiger', 'elephant'}
>>>  birds   = {'crow','sparrow','eagle','chicken', 'albatross'}

# Methods will take any iterable as an argument
>>> mammals.issubset(animal_colors)
True


# A set is always a loose subset of itself
>>> animals <= animals
True

>>> birds <= animals
True

>>> birds <= mammals
False
```

`<set> < <other_set>` and `<set> > <other_set>` are used to test for _proper subsets_:
(`<set>` <= `<other_set>`) AND (`<set>` != `<other_set>`) for the `<` operator; (`<set>` >= `<other_set>`) AND (`<set>` != `<other_set>`) for the `>` operator.
They have no method equivelent.

```python
>>> animal_names =      {'albatross','cat','chicken','cow','crow','dog',
                         'eagle','elephant','sparrow','squirrel','tiger'}

>>> animal_names_also = {'albatross','cat','chicken','cow','crow','dog',
                         'eagle','elephant','sparrow','squirrel','tiger'}

>>>  mammals = {'squirrel','dog','cat','cow', 'tiger', 'elephant'}
>>>  birds   = {'crow','sparrow','eagle','chicken', 'albatross'}

>>> mammals < animal_names
True

>>> animal_names > birds
True

# A set is never a *proper subset* of itself
>>> animal_names_also < animal_names
False


>>> animals < animals

```

### Set Operations

`<set>.union(*<other iterables>)` and `<set> | <other set 1> | <other set 2> | ... | <other set n>` return a new `set` with elements from `<set>` and all `<others>`.

```python
>>> perennial_vegetables = {'Asparagus', 'Broccoli', 'Sweet Potatoe', 'Kale'}
>>> annual_vegetables = {'Corn', 'Zucchini', 'Sweet Peas', 'Summer Squash'}

>>> more_perennials = ['Radicchio', 'Rhubarb', 'Spinach', 'Watercress']

# Methods will take any iterable as an argument.
>>> perennial_vegetables.union(more_perennials)
{'Asparagus','Broccoli','Kale','Radicchio','Rhubarb','Spinach','Sweet Potatoe','Watercress'}

# Operators require sets.
>>> perennial_vegetables | annual_vegetables
{'Asparagus','Broccoli','Corn','Kale','Summer Squash','Sweet Peas','Sweet Potatoe','Zucchini'}

```

`<set>.difference(*<other iterables>)` and `<set> - <other set 1> - <other set 2> - ...<other set n>` return a new `set` with elements from the original `<set>` that are not in `<others>`.

```python
>>> berries_and_veggies = {'Asparagus', 'Broccoli', 'Watercress', 'Goji Berries', 'Goose Berries', 'Ramps',
                           'Walking Onions', 'Raspberries','Blueberries', 'Blackberries', 'Strawberries',
                           'Rhubarb', 'Kale', 'Artichokes', 'Currants', 'Honeyberries'}

# Methods will take any iterable as an argument.
>>> veggies = ('Asparagus', 'Broccoli', 'Watercress', 'Ramps',
               'Walking Onions', 'Rhubarb', 'Kale', 'Artichokes')

>>> just_berries = berries_and_veggies.difference(veggies)
>>> just_berries
{'Blackberries','Blueberries','Currants','Goji Berries',
 'Goose Berries','Honeyberries','Raspberries','Strawberries'}

>>> berries_and_veggies - just_berries
{'Artichokes','Asparagus','Broccoli','Kale','Ramps','Rhubarb','Walking Onions','Watercress'}
```

`<set>.intersection(*<other iterables>)` and `<set> & <other set> & <other set 2> & ... <other set n>` return a new `set` with elements common to the original `set` and all `<others>`.

```python
>>> perennials = {'Annatto','Asafetida','Asparagus','Azalea','Winter Savory', 'Blackberries','Broccoli','Curry Leaf',
                  'Fennel','French Sorrel','Fuchsia','Kaffir Lime','Kale','Lavender','Mint','Oranges',
                  'Oregano','Ramps','Roses','Tarragon','Watercress','Wild Bergamot'}

>>> annuals = {'Corn', 'Zucchini', 'Sweet Peas', 'Marjoram', 'Summer Squash', 'Okra',
               'Shallots', 'Basil', 'Cilantro', 'Cumin', 'Sunflower', 'Chervil', 'Summer Savory'}

>>> herbs = ['Annatto','Asafetida','Basil','Chervil','Cilantro','Curry Leaf','Fennel','Kaffir Lime',
             'Lavender','Marjoram','Mint','Oregano','Summer Savory' 'Tarragon','Wild Bergamot',
             'Wild Celery','Winter Savory']


# Methods will take any iterable as an argument.
>>> perennial_herbs = perennials.intersection(herbs)
>>> perennial_herbs
{'Mint', 'Annatto', 'Winter Savory', 'Curry Leaf', 'Lavender', 'Fennel',
 'Oregano', 'Kaffir Lime','Asafetida', 'Wild Bergamot', 'Tarragon'}

>>> annuals & set(herbs)
 {'Basil', 'Chervil', 'Marjoram', 'Cilantro'}
```

`<set>.symmetric_difference(<other iterable>)` and `<set> ^ <other set>` return a new `set` that contains elements that are in `<set>` OR `<other>`, but **not in both**.

```python
>>> plants_1 = {'🌲','🍈','🌵', '🥑','🌴', '🥭'}
>>> plants_2 = ('🌸','🌴', '🌺', '🌲', '🌻', '🌵')


# Methods will take any iterable as an argument.
>>> fruit_and_flowers = plants_1.symmetric_difference(plants_2)
>>> fruit_and_flowers
{'🌸', '🌺', '🍈', '🥑', '🥭','🌻' }

>>> fruit_and_flowers ^ plants_1
{'🌲',  '🌸', '🌴', '🌵','🌺', '🌻'}

>>> fruit_and_flowers ^ plants_2
{ '🥑', '🌴','🌲', '🌵', '🍈', '🥭'}
```

[type-set]: https://docs.python.org/3/library/stdtypes.html#set
[type-frozenset]: https://docs.python.org/3/library/stdtypes.html#frozenset
[mathematical-sets]: https://en.wikipedia.org/wiki/Set_theory#Basic_concepts_and_notation
[hashable]: https://docs.python.org/3.7/glossary.html#term-hashable
