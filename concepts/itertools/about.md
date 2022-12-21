## Infinite iterators

```exercism/note
To avoid infinite loops, you can use `break` to end a loop.
```

### Count()

`count(start, <step>)` allows to print all values from the start value to infinity.
Count also has an optional step parameter, which allows to print values with a step size other than 1.

```python
>>> import itertools
>>> for number in itertools.count(5, 2):
...     if number > 20:
...         break
...     else:
...         print(number, end=' ')
...
5 7 9 11 13 15 17 19
```

Giving `count()` a negative step size will print values in a descending order.

```python
>>> import itertools
>>> for number in itertools.count(5, -2):
...     if number < -20:
...         break
...     else:
...         print(number, end=' ')
...
5 3 1 -1 -3 -5 -7 -9 -11 -13 -15 -17 -19
```

### Cycle()

`cycle(iterable)` allows to print all values from the iterable in an infinte loop.
For example a `list`, `tuple`, `string` or `dict` can be used as an iterable.

```python
>>> import itertools
>>> number = 0
>>> for letter in itertools.cycle("ABC"):
...     if number == 10:
...         break
...     else:
...         print(letter, end=' ')
...         number += 1
...
A B C A B C A B C A
```

### Repeat()

`repeat(object, <times>)` allows to print the same value in an infinte loop.
Although if the optional times parameter is given, the value will be printed that many times.
Meaning that it is not an infinite loop if that parameter is given.

```python
>>> import itertools
>>> for number in itertools.repeat(5, 3):
...     print(number, end=' ')
...
5 5 5
```

## Iterators terminating on the shortest input sequence

### Accumulate()

`accumulate(iterable, <function>)` allows to print the accumulated values.

perhaps skip

### Chain()

`chain(iterable1, iterable2...)` creates an irretator of values from the iterables in the order they are given.

```python
>>> import itertools
>>> for number in itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9]):
...     print(number, end=' ')
...
1 2 3 4 5 6 7 8 9
```

Chain can also be used to concate a different amount of iterables to a list or tuple by using the `list()` or `tuple()` function.

