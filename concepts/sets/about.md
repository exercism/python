# Sets

A [`set`][type-set] is a _mutable_ and _unordered_ collection of [_hashable_][hashable] objects.
Set members must be distinct -- duplicate items are not allowed.
They can hold multiple different data types and even nested structures like a `tuple` of `tuples` -- as long as all elements can be _hashed_.
Sets also come in an immutable [`frozensets`][type-frozenset] flavor.

Sets are most commonly used to quickly remove duplicates from other data structures or item groupings.
They are also used for efficient comparisons when sequencing and duplicate tracking are not needed.

Like other collection types (_dictionaries, lists, tuples_), `sets` support:
- Iteration via `for item in <set>`
- Membership checking via `in` and `not in`,
- Length calculation through `len()`, and
- Shallow copies through `copy()`

`sets` do not support:
- Indexing of any kind
- Ordering via sorting or insertion
- Slicing
- Concatenation via `+`


Checking membership in a `set` has constant time complexity (on average) versus checking membership in a `list` or `string`, where the time complexity grows as the length of the data increases.
Methods such as `<set>.union()`, `<set>.intersection()`, or `<set>.difference()` also have constant time complexity (on average).


## Set Construction

While sets can be created in many different ways, the most straightforward construction methods are declaring a _set literal_, using the `set` class constructor (`set()`), and using a _set comprehension_.

### Set Literals

A `set` can be directly entered as a _set literal_ with curly `{}` brackets and commas between elements.
Duplicates are silently omitted:

```python
>>> one_element = {'😀'}
{'😀'}

>>> multiple_elements = {'😀', '😃', '😄', '😁'}
{'😀', '😃', '😄', '😁'}

>>> multiple_duplicates =  {'Hello!', 'Hello!', 'Hello!', 
                            '¡Hola!','Привіт!', 'こんにちは！', 
                            '¡Hola!','Привіт!', 'こんにちは！'}
{'こんにちは！', '¡Hola!', 'Hello!', 'Привіт!'}
```

Set literals use the same curly braces as `dict` literals, which means you need to use `set()` to create an empty `set`.

### The Set Constructor

`set()` (_the constructor for the `set` class_) can be used with any `iterable` passed as an argument.
Elements of the `iterable` are cycled through and added to the `set` individually.
Element order is not preserved and duplicates are silently omitted:


```python
# To create an empty set, the constructor must be used.
>>> no_elements = set()
set()

# The tuple is unpacked & each element is added.  
# Duplicates are removed.
>>> elements_from_tuple = set(("Parrot", "Bird", 
                               334782, "Bird", "Parrot"))
{334782, 'Bird', 'Parrot'}

# The list is unpacked & each element is added.
# Duplicates are removed.
>>> elements_from_list = set([2, 3, 2, 3, 3, 3, 5, 
                              7, 11, 7, 11, 13, 13])
{2, 3, 5, 7, 11, 13}
```

### Set Comprehensions

Like `lists` and `dicts`, sets can be created via _comprehension_:

```python
# First, a list with duplicates
>>> numbers = [1,2,3,4,5,6,6,5,4,8,9,9,9,2,3,12,18]

# This set comprehension squares the numbers divisible by 3
# Duplicates are removed.
>>> calculated = {item**2 for item in numbers if item % 3 == 0}
{9, 36, 81, 144, 324}
```

### Gotchas when Creating Sets

Due to its "unpacking" behavior, using the `set` constructor with a string might be surprising:

```python
# String elements (Unicode code points) are 
# iterated through and added *individually*.
>>> elements_string = set("Timbuktu")
{'T', 'b', 'i', 'k', 'm', 't', 'u'}

# Unicode separators and positioning code points 
# are also added *individually*.
>>> multiple_code_points_string = set('अभ्यास')
{'अ', 'भ', 'य', 'स', 'ा', '्'}
```

Remember: sets can hold different datatypes and _nested_ datatypes, but all `set` elements must be _hashable_:

```python
# Attempting to use a list for a set member throws a TypeError
>>> lists_as_elements = {['😅','🤣'], 
                        ['😂','🙂','🙃'], 
                        ['😜', '🤪', '😝']}

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'


# Standard sets are mutable, so they cannot be hashed.
>>> sets_as_elements = {{'😅','🤣'}, 
                        {'😂','🙂','🙃'}, 
                        {'😜', '🤪', '😝'}}

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
```

However, a  `set` of `sets` can be created via type `frozenset()`:

