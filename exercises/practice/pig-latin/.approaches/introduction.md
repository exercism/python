# Introduction

There are various ways to solve Pig Latin.
One way is to use [regular expressions][regex] (also known as [regex][regex-ops]) for processing the input.
Solutions using regex can be very succinct, but require familiarity with regex patterns, which are like another language.
Another way is to use a series of conditional statements to test which of several rules the input matches.
Another approach is to use [set][set]s for look-up and then [slice][slicing] the input to return the correct value.

## General guidance

At the time of writing only four rules need to be handled, but if they have similar output, they don't need to be handled completely separately.

## Approach: Sets and slices

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

For more information, check the [sets and slices approach][approach-sets-and-slices].

[regex]: https://docs.python.org/3/howto/regex.html#regex-howto
[regex-ops]: https://docs.python.org/3/library/re.html?regex
[set]: https://docs.python.org/3/library/stdtypes.html?#set
[slicing]: https://www.learnbyexample.org/python-string-slicing/
[approach-sets-and-slices]: https://exercism.org/tracks/python/exercises/pig-latin/approaches/sets-and-slices
