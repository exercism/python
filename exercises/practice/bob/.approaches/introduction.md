# Introduction

There are various idiomatic approaches to solve Bob.
A basic approach can use a series of `if` statements to test the conditions.
The `if` statements could also be nested.
A list can contain answers from which the right response is selected by an index calculated from scores given to the conditions.

## General guidance

Regardless of the approach used, some things you could look out for include

- If the input is stripped, [`rstrip`][rstrip] only once.

- Use the [`endswith`][endswith] method instead of checking the last character by index for `?`.

- Don't copy/paste the logic for determining a shout and for determing a question into determing a shouted question.
  Combine the two determinations instead of copying them.
  Not duplicating the code will keep the code [DRY][dry].

- Perhaps consider making `is_question` and `is_shout` values set once instead of functions that are possibly called twice.

- If an `if` statement can return, then an `elif` or `else` is not needed.
  Execution will either return or will continue to the next statement anyway.

## Approach: `if` statements

```python
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if is_shout and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shout:
        return 'Whoa, chill out!'
    if is_question:
        return 'Sure.'
    return 'Whatever.'
    
```

For more information, check the [`if` statements approach][approach-if].

## Approach: `if` statements nested

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

For more information, check the [`if` statements nested approach][approach-if-nested].

## Other approaches

Besides the aforementioned, idiomatic approaches, you could also approach the exercise as follows:

### Other approach: answer list

A list can be defined that contains Bob’s answers, and each condition is given a score.
The correct answer is selected from the list by using the score as the list index.
For more information, check the [answer list approach][approach-answer-list].

## Which approach to use?

The nested `if` approach is fastest, but some may consider it a bit less readable than the unnested `if` statements.
The answer list approach is slowest, but some may prefer doing away with the chain of `if` statements.
Since the difference between them is a few nanoseconds, which one is used may be a matter of stylistic preference.

- To compare the performance of the approaches, check out the [Performance article][article-performance].

[rstrip]: https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
[endswith]: https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.endswith
[dry]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
[approach-if]: https://exercism.org/tracks/python/exercises/bob/approaches/if-statements
[approach-if-nested]: https://exercism.org/tracks/python/exercises/bob/approaches/if-statements-nested
[approach-answer-list]: https://exercism.org/tracks/python/exercises/bob/approaches/answer-list
[article-performance]: https://exercism.org/tracks/python/exercises/bob/articles/performance