```python
# Frozensets don't have a literal form.
>>> set_1 = frozenset({'😜', '😝', '🤪'})
>>> set_2 = frozenset({'😅', '🤣'})
>>> set_3 = frozenset({'😂', '🙂', '🙃'})

>>> frozen_sets_as_elements = {set_1, set_2, set_3}
>>> frozen_sets_as_elements
{frozenset({'😜', '😝', '🤪'}), frozenset({'😅', '🤣'}), 
frozenset({'😂', '🙂', '🙃'})}
```


## Adding and Removing Set Members

Elements can be added or removed from a `set` using the methods `<set>.add(<item>)` and `<set>.remove(<item>)`.
The `.remove(<item>)` method will raise a `KeyError` if the item is not present in the `set`:

```python
>>> creatures = {'crow', 'duck', 'fish', 'monkey', 'elephant'}
>>> creatures.add('beaver')
>>> creatures.remove('duck')
>>> creatures
{'beaver', 'crow', 'elephant', 'fish', 'monkey'}

# Trying to remove an item that is not present raises a KeyError
>>> creatures.remove('bear')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  KeyError: 'bear'
```

### Additional Strategies for Removing Set Members

- `<set>.discard(<item>)` will remove an item from the `set`, but will **not** raise a `KeyError` if the item is not present.
- `<set>.clear()` will remove all items from the set.
- `<set>.pop()` will remove and _return_ an **arbitrary** item, and raises a `KeyError` if the `set` is empty.


## Set Operations

Sets have methods that generally mimic [mathematical set operations][mathematical-sets].
Most (_not all_) of these methods have an [operator][operator] equivalent.
Methods generally take any `iterable` as an argument, while operators require that both sides of the operation are `sets` or `frozensets`.


### Membership Testing Between Sets

The `<set>.isdisjoint(<other_collection>)` method is used to test if a `sets` elements have any overlap with the elements of another.
The method will accept any `iterable` or `set` as an argument.
It will return `True` if the two sets have **no elements in common**, `False` if elements are **shared**.

```python
# Both mammals and additional_animals are lists.
>>> mammals = ['squirrel','dog','cat','cow', 'tiger', 'elephant']
>>> additional_animals = ['pangolin', 'panda', 'parrot', 
                          'lemur', 'tiger', 'pangolin']

# Animals is a dict.
>>> animals = {'chicken': 'white',
               'sparrow': 'grey',
               'eagle': 'brown and white',
               'albatross': 'grey and white',
               'crow': 'black',
               'elephant': 'grey', 
               'dog': 'rust',
               'cow': 'black and white',
               'tiger': 'orange and black',
               'cat': 'grey',
               'squirrel': 'black'}
               
# Birds is a set.
>>> birds = {'crow','sparrow','eagle','chicken', 'albatross'}

# Mammals and birds don't share any elements.
>>> birds.isdisjoint(mammals)
True

# There are also no shared elements between 
# additional_animals and birds.
>>> birds.isdisjoint(additional_animals)
True

# Animals and mammals have shared elements.
# **Note** The first object needs to be a set or converted to a set
# since .isdisjoint() is a set method.
>>> set(animals).isdisjoint(mammals)
False
```

### Checking for Subsets and Supersets

`<set>.issubset(<other_collection>)` is used to check if every element in `<set>` is also in `<other_collection>`.
The operator form is `<set> <= <other_set>`:

```python
# Set methods will take any iterable as an argument.
# All members of birds are also members of animals.
>>> birds.issubset(animals)
True

# All members of mammals also appear in animals.
# **Note** The first object needs to be a set or converted to a set
# since .issubset() is a set method.
>>> set(mammals).issubset(animals)
True

# Both objects need to be sets to use a set operator
>>> birds <= set(mammals)
False

# A set is always a loose subset of itself.
>>> set(additional_animals) <= set(additional_animals)
True
```

`<set>.issuperset(<other_collection>)` is the inverse of `.issubset()`.
It is used to check if every element in `<other_collection>` is also in `<set>`.
The operator form is `<set> >= <other_set>`:


```python
# All members of mammals also appear in animals.
# **Note** The first object needs to be a set or converted to a set
# since .issuperset() is a set method.
>>> set(animals).issuperset(mammals)
True

# All members of animals do not show up as members of birds.
>>> birds.issuperset(animals)
False

# Both objects need to be sets to use a set operator
>>> birds >= set(mammals)
False

# A set is always a loose superset of itself.
>>> set(animals) >= set(animals)
True
```

