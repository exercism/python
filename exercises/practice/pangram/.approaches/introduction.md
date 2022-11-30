# Introduction

There are various idomatic approaches to Pangram.
You can use the `all()` method on the `ascii_lowercase` letters with the lowercased letters of the `sentence`.
You can see if the `set` of the alphabet `issubset()` of a `set` of the lowercased `sentence`.
Or you can see if the `set` `len()` of the lowercased `sentence` filtered to just ASCII letters is `26`.

## General guidance

The key to solving Pangram is determining if all of the letters in the alphabet are in the `sentence` being tested.
The occurrence of either the letter `a` or the letter `A` would count as the same letter.

## Approach: `all()` on lowercased letters

```python
from string import ascii_lowercase


def is_pangram(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)

```

For more information, check the [`all()` approach][approach-all].

## Approach: `set` with `issubset()` on lowercased characters

```python
from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_pangram(sentence):
    return ALPHABET.issubset(sentence.lower())

```

For more information, check the [`set` with `issubset()` approach][approach-set-issubset].

## Approach: `set` with `len()` on lowercased characters

```python
def is_pangram(sentence):
    return len([ltr for ltr in set(sentence.lower()) if ltr.isalpha()]) \
        == 26

```

For more information, check the [`set` with `len()` approach][approach-set-len].

## Other approaches

Besides the aforementioned, idiomatic approaches, you could also approach the exercise as follows:

### Other approach: Bit field

Another approach can use a bit field to keep track of used letters.
For more information, check the [bit field approach][approach-bitfield].

## Which approach to use?

The fastest is the `set` `issubset()` approach.

To compare performance of the approaches, check the [Performance article][article-performance].

[approach-all]: https://exercism.org/tracks/python/exercises/pangram/approaches/all
[approach-set-issubset]: https://exercism.org/tracks/python/exercises/pangram/approaches/set-issubset
[approach-set-len]: https://exercism.org/tracks/python/exercises/pangram/approaches/set-len
[approach-bitfield]: https://exercism.org/tracks/python/exercises/pangram/approaches/bitfield
[article-performance]: https://exercism.org/tracks/python/exercises/pangram/articles/performance
