# About


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
