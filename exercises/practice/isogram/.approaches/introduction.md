# Introduction

There are many idiomatic ways to solve Isogram.
Among them are:
- You can scrub the input with a list comprehension and then compare the `len()` of the scrubbed letters with the `len()` of a `set` of the scrubbed letters.
- You can scrub the input with a couple of calls to `replace()` and then compare the `len()` of the scrubbed letters with the `len()` of a `set` of the scrubbed letters.
- You can scrub the input with a `re.sub()` and then compare the `len()` of the scrubbed letters with the `len()` of a `set` of the scrubbed letters.
- You can filter the input with a `re.findall()` and then compare the `len()` of the scrubbed letters with the `len()` of a `set` of the scrubbed letters.

## General guidance

The key to solving Isogram is to determine if any of the letters in the input are repeated.
A repeated letter means the input is not an isogram.
The letters are "scrubbed" or filtered so that non-alphabetic characters are not considered when determining an isogram.
The occurrence of the letter `a` and the letter `A` count as a repeated letter, so `Alpha` would not be an isogram.

The following four approaches compare the length of the scrubbed letters with the length of a `set`of the scrubbed letters.

## Approach: scrub with a list comprehension

```python
def is_isogram(phrase):
    scrubbed = [ltr.lower() for ltr in phrase if ltr.isalpha()]
    return len(set(scrubbed)) == len(scrubbed)

```

For more information, check the [scrub with list comprehension approach][approach-scrub-comprehension]

## Approach: scrub with `replace()`

```python
def is_isogram(phrase):
    scrubbed = phrase.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))

```

For more information, check the [scrub with `replace()` approach][approach-scrub-replace]

## Approach: scrub with `re.sub()`

```python
import re


def is_isogram(phrase):
    scrubbed = re.compile('[^a-zA-Z]').sub('', phrase).lower()
    return len(set(scrubbed)) == len(scrubbed)

```

For more information, check the [scrub with `re.sub()` approach][approach-scrub-regex]

## Approach: filter with `re.findall()`

```python
import re


def is_isogram(phrase):
    scrubbed = "".join(re.findall("[a-zA-Z]", phrase)).lower()
    return len(set(scrubbed)) == len(scrubbed)

```

For more information, check the [filter with `re.findall()` approach][approach-scrub-regex]

## Other approaches

Besides the aforementioned, idiomatic approaches, you could also approach the exercise as follows:

### Other approach: Bit field

Another approach can use a bit field to keep track of used letters.
For more information, check the [bit field approach][approach-bitfield].

## Which approach to use?

All four `set` approaches are idiomatic.
The `replace` approach is the fastest.

To compare performance of the approaches, check the [Performance article][article-performance].

[approach-scrub-comprehension]: https://exercism.org/tracks/python/exercises/isogram/approaches/scrub-comprehension
[approach-scrub-replace]: https://exercism.org/tracks/python/exercises/isogram/approaches/scrub-replace
[approach-scrub-regex]: https://exercism.org/tracks/python/exercises/isogram/approaches/scrub-regex
[approach-findall-regex]: https://exercism.org/tracks/python/exercises/isogram/approaches/findall-regex
[approach-bitfield]: https://exercism.org/tracks/python/exercises/isogram/approaches/bitfield
[article-performance]: https://exercism.org/tracks/python/exercises/isogram/articles/performance
