# `if` statements

```python
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    isShout = hey_bob.isupper()
    isQuestion = hey_bob.endswith('?')
    if isShout and isQuestion:
        return "Calm down, I know what I'm doing!"
    if isShout:
        return 'Whoa, chill out!'
    if isQuestion:
        return 'Sure.'
    return 'Whatever.'
    
```

In this approach you have a series of `if` statements using the calculated variables to evaluate the conditions.
As soon as the right condition is found, the correct response is returned.

```exercism/note
Note that there are no `elif` or `else` statements.
If an `if` statement can return, then an `elif` or `else` is not needed.
Execution will either return or will continue to the next statement anyway.
```

The [rstrip][rstrip] method is applied to the input to eliminate any whitespace at the end of the input.
If the string has no characters left, it uses the [falsiness][falsiness] of an emptry string with the [`not`][not] operator to return the response for saying nothing.
Since it doesn't matter if there is leading whitespace, the [rstrip][rstrip] function is used instead of `strip`.

The [isupper][isupper] method is used to test that there is at least one uppercased character and that all characters are uppercased.

The [endswith][endswith] method is used to determine if the input ends with a question mark.

[rstrip]: https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[not]: https://docs.python.org/3/reference/expressions.html#not
[rstrip]: https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
[isupper]: https://docs.python.org/3/library/stdtypes.html?highlight=isupper#str.isupper
[endswith]: https://docs.python.org/3/library/stdtypes.html?highlight=endswith#str.endswith
