# Tuples with `sequence.index()`

```python
OPERATOR_WORDS = ("plus", "minus", "multiplied", "divided")

EXTRA_OPERATOR_WORDS = (None, None, "by", "by")


def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    words = question[:-1].split(" ")
    result = str_to_int(words[2])
    index = 3

    while index < len(words):
        try:
            operator_index = OPERATOR_WORDS.index(words[index])
        except ValueError:
            str_to_int(words[index], "unknown operation")
            raise ValueError("syntax error")

        operand_index = index + 1
        if EXTRA_OPERATOR_WORDS[operator_index] is not None:
            if index + 1 >= len(words) or words[index + 1] != EXTRA_OPERATOR_WORDS[operator_index]:
                raise ValueError("syntax error")
            operand_index += 1

        if operand_index >= len(words):
            raise ValueError("syntax error")

        operand = str_to_int(words[operand_index])
        match operator_index:
            case 0: result += operand
            case 1: result -= operand
            case 2: result *= operand
            case 3: result //= operand

        index = operand_index + 1

    return result


def str_to_int(string, err_msg = "syntax error"):
    try:
        return int(string)
    except ValueError:
        raise ValueError(err_msg)
```

This approach starts with declaring the `OPERATOR_WORDS` tuple, which contains the first word of each phrase that indicates an operator.
The `EXTRA_OPERATOR_WORDS` tuple contains the second word of each phrase if it exists, and [`None`][none] otherwise.

In `answer()`, we start by checking that the question starts with "What is " and ends with "?".
(Unlike many other approaches, it does not rely on explicitly checking for "cubed".)
Next, the question is `split` into a `words` list, excluding the trailing "?".

Then we call the helper function `str_to_int()` to initialize `result` to the first number in the question, or raise a `ValueError` if the third "word" is not a number.
Next, we start the while loop with `index` set to `3`, indicating that we have finished parsing the first `3` words ("What", "is", and the number).

Inside the loop, we use [`OPERATOR_WORDS.index()`][sequence-index-method] to get the index of the operator at index `index` of `words`.
If `words[index]` is not an operator word, the raised `ValueError` will be caught by the [`try-except`][handling-exceptions] statement, and the `except` block will determine the correct error to raise instead.

Next, we need to get the second operand for the operator (we already have `result` for the first one), so we set `operand_index = index + 1`.
However, some operator phrases are multiple words long, so we need to check if `EXTRA_OPERATOR_WORDS[operator_index] is not None`.
If there *is* an extra operator word, then we need to check if it is present as the next word in `words`.
If it is not present, we raise a `ValueError`, else we increment `operand_index` by `1` to get the correct index.

Here we call the helper function again, setting `operand` to the number at index `operand_index`, and raising a `ValueError` if it is not a number.
After this, the approach uses [structural pattern matching][structural-pattern-matching] to modify `result` using `+=`, `-=`, `*=`, or `//=` depending on the `operator_index`.
However, this section could easily be modified to use a similar method to any of the other approaches, such as an `if-elif-else` block or a tuple of `lambda`s.

At the end of the loop, we set `index` to `operand_index + 1`, as we have finished processing everything up to and including `operand_index`.
Then the loop continues until `index` reaches or exceeds `len(words)` or something raises an uncaught error.
When the loop ends, we know that we have finished processing the whole string, and thus we return `result`.

[handling-exceptions]: https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions
[none]: https://docs.python.org/3/library/constants.html#None
[sequence-index-method]: https://docs.python.org/3/library/stdtypes.html#sequence.index
[structural-pattern-matching]: https://peps.python.org/pep-0636/
