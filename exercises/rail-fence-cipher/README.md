# Rail Fence Cipher

Implement encoding and decoding for the rail fence cipher.

The Rail Fence cipher is a form of transposition cipher that gets its name from
the way in which it's encoded. It was already used by the ancient Greeks.

In the Rail Fence cipher, the message is written downwards on successive "rails"
of an imaginary fence, then moving up when we get to the bottom (like a zig-zag).
Finally the message is then read off in rows.

For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE",
the cipherer writes out:

```text
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
```

Then reads off:

```text
WECRLTEERDSOEEFEAOCAIVDEN
```

To decrypt a message you take the zig-zag shape and fill the ciphertext along the rows.

```text
? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
```

The first row has seven spots that can be filled with "WECRLTE".

```text
W . . . E . . . C . . . R . . . L . . . T . . . E
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
```

Now the 2nd row takes "ERDSOEEFEAOC".

```text
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
```

Leaving "AIVDEN" for the last row.

```text
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
```

If you now read along the zig-zag shape you can read the original message.


## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you should write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Running the tests

To run the tests, run `pytest rail_fence_cipher_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest rail_fence_cipher_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/rail-fence-cipher` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Wikipedia [https://en.wikipedia.org/wiki/Transposition_cipher#Rail_Fence_cipher](https://en.wikipedia.org/wiki/Transposition_cipher#Rail_Fence_cipher)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
