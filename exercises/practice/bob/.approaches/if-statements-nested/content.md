# `if` statements nested

```python
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if is_shout:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return 'Whoa, chill out!'
    if is_question:
        return 'Sure.'
    return 'Whatever.'    

```

In this approach you have a series of `if` statements using the calculated variables to evaluate the conditions, some of which are nested.
As soon as a `True` condition is found, the correct response is returned.

```exercism/note
Note that there are no `elif` or `else` statements.
If an `if` statement can return, then an `elif` or `else` is not needed.
Execution will either return or will continue to the next statement anyway.
```

The [`rstrip`][rstrip] method is applied to the input to eliminate any whitespace at the end of the input.
If the input has no characters left, it uses the [falsiness][falsiness] of an empty string with the [`not`][not] operator to return the response for saying nothing.
Since it doesn't matter if there is leading whitespace, the `rstrip` function is used instead of [`strip`][strip].

The [`isupper`][isupper] method is used to test that there is at least one cased character and that all cased characters are uppercase.

```exercism/note
A cased character is one which differs between lowercase and uppercase.
For example, `?` and `3` are not cased characters, as they do not change between lowercase and uppercase.
`a` and `z` are cased characters, since their lowercase form changes to `A` and ` Z` when uppercase.
```

The [`endswith`][endswith] method is used to determine if the input ends with a question mark.

Instead of testing a shout and a question on the same line, this approach first tests if the input is a shout.
If it is a shout, then the nested `if`/[`else`][else] statement returns if it is a shouted question or just a shout.
If it is not a shout, then the flow of execution skips down to the non-nested test for if the input is a question.

[rstrip]: https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[not]: https://docs.python.org/3/reference/expressions.html#not
[strip]: https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip
[isupper]: https://docs.python.org/3/library/stdtypes.html?highlight=isupper#str.isupper
[endswith]: https://docs.python.org/3/library/stdtypes.html?highlight=endswith#str.endswith
[else]: https://docs.python.org/3/reference/compound_stmts.html#else
