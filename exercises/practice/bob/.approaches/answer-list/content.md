# Answer list

```python
ANSWERS = ['Whatever.', 'Sure.', 'Whoa, chill out!',
            "Calm down, I know what I'm doing!"]


def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = 2 if hey_bob.isupper() else 0
    is_question = 1 if hey_bob.endswith('?') else 0
    return ANSWERS[is_shout + is_question]

```

In this approach you define a [list][list] that contains Bob’s answers, and each condition is given a score.
The correct answer is selected from the list by using the score as the list index.

Python doesn't _enforce_ having real constant values,
but the `ANSWERS` list is defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

```exercism/note
`ANSWERS` could prevent item reassignment by being defined as a [tuple](https://realpython.com/python-lists-tuples/#python-tuples) instead of a list.
The items in a tuple cannot be changed, and the performance between a tuple and a list here is equivalent.
The entire `ANSWERS` tuple could still be reassigned to another tuple,
so uppercase letters would still be used to indicate that the `ANSWERS` tuple should not be changed.
```

The [`rstrip`][rstrip] method is applied to the input to eliminate any whitespace at the end of the input.
If the input has no characters left, it uses the [falsiness][falsiness] of an empty string with the [`not`][not] operator to return the response for saying nothing.
Since it doesn't matter if there is leading whitespace, the `rstrip` function is used instead of [`strip`][strip].

A [ternary operator][ternary] is used for determining the score for a shout and a question.

The [`isupper`][isupper] method is used to test that there is at least one cased character and that all cased characters are uppercase.

```exercism/note
A cased character is one which differs between lowercase and uppercase.
For example, `?` and `3` are not cased characters, as they do not change between lowercase and uppercase.
`a` and `z` are cased characters, since their lowercase form changes to `A` and ` Z` when uppercase.
```

If `isupper` is `True`, then `is_shout` is given the value of `2`; otherwise, it is given the value of `0`.

The [`endswith`][endswith] method is used to determine if the input ends with a question mark.
If the test for `endswith('?')` is `True`, then `is_question` is given the value of `1`; otherwise it is given the value of `0`.


The response is selected from the list by the index like so

| is_shout | is_question | Index     | Answer                                |
| -------- | ----------- | --------- | ------------------------------------- |
| `false`  | `false`     | 0 + 0 = 0 | `"Whatever."`                         |
| `false`  | `true`      | 0 + 1 = 1 | `"Sure."`                             |
| `true`   | `false`     | 2 + 0 = 2 | `"Whoa, chill out!"`                  |
| `true`   | `true`      | 2 + 1 = 3 | `"Calm down, I know what I'm doing!"` |


[list]: https://docs.python.org/3/library/stdtypes.html?highlight=list#list
[const]: https://realpython.com/python-constants/
[rstrip]: https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[not]: https://docs.python.org/3/reference/expressions.html#not
[strip]: https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.strip
[ternary]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[isupper]: https://docs.python.org/3/library/stdtypes.html?highlight=isupper#str.isupper
[endswith]: https://docs.python.org/3/library/stdtypes.html?highlight=endswith#str.endswith