### 'Proper' Subsets and Supersets

`<set> < <other_set>` and `<set> > <other_set>` are used to test for _proper subsets_.
A `set` is a proper subset if (`<set>` <= `<other_set>`) **AND** (`<set>` != `<other_set>`) for the `<` operator.

A `set is a proper superset if `(`<set>` >= `<other_set>`) **AND** (`<set>` != `<other_set>`) for the `>` operator.
These operators have no method equivalent:

```python
>>> animal_names = {'albatross','cat','chicken','cow','crow','dog',
                   'eagle','elephant','sparrow','squirrel','tiger'}

>>> animals_also = {'albatross','cat','chicken','cow','crow','dog',
                   'eagle','elephant','sparrow','squirrel','tiger'}

>>> mammals = {'squirrel','dog','cat','cow', 'tiger', 'elephant'}
>>> birds   = {'crow','sparrow','eagle','chicken', 'albatross'}

>>> mammals < animal_names
True

>>> animal_names > birds
True

# A set is not a *proper subset* if set == other set.
>>> animals_also < animal_names
False

# A set is never a *proper subset* of itself
>>> animals_also < animals_also
False
```

### Set Unions

`<set>.union(*<other iterables>)` returns a new `set` with elements from `<set>` and all `<other iterables>`.
The operator form of this method is `<set> | <other set 1> | <other set 2> | ... | <other set n>`.

```python
>>> perennials = {'Asparagus', 'Broccoli', 'Sweet Potato', 'Kale'}
>>> annuals = {'Corn', 'Zucchini', 'Sweet Peas', 'Summer Squash'}
>>> more_perennials = ['Radicchio', 'Rhubarb', 
                      'Spinach', 'Watercress']

# Methods will take any iterable as an argument.
>>> perennials.union(more_perennials)
{'Asparagus','Broccoli','Kale','Radicchio','Rhubarb',
'Spinach','Sweet Potato','Watercress'}

# Operators require sets.
>>> set(more_perennials) | perennials
{'Asparagus',
 'Broccoli',
 'Kale',
 'Radicchio',
 'Rhubarb',
 'Spinach',
 'Sweet Potato',
 'Watercress'}
```

### Set Differences

`<set>.difference(*<other iterables>)` returns a new `set` with elements from the original `<set>` that are not in `<others>`.
The operator version of this method is `<set> - <other set 1> - <other set 2> - ...<other set n>`.

```python
>>> berries_and_veggies = {'Asparagus', 
                          'Broccoli', 
                          'Watercress', 
                          'Goji Berries', 
                          'Goose Berries', 
                          'Ramps', 
                          'Walking Onions', 
                          'Blackberries', 
                          'Strawberries', 
                          'Rhubarb', 
                          'Kale', 
                          'Artichokes', 
                          'Currants'}

>>> veggies = ('Asparagus', 'Broccoli', 'Watercress', 'Ramps',
               'Walking Onions', 'Rhubarb', 'Kale', 'Artichokes')

# Methods will take any iterable as an argument.
>>> berries = berries_and_veggies.difference(veggies)
{'Blackberries','Currants','Goji Berries',
 'Goose Berries', 'Strawberries'}

# Operators require sets.
>>> berries_and_veggies - just_berries
{'Artichokes','Asparagus','Broccoli','Kale',
'Ramps','Rhubarb','Walking Onions','Watercress'}
```

### Set Intersections

`<set>.intersection(*<other iterables>)` returns a new `set` with elements common to the original `set` and all `<others>` (in other words, the `set` where everything [intersects][intersection]).
The operator version of this method is  `<set> & <other set> & <other set 2> & ... <other set n>`

```python
>>> perennials = {'Annatto','Asafetida','Asparagus','Azalea',
                 'Winter Savory', 'Broccoli','Curry Leaf','Fennel', 
                 'Kaffir Lime','Kale','Lavender','Mint','Oranges',
                 'Oregano', 'Tarragon', 'Wild Bergamot'}

>>> annuals = {'Corn', 'Zucchini', 'Sweet Peas', 'Marjoram', 
              'Summer Squash', 'Okra','Shallots', 'Basil', 
              'Cilantro', 'Cumin', 'Sunflower', 'Chervil', 
              'Summer Savory'}

>>> herbs = ['Annatto','Asafetida','Basil','Chervil','Cilantro',
            'Curry Leaf','Fennel','Kaffir Lime','Lavender',
            'Marjoram','Mint','Oregano','Summer Savory' 
            'Tarragon','Wild Bergamot','Wild Celery',
            'Winter Savory']


# Methods will take any iterable as an argument.
>>> perennial_herbs = perennials.intersection(herbs)
{'Annatto', 'Asafetida', 'Curry Leaf', 'Fennel', 'Kaffir Lime',
 'Lavender', 'Mint', 'Oregano', 'Wild Bergamot','Winter Savory'}

# Operators require both groups be sets.
>>> annuals & set(herbs)
 {'Basil', 'Chervil', 'Marjoram', 'Cilantro'}
```

