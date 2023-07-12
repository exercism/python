# About

[`itertools`][itertools] is a module in the Python standard library that provides a number of functions that create iterators for more efficient looping.

[Iterators][iterators] are objects that represent a stream of data.

An example is the "stream" of data when you iterate over a `list` in a `for <item> in <list>:` loop.


Many functions in `itertools` are very useful for looping/iterating over data streams in various ways.

These functions often enhance the readability and/or maintainability of the code.


This concept will cover a selection of these functions and how to use them:


- `chain()`
- `chain.from_iterable()`
- `compress()`
- `islice()`
- `pairwise()`
- `zip_longest()`
- `product()`
- `permutations()`
- `combinations()`
- `count()`
- `cycle()`

There are more functions in the itertools module, like:

- `accumulate()`
-`combinations_with_replacement()`
- `groupby()`

- `repeat()`
- `starmap()`

- `takewhile()`
- `dropwhile()`
- `filterfalse()`

These functions will be covered in a later concept.

`count()`, `cycle()`, and `repeat()` are categorized as infinite iterators.

These iterators will never terminate and will keep looping forever.

## Iterators terminating on the shortest input sequence

### Chain()

`chain(iterable1, iterable2...)` creates an iterator of values from the iterables in the order they are given.

```python
>>> import itertools
>>> for number in itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9]):
...     print(number, end=' ')
...
1 2 3 4 5 6 7 8 9
```

Since `chain()` takes iterables as arguments, so can it take it for example take: `set`, `tuple`, `list`, `str`, and more.
You can give iterables of different types at the same time.

```python
>>> import itertools
>>> for number in itertools.chain([1, 2, 3], (4, 5, 6), {7, 8, 9}, "abc"):
...     print(number, end=' ')
...
1 2 3 4 5 6 7 8 9 a b c
```

Chain can also be used to concate a different amount of iterables to a list or tuple by using the `list()` or `tuple()` function.

Using `list()`:

```python
>>> import itertools
>>> list(itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Using `tuple()`:

```python
>>> import itertools
>>> tuple(itertools.chain([1, 2, 3], [4, 5, 6], [7, 8, 9]))
(1, 2, 3, 4, 5, 6, 7, 8, 9)
```

### chain.from_iterable()

`chain.from_iterable()` works like `chain` but takes a single nested iterable.
Then the method unpack that iterable into individual iterables.

```python
>>> import itertools
>>> for number in itertools.chain.from_iterable(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]):
...     print(number, end=' ')
...
1 2 3 4 5 6 7 8 9
```

### Compress()

`compress(iterable, selectors)` creates an iterator from the input iterable where the corresponding selector is `True`.
The selector can be `True`/`False` or integers, where 0 is `False` and 1 is `True`.
You can read more about the behavior when [numbers act like booleans][numbers-as-boolean-values].

```python
>>> import itertools
>>> for letter in itertools.compress("Exercism", [1, 0, 0, 1, 1, 0, 1, 1]):
...     print(letter, end=' ')
...
E r c s m
```

With `True`/`False`:

```python
>>> import itertools
>>> for letter in itertools.compress("Exercism", [True, False, False, True, True, False, True, True]):
...     print(letter, end=' ')
...
E r c s m
```

### Islice()

`islice(iterable, start, <stop>, <step>)` creates a new iterator from the slice (from the start index to the stop index with a step size of step).

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

`Pairwise(iterable)` was introduced in Python 3.10 and returns an iterator of overlapping pairs of values from the input iterable.

```python
>>> import itertools
>>> for pair in itertools.pairwise("Exercism"):
...     print(pair, end=' ')
...
('E', 'x') ('x', 'e') ('e', 'r') ('r', 'c') ('c', 'i') ('i', 's') ('s', 'm')
```

### Tee()

Talk with Bethany about

### Zip_longest()

#### Explaining zip

```exercism/caution
Pythons `zip()` function should not be confused with the zip compression format.
```

`zip()` is a built in function and is not apart of the `itertools` module.
It takes any number of iterables and returns an iterator of tuples.
Where the i-th tuple contains the i-th element from each of the argument iterables.
For example, the first tuple will contain the first element from each iterable, the second tuple will contain the second element from each iterable, and so on until the shortest iterable is exhausted.

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

#### Explaining zip_longest

`zip_longest(iterator, <fillvalue=None>)` is a function from the `itertools` module.
Unlike `zip()`, it will not stop when the shortest iterable is exhausted.
If the iterables are not the same length, `fillvalue` will be used to pad missing values.
By the default the `fillvalue` is `None`.

```python
>>> import itertools
>>> zipped = itertools.zip_longest(['x', 'y', 'z'], [1, 2, 3, 4], [True, False])
>>> list(zipped)
[('x', 1, True),('y', 2, False), ('z', 3, None), (None, 4, None)]
```

An example where a `fillvalue` is given:

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

Giving a repeat value of 2:

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

Here is an example of doing it without `product()`.
It looks similar to the last example but since we have two iterables we need to nest the for loops.
Even though the product is given repeat=1.
The reason to why it is only 2 for loops earlier was because we only had one iterable.
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
It works like `product()` but it doesn't repeat values from a specific position from the iterable and can only take one iterable.
The **r** keyword argument can be used to specify the number of times the input iterables are repeated.
By default the **r** keyword argument is None.
If **r** is None then the length of the iterable is used.

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
The **r** keyword argument is used to specify the length of the tuples generated.

```python
>>> import itertools
>>> for combination in itertools.combinations("ABCD", 2):
...     print(combination, end=' ')
...
('A', 'B') ('A', 'C') ('A', 'D') ('B', 'C') ('B', 'D') ('C', 'D')
```

### Combinations_with_replacement()

`combinations_with_replacement(iterable, r)` finds all the possible combinations of the given iterable.
The **r** keyword argument is used to specify the length of the tuples generated.
The difference between this and `combinations()` is that it can repeat values.
That means that if you have "AB" and you want to find all the combinations of length 2 you will get `("A", "A"), ("A", "B"), ("B", "B")`.
While with `combinations()` you would only get `("A", "B")`.

```python
>>> import itertools
>>> for combination in itertools.combinations_with_replacement("ABCD", 2):
...     print(combination, end=' ')
...
('A', 'A') ('A', 'B') ('A', 'C') ('A', 'D') ('B', 'B') ('B', 'C') ('B', 'D') ('C', 'C') ('C', 'D') ('D', 'D')
```

## Infinite iterators

Most of iterator from the `itertools` module get exhausted after a time.
But there are some that are infinite, these are known as infinite iterators.
These iterators will will keep producing values until you tell them to stop.

```exercism/note
To avoid infinite loops, you can use `break` to end a loop.
```

### Count()

`count(start, <step>)` produces all values from the start value to infinity.
Count also has an optional step parameter, which will produce values with a step size other than 1.

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

Giving `count()` a negative step size will produces values in a descending order.

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

`cycle(iterable)` produces all values from the iterable in an infinite loop.
A `list`, `tuple`, `string`, `dict` or any other iterable can be used.

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

`repeat(object, <times>)` produces the same value in an infinite loop.
Although if the optional times parameter is given, the value will produces that many times.
Meaning that it is not an infinite loop if that parameter is given.

```python
>>> import itertools
>>> for number in itertools.repeat(5, 3):
...     print(number, end=' ')
...
5 5 5
```

[itertools]: https://docs.python.org/3/library/itertools.html
[numbers-as-boolean-values]: https://realpython.com/python-boolean/#numbers-as-boolean-values
