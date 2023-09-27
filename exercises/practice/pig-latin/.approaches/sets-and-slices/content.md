# Sets and slices

```python
VOWELS = {"a", "e", "i", "o", "u"}
VOWELS_Y = {"a", "e", "i", "o", "u", "y"}
SPECIALS = {"xr", "yt"}


def translate(text):
    piggyfied = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIALS:
            piggyfied.append(word + "ay")
            continue

        for pos in range(1, len(word)):
            if word[pos] in VOWELS_Y:
                pos += 1 if word[pos] == 'u' and word[pos - 1] == "q" else 0
                piggyfied.append(word[pos:] + word[:pos] + "ay")
                break

    return " ".join(piggyfied)

```

This approach begins by defining [sets][set] for looking up matching characters from the input.
Python doesn't _enforce_ having real constant values,
but the sets are defined with all uppercase letters, which is the naming convention for a Python [constant][const].
It indicates that the value is not intended to be changed.

The `translate()` function begins by defining the list which will hold the parsed value(s).

The input is [`split()`][split] into a list of its words, which is then iterated.

[String indexing][string-indexing] is used to check if the first letter of the word is in the set of vowels.
If so, the logical [or][logical-or] operator "short-circuits" and the word plus "ay" is appended to the list.
If the first letter is not a vowel, then a [slice][slicing] of the first two letters is used to check if they match any of the special beginning characters.
If the letters match, the word plus "ay" will be appended to the list.
If the beginning of the word matches either condition, the loop [continue][continue]s to the next word.

If the beginning of the word did not match either condition,
that leaves [ranging][ranging] its characters from position 1 until the [`len()`][len] of the word.

~~~~exercism/note
When a [range](https://docs.python.org/3/library/stdtypes.html?#range) is provided two arguments,
it generates values from the `start` argument up to _but not including_ the `stop` argument.
This behavior can be referred to as start inclusive, stop exclusive.
~~~~

The inner loop iterating characters is nested within the outer loop that iterates the words.
Each character is iterated until finding a vowel (at this point, the letter `y` is now considered a vowel.)
If the vowel is `u`, the previous consonant is checked to be `q`. 
If so, the position is advanced to be one position after the found `u`.

A slice is then taken from the position until the end of the word,
plus a slice taken from the beginning of the word and stopped just before the position, plus `ay`.
That concatenated string is appended to the list, [break][break] is called to exit the inner loop,
and execution returns to the outer loop.

Once all of the words in the input have been iterated,
the [join][join] method is called on a space character to connect all of the words in the list back into a single string.
Since the space is only used as a separator _between_ elements of the list, if the list has only one element,
the space will not be added to the beginning or end of the output string.
 
[set]: https://docs.python.org/3/library/stdtypes.html?#set
[const]: https://realpython.com/python-constants/
[split]: https://docs.python.org/3/library/stdtypes.html?#str.split
[string-indexing]: https://realpython.com/lessons/string-indexing/
[logical-or]: https://realpython.com/python-or-operator/
[continue]: https://docs.python.org/3/reference/simple_stmts.html#the-continue-statement
[ranging]: https://www.w3schools.com/python/gloss_python_for_range.asp
[range]: https://docs.python.org/3/library/stdtypes.html?#range
[len]: https://docs.python.org/3/library/functions.html?#len
[slicing]: https://www.learnbyexample.org/python-string-slicing/
[break]: https://docs.python.org/3/reference/simple_stmts.html#the-break-statement
[join]: https://docs.python.org/3/library/stdtypes.html?#str.join