### Set Symmetric Differences

`<set>.symmetric_difference(<other iterable>)` returns a new `set` that contains elements that are in `<set>` OR `<other>`, but **not in both**.
The operator version of this method is  `<set> ^ <other set>`.

```python
>>> plants_1 = {'🌲','🍈','🌵', '🥑','🌴', '🥭'}
>>> plants_2 = ('🌸','🌴', '🌺', '🌲', '🌻', '🌵')


# Methods will take any iterable as an argument.
>>> fruit_and_flowers = plants_1.symmetric_difference(plants_2)
>>> fruit_and_flowers
{'🌸', '🌺', '🍈', '🥑', '🥭','🌻' }


# Operators require both groups be sets.
>>> fruit_and_flowers ^ plants_1
{'🌲',  '🌸', '🌴', '🌵','🌺', '🌻'}

>>> fruit_and_flowers ^ plants_2
{ '🥑', '🌴','🌲', '🌵', '🍈', '🥭'}
```

~~~~exercism/note

A symmetric difference of more than two sets will result in a `set` that includes both the elements unique to each `set` AND elements shared between more than two sets in the series (_details in the Wikipedia article on [symmetric difference][symmetric_difference]_).  

To obtain only items unique to each `set` in the series, intersections between all 2-set combinations need to be aggregated in a separate step, and removed:  


```python
>>> one = {'black pepper','breadcrumbs','celeriac','chickpea flour',
           'flour','lemon','parsley','salt','soy sauce',
           'sunflower oil','water'}

>>> two = {'black pepper','cornstarch','garlic','ginger',
           'lemon juice','lemon zest','salt','soy sauce','sugar',
           'tofu','vegetable oil','vegetable stock','water'}

>>> three = {'black pepper','garlic','lemon juice','mixed herbs',
             'nutritional yeast', 'olive oil','salt','silken tofu',
             'smoked tofu','soy sauce','spaghetti','turmeric'}

>>> four = {'barley malt','bell pepper','cashews','flour',
            'fresh basil','garlic','garlic powder', 'honey',
            'mushrooms','nutritional yeast','olive oil','oregano',
            'red onion', 'red pepper flakes','rosemary','salt',
            'sugar','tomatoes','water','yeast'}

>>> intersections = (one & two | one & three | one & four | 
                     two & three | two & four | three & four)
...
{'black pepper','flour','garlic','lemon juice','nutritional yeast', 
'olive oil','salt','soy sauce', 'sugar','water'}

# The ^ operation will include some of the items in intersections, 
# which means it is not a "clean" symmetric difference - there
# are overlapping members.
>>> (one ^ two ^ three ^ four) & intersections
{'black pepper', 'garlic', 'soy sauce', 'water'}

# Overlapping members need to be removed in a separate step
# when there are more than two sets that need symmetric difference.
>>> (one ^ two ^ three ^ four) - intersections
...
{'barley malt','bell pepper','breadcrumbs', 'cashews','celeriac',
  'chickpea flour','cornstarch','fresh basil', 'garlic powder',
  'ginger','honey','lemon','lemon zest','mixed herbs','mushrooms',
  'oregano','parsley','red onion','red pepper flakes','rosemary',
  'silken tofu','smoked tofu','spaghetti','sunflower oil', 'tofu', 
  'tomatoes','turmeric','vegetable oil','vegetable stock','yeast'}
```

[symmetric_difference]: https://en.wikipedia.org/wiki/Symmetric_difference
~~~~

[hashable]: https://docs.python.org/3.7/glossary.html#term-hashable
[mathematical-sets]: https://en.wikipedia.org/wiki/Set_theory#Basic_concepts_and_notation
[operator]: https://www.computerhope.com/jargon/o/operator.htm
[type-frozenset]: https://docs.python.org/3/library/stdtypes.html#frozenset
[type-set]: https://docs.python.org/3/library/stdtypes.html#set
[intersection]: https://www.mathgoodies.com/lessons/sets/intersection
