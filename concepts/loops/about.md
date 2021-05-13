# About

Python has two looping constructs.
`while` loops for _indefinite_ (uncounted) iteration and `for` loops for _definite_, (counted) iteration.
The keywords `break`, `continue`, and `else` help customize loop behavior.

<br>

## `While`

[`while`][while statement] loops continue to exectute as long as the loop expression or "test" evaluates to `True` in a [`boolean context`][truth value testing], terminating when it evaluates to `False`.

```python

# Lists are considered "truthy" in a boolean context if they
# contain one or more values, and "falsy" if they are empty.

>>> placeholders = ["spam", "ham", "eggs", "green_spam", "green_ham", "green_eggs"]

>>> while 'eggs' in placeholders:
...     print(placeholders.pop(0))
...
spam
ham
eggs

>>> print(placeholders)
['green_spam', 'green_ham', 'green_eggs']
<br>

## `For`

The basic [`for`][for statement] loop is better described as a _`for each`_ which cycles through the values of any [iterable object][iterable], terminating when there are no values returned from calling [`next()`][next built-in] (_raising a [`StopIteration`][stopiteration]_).

```python

>>> word_list = ["bird", "chicken", "barrel", "bongo"]

>>> for word in word_list:
...    if word.startswith("b"):
...        print(f"{word.title()} starts with a B.")
...    else:
...        print(f"{word.title()} doesn't start with a B.")
...
Bird starts with a B.
Chicken doesn't start with a B.
Barrel starts with a B.
Bongo starts with a B.

```

<br>

## Sequence Object `range()`

When there isn't a specific `iterable` given, the special [`range()`][range] sequence is used.  
`range()` requires a number before which to `stop`, and can optionally take a `start` parameter.  
If no `start` number is provided, the sequence will begin with 0.  
`range()` objects are `lazy` (_values are generated on request_), support all [common sequence operations][common sequence operations], and take up a fixed amount of memory, no matter how long the sequence.
Interestingly, `range()` [is not an iterator][range is not an iterator], and can be used many in non-looping contexts.

```python
# Here we use range to produce some numbers, rather than creating a list of them in memory.
# The values will start with 1 and stop *before* 7

>>> for number in range(1, 7):
...    if number % 2 == 0:
...       print(f"{number} is even.")
...    else:
...       print(f"{number} is odd.")
1 is odd.
2 is even.
3 is odd.
4 is even.
5 is odd.
6 is even.


# range() can also take a *step* parameter.
# Here we use range to produce only the "odd" numbers, starting with 3 and stopping *before* 15.

>>> for number in range(3, 15, 2):
...    if number % 2 == 0:
...       print(f"{number} is even.")
...    else:
...       print(f"{number} is odd.")
...
3 is odd.
5 is odd.
7 is odd.
9 is odd.
11 is odd.
13 is odd.

```

<br>

## Values and Indexes with `enumerate()`

If both values and indexes are needed, the built-in [`enumerate()`][enumerate] will return an [`iterator`][iterator] over (`index`, `value`) pairs:

```python

>>> word_list = ["bird", "chicken", "barrel", "apple"]

# *index* and *word* are the loop variables.
# Loop variables can be any valid python name.

>>> for index, word in enumerate(word_list):
...    if word.startswith("b"):
...        print(f"{word.title()} (at index {index}) starts with a B.")
...    else:
...        print(f"{word.title()} (at index {index}) doesn't start with a B.")
...
Bird (at index 0) starts with a B.
Chicken (at index 1) doesn't start with a B.
Barrel (at index 2) starts with a B.
Apple (at index 3) doesn't start with a B.


# enumerate() can also be set to *start* the index count at a different number.
# Here, the index count will start at 1.

>>> for position, word in enumerate(word_list, start=1):
...    if word.startswith("b"):
...        print(f"{word.title()} (at position {position}) starts with a B.")
...    else:
...        print(f"{word.title()} (at position {position}) doesn't start with a B.")
...
Bird (at position 1) starts with a B.
Chicken (at position 2) doesn't start with a B.
Barrel (at position 3) starts with a B.
Apple (at position 4) doesn't start with a B.

```

<br>

## Altering Loop Behavior

[`continue`][continue statement] can be used to skip forward to the next iteration.

```python
word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple", "bear"]

# This will skip *bird*, at index 0
for index, word in enumerate(word_list):
    if index == 0:
        continue
    if word.startswith("b"):
        print(f"{word.title()} (at index {index}) starts with a b.")

Barrel (at index 2) starts with a b.
Bongo (at index 3) starts with a b.
Bear (at index 6) starts with a b.

```

[`break`][break statement] (_like in many C-related languages_) can be used to stop the iteration and "break out" of the innermost enclosing loop.

```python
>>>  word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]

>>> for index, word in enumerate(word_list):
...    if word.startswith("b"):
...        print(f"{word.title()} (at index {index}) starts with a B.")
...    elif word == 'sliver':
...        break
...    else:
...        print(f"{word.title()} doesn't start with a B.")
...print("loop broken.")
...
Bird (at index 0) starts with a B.
Chicken doesn't start with a B.
Barrel (at index 2) starts with a B.
Bongo (at index 3) starts with a B.
loop broken.

```

The loop [`else` clause][loop else] is unique to python, and can be used as a "wrap up" or "concluding" action for when iteration has been exhausted. `else` statements will not run if iteration terminates through a `break` statement.

```python
>>> word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]

# Using enumerate to get both an index and a value.

>>> for index, word in enumerate(word_list):
...    word = word.title()
...    if word.startswith("B"):
...        print(f"{word} (at index {index}) starts with a B.")
...# This executes once *StopIteration* is raised and there are no more items.
...else:
...    print(f"Found the above b-words, out of {len(word_list)} words in the word list.")
...
Bird (at index 0) starts with a B.
Barrel (at index 2) starts with a B.
Bongo (at index 3) starts with a B.
Found the above b-words, out of 6 words in the word list.


# Terminating a loop via *break* will bypass the loop *else* clause

>>> for index, word in enumerate(word_list):
...    word = word.title()
...    if word.startswith("B"):
...       print(f"{word} (at index {index}) starts with a B.")
...    if word.startswith("S"):
...        print("Found an S, stopping iteration.")
...        break
...# This is not run, because break was triggered
... else:
...    print(f"Found the above b-words, out of {len(word_list)} words in the word list.")
...
Bird (at index 0) starts with a B.
Barrel (at index 2) starts with a B.
Bongo (at index 3) starts with a B.
Found an S, stopping iteration.

```

[next built-in]: https://docs.python.org/3/library/functions.html#next
[stopiteration]: https://docs.python.org/3/library/exceptions.html#StopIteration
[loop else]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
[for statement]: https://docs.python.org/3/reference/compound_stmts.html#for
[range]: https://docs.python.org/3/library/stdtypes.html#range
[break statement]: https://docs.python.org/3/reference/simple_stmts.html#the-break-statement
[continue statement]: https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement
[while statement]: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
[iterable]: https://docs.python.org/3/glossary.html#term-iterable
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
[enumerate]: https://docs.python.org/3/library/functions.html#enumerate
[iterator]: https://docs.python.org/3/glossary.html#term-iterator
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[range is not an iterator]: https://treyhunner.com/2018/02/python-range-is-not-an-iterator/