```python
>>> import itertools
>>> list(itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### chain.from_iterable()

Works like chain but takes a single iterable argument and unpack that iterable into individual iterables.

```python
>>> import itertools
>>> for number in itertools.chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
...     print(number, end=' ')
...
1 2 3 4 5 6 7 8 9
```

### Compress()

`compress(iterable, selectors)` creates an irretator from the iterable where the corresponding selector is `True`.
The selector can hold bools but can also hold integers, where 0 is `False` and any other integer is `True`.

```python
>>> import itertools
>>> for letter in itertools.compress("Exercism", [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]):
...     print(letter, end=' ')
...
E r c s m
```

### Dropwhile()

skip

### Filterfalse()

skip

### Groupby()

probably skip

### Islice()

`islice(iterable, <start>, <stop>, <step>)` creates an irretator of the values from the iterable, from the start index to the stop index with a step size of step.

```python
>>> import itertools
>>> for letter in itertools.islice("Exercism", 2, 5, 2):
...     print(letter, end=' ')
...
e c
```

### Pairwise()

```exercism/note
`Pairwise()` requires Python 3.10+.
If you are using the online editor then you don't need to worry about this.
```

`Pairwise(iterable)` was intruduced in Python 3.10 and returns an iterator of overlapping pairs of values from the input iterable.

```python
>>> import itertools
>>> for pair in itertools.pairwise("Exercism"):
...     print(pair, end=' ')
...
('E', 'x') ('x', 'e') ('e', 'r') ('r', 'c') ('c', 'i') ('i', 's') ('s', 'm')
```

### Starmap()

Pehaps skip

### Takewhile()

skip

### Tee()

Talk with Bethany about

### Zip_longest()

#### Explaning zip

```exercism/caution
Zip in computer science(programming) is not the same as zip in computer terms.
Zip in computer terms reffers to a file format that supports compression.
While zip in computer science(programming) reffers to the `zip()` function.
```

`zip()` is a built in function and is not apart of the `itertools` module.
It takes any number of iterables and returns an iterator of tuples.
Where the i-th tuple contains the i-th element from each of the argument iterables.
Meaning the first tuple will contain the first element from each iterable, the second tuple will contain the second element from each iterable and so on.

```python
>>> zipped = zip(['x', 'y', 'z'], [1, 2, 3], [True, False, True])
>>> list(zipped)
[('x', 1, True),('y', 2, False), ('z', 3, True)]
```

If the iterables are not the same length, then the iterator will stop when the shortest iterable is exhausted.

```python
>>> zipped = zip(['x', 'y', 'z'], [1, 2, 3, 4], [True, False])
>>> list(zipped)
[('x', 1, True),('y', 2, False)]
```

#### Explaning zip_longest

`zip_longest(iterator, <fillvalue=None>)` is a function from the `itertools` module.
The difference between `zip_longest()` and `zip()` is that `zip_longest()` will continue until the longest iterable is exhausted.
If the iterables are not the same length the `fillvalue` will be used to fill in the missing values.
By the default the `fillvalue` is `None`.

```python
>>> import itertools
>>> zipped = itertools.zip_longest(['x', 'y', 'z'], [1, 2, 3, 4], [True, False])
>>> list(zipped)
[('x', 1, True),('y', 2, False), ('z', 3, None), (None, 4, None)]
```

An example where a fillvalue is given:

```python
>>> import itertools
>>> zipped = itertools.zip_longest(['x', 'y', 'z'], [1, 2, 3, 4], [True, False], fillvalue='fill')
>>> list(zipped)
[('x', 1, True),('y', 2, False), ('z', 3, 'fill'), ('fill', 4, 'fill')]
```

## Combinatoric iterators

### Product()

`product(iterable1, iterable2..., <repeat=1>)` creates an iterator of tuples where the i-th tuple contains the i-th element from each of the argument iterables.
The repeat keyword argument can be used to specify the number of times the input iterables are repeated.
By default the repeat keyword argument is 1.

```python
>>> import itertools
>>> for product in itertools.product("ABCD", repeat=1):
...     print(product, end=' ')
...
('A',) ('B',) ('C',) ('D',)
```

```python
>>> import itertools
>>> for product in itertools.product("ABCD", repeat=2):
...     print(product, end=' ')
...
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'C') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C') ('D', 'D')
```

The last one here can be seen as doing a nested for loop.
When you increase the repeat value the number of iterations increases exponentially.
The example above is a n\*\*2 iteration.

```python
>>> import itertools
>>> for letter1 in "ABCD":
...     for letter2 in "ABCD":
...         print((letter1, letter2), end=' ')
...
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'C') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C') ('D', 'D')
```

You can also give it multiple iterables.

```python
>>> import itertools
>>> for product in itertools.product("ABCD", "xy" repeat=1):
...     print(product, end=' ')
...
('A', 'x') ('A', 'y') ('B', 'x') ('B', 'y') ('C', 'x') ('C', 'y') ('D', 'x') ('D', 'y')
```

Here is an example of doing it wihout `product()`.
It looks similliar to the last example but since we have two iterables we need to nest the for loops.
Even though the proudct is given repeat=1.
The reasson to why it is only 2 for loops earlier was because we only had one iterable.
If we had two iterables and gave it repeat=2 we would need 4 for loops.
Since 2 \* 2 = 4.

```python
>>> for letter1 in "ABCD":
...     for letter2 in "xy":
...         print((letter1, letter2), end=' ')
...
('A', 'x') ('A', 'y') ('B', 'x') ('B', 'y') ('C', 'x') ('C', 'y') ('D', 'x') ('D', 'y')
```

### Permutations()

`permutations(iterable, <r=None>)` creates an iterator of tuples.
It works like `product()` but it doesnt repeat values from a specific positoon from the iterable and can only take one iterable.
The "r" keyword argument can be used to specify the number of times the input iterables are repeated.
By default the "r" keyword argument is None.
If "r" is None then the length of the iterable is used.

```python
>>> import itertools
>>> for permutation in itertools.permutations("ABCD", repeat=1):
...     print(permutation, end=' ')
...
('A',) ('B',) ('C',) ('D',)
```

```python
>>> import itertools
>>> for permutation in itertools.permutations("ABCD", repeat=2):
...     print(permutation, end=' ')
...
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'A') ('B', 'C') ('B', 'D') ('C', 'A') ('C', 'B') ('C', 'D') ('D', 'A') ('D', 'B') ('D', 'C')
```

### Combinations()

`combinations(iterable, r)` finds all the possible combinations of the given iterable.
The r keyword argument is used to specify the length of the tuples generated.

```python
>>> import itertools
>>> for combination in itertools.combinations("ABCD", 2):
...     print(combination, end=' ')
...
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'C') ('B', 'D') ('C', 'D')
```

### Combinations_with_replacement()

`combinations_with_replacement(iterable, r)` finds all the possible combinations of the given iterable.
The r keyword argument is used to specify the length of the tuples generated.
The difference between this and `combinations()` is that it can repeat values.

```python
>>> import itertools
>>> for combination in itertools.combinations_with_replacement("ABCD", 2):
...     print(combination, end=' ')
...
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'C') ('C', 'D') ('D', 'D')
```
