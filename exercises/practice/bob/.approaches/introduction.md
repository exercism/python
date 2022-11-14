# Introduction

There are various idiomatic approaches to solve Bob.
A basic approach can use a series of `if` statements to test the conditions.
The `if` statements could also be nested.
An array can contain answers from which the right response is selected by an index calculated from scores given to the conditions.

## General guidance

Regardless of the approach used, some things you could look out for include

- If the input is stripped, [rstrip][rstrip] only once.

- Use the [endsWith][endswith] `str` method instead of checking the last character by index for `?`.

- Don't copy/paste the logic for determining a shout and for determing a question into determing a shouted question.
  Combine the two determinations instead of copying them.
  Not duplicating the code will keep the code [DRY][dry].

- Perhaps consider making `IsQuestion` and `IsShout` values set once instead of functions that are possibly called twice.

- If an `if` statement can return, then an `elif` or `else` is not needed.
  Execution will either return or will continue to the next statement anyway.

## Approach: `if` statements

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

For more information, check the [`if` statements approach][approach-if].

## Approach: `if` statements nested

```python
def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    isShout = hey_bob.isupper()
    isQuestion = hey_bob.endswith('?')
    if isShout:
        if isQuestion:
            return "Calm down, I know what I'm doing!"
        else:
            return 'Whoa, chill out!'
    if isQuestion:
        return 'Sure.'
    return 'Whatever.'    

```

For more information, check the [`if` statements nested approach][approach-if-nested].

## Other approaches

Besides the aforementioned, idiomatic approaches, you could also approach the exercise as follows:

### Other approach: answer array

An array can be defined that contains Bob’s answers, and each condition is given a score.
The correct answer is selected from the array by using the score as the array index.
For more information, check the [Answer array approach][approach-answer-array].

put code here for now

```python
_ANSWERS = ['Whatever.', 'Sure.', 'Whoa, chill out!',
            "Calm down, I know what I'm doing!"]


def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return 'Fine. Be that way!'
    isShout = (2 if hey_bob.isupper() else 0)
    isQuestion = (1 if hey_bob.endswith('?') else 0)
    return _ANSWERS[isShout + isQuestion]

```

## Which approach to use?

The nested `if` approach is fastest, but some may consider it a bit less readable than the unnested `if` statements.
The answer array approach is slowest, but some may prefer doing away with the chain of `if` statements.

- To compare the performance of the approaches, check out the [Performance article][article-performance].

[rstrip]: https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
[endswith]: https://docs.python.org/3/library/stdtypes.html?highlight=strip#str.endswith
[dry]: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
[approach-if]: https://exercism.org/tracks/python/exercises/bob/approaches/if-statements
[approach-if-nested]: https://exercism.org/tracks/python/exercises/bob/approaches/if-statements-nested
[approach-answer-array]: https://exercism.org/tracks/python/exercises/bob/approaches/answer-array
[article-performance]: https://exercism.org/tracks/python/exercises/bob/articles/performance
