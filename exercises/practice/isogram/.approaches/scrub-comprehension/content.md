# Scrub with a list comprehension

```python
def is_isogram(phrase):
    scrubbed = [ltr.lower() for ltr in phrase if ltr.isalpha()]
    return len(set(scrubbed)) == len(scrubbed)

```

For this approach, a [list comprehension][list-comprehension] is used to iterate the letters in the input phrase [str][str]ing.

- In the code example, `ltr` is the name given to each letter iterated in the [`for`][for] loop.
- The result of each iteration is `ltr.lower()`, which is the [`lower`][lower]cased letter being iterated.
All of the letters are lowercased so that letters of different cases will become the same letter for comparison purposes,
since `A` and `a` are considered to be the same letter.
- The iterable part of the list comprehension is the input phrase.
- The letters are filtered by the use of the [optional conditional logic][conditional-logic]: `if ltr.isalpha()`.
[`isalpha()`][isalpha] returns `True` if the letter being iterated is alphabetic.

When the list comprehension is done, the scrubbed variable will be a list holding only lowercased alphabetic characters.
- A [`set`][set] is constructed from the scrubbed list and its [`len`][len] is compared with the `len` of the the scrubbed list.
Since a `set` holds only unique values, the phrase will be an isogram if its number of unique letters is the same as its total number of letters.
The function returns whether the number of unique letters equals the total number of letters.
- For `Alpha` it would return `False`, because `a` is considered to repeat `A`, so the number of unique letters in `Alpha` is `4`,
and the total number of letters in `Alpha` is `5`.
- For `Bravo` it would return `True`, since the number of unique letters in `Bravo` is `5`, and the total number of letters in `Bravo` is `5`.


[list-comprehension]: https://realpython.com/list-comprehension-python/#using-list-comprehensions
[str]: https://docs.python.org/3/library/stdtypes.html#textseq
[lower]: https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.lower
[for]: https://realpython.com/python-for-loop/#the-python-for-loop
[conditional-logic]: https://realpython.com/list-comprehension-python/#using-conditional-logic
[isalpha]: https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.isalpha
[set]: https://docs.python.org/3/library/stdtypes.html?highlight=set#set
[len]: https://docs.python.org/3/library/functions.html?highlight=len#len
