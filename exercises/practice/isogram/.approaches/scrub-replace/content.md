# Scrub with `replace()`

```python
def is_isogram(phrase):
    scrubbed = phrase.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))

```

For this approach, [`replace()`][replace] is called a couple times to scrub the input phrase [str][str]ing.
Thw two `replace()` calls are [chained][method-chaining], so the output of the first `replace()` is the input for the next `replace()`.
The output of the last `replace()` is the input for [`lower()`][lower].
All of the letters are lowercased so that letters of different cases will become the same letter for comparison purposes,
since `A` and `a` are considered to be the same letter.
When the replacing and lowercasing is done, the scrubbed variable will be a string having no hyphens or spaces,
and with all alphabetic letters lowercased.
- A [`set`][set] is constructed from the scrubbed string and its [`len`][len] is compared with the `len` of the the scrubbed string.
Since a `set` holds only unique values, the phrase will be an isogram if its number of unique letters is the same as its total number of letters.
The function returns whether the number of unique letters equals the total number of letters.
- For `Alpha` it would return `False`, because `a` is considered to repeat `A`, so the number of unique letters in `Alpha` is `4`,
and the total number of letters in `Alpha` is `5`.
- For `Bravo` it would return `True`, since the number of unique letters in `Bravo` is `5`, and the total number of letters in `Bravo` is `5`.


[replace]: https://docs.python.org/3/library/stdtypes.html?highlight=replace#str.replace
[str]: https://docs.python.org/3/library/stdtypes.html#textseq
[method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
[lower]: https://docs.python.org/3/library/stdtypes.html?highlight=lower#str.lower
[set]: https://docs.python.org/3/library/stdtypes.html?highlight=set#set
[len]: https://docs.python.org/3/library/functions.html?highlight=len#len

