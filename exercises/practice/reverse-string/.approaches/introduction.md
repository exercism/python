# Introduction


The goal of the Reverse String exercise is to output a given string in reverse order.
It can be solved in a lot of different ways in Python, with a near-endless amount of variation.

However, not all strategies are efficient, concise, or small in memory.
Care must be taken to not inadvertently slow down the code by using methods that don't scale well.

Additionally, most 'canonical' solutions for reversing a string using the Python standard library do not account for Unicode text beyond the ASCII (0-127) range.


In this introduction, we cover six general approaches and an additional group of 'interesting' takes, but there are many more techniques that could be used.

1.  Sequence Slice with Negative Step
2.  Iteration with String Concatenation
3.  Reverse Iteration with Range()
4.  Make a list and Use str.join()
5.  Make a list and use list.reverse()
6.  Use the built-in reversed()
7.  Other [interesting approaches][approach-additional-approaches]

We encourage you to experiment and get creative with the techniques you use, and see how it changes the way you think about the problem and think about Python.


And while Unicode text is outside the core tests for this exercise (_there are optional tests in the test file you can enable for Unicode_), we encourage you to give reversing strings that have non ASCII text a try.
We talk more about the considerations and strategies for Unicode text reversal (_and third-party libraries that can help_) in the [Working with Unicode Strings][article-working-with-unicode-strings] article.


## Approach: Sequence Slice with a Negative Step

```python
def reverse(text):
  return text[::-1]
```

This is "THE" canonical solution, _provided_ you know what encoding and character sets you are dealing with.
For example, if you know all of your text is **always** going to be within the ASCII space, this is by far the most succinct and performant way to reverse a string in Python.

For more details, see the [sequence slicing approach][approach-sequence-slicing]


## Approach: Iterate over the String; Concatenate to a New String


```python
def reverse(text):
    output = ''
    for codepoint in text:
        output = codepoint + output
    return output
```

This approach iterates over the string, concatenating each codepoint to a new string.
This approach and its variants avoid all use of built-ins such as  `range()`, `reversed()`, and `list.reverse()`.
But for very long strings, this approach can degrade performance toward O(n**2).

For more information and relative performance timings for this group, check out the [iteration and concatenation][approach-iteration-and-concatenation] approach.


## Approach: Use range() to Iterate Backwards over the String, Append to New String


```python
def reverse(text):
    new_word = ""
    
    for index in range(len(text) - 1, -1, -1): #For 'Robot', this is 4 (start) 0 (stop), iterating (4,3,2,1,0)
        new_word += text[index]
    return new_word
```

This method uses the built-in [`range()`][range] object to iterate over text right-to-left, adding each codepoint to the 'new_word' string.
This is essentially the same technique as the approach above, but incurs slightly less overhead by avoiding the potential performance hit of _prepending_ to the 'new_word' string, or creating index or tracking variables.

For very long strings, this approach will still degrade to `O(n**2)` performance, due to the use of string concatenation.
Using `''.join()` here can avoid the concatenation penalty.
For more information and relative performance timings for this group, check out the [backwards iteration with range][approach-backward-iteration-with-range] approach.


## Approach: Create a List and Use str.join() to make new String.


```python
def reverse(text):
    output = []
    
    for codepoint in text:
        output.insert(0,codepoint)
    return "".join(output)
```

This approach either breaks the string up into a list of codepoints to swap or creates an empty list as a "parking place" to insert or append codepoints.
It then iterates over the text, swapping, inserting, or appending each codepoint to the output list.
Finally, `str.join()` is used to re-assemble the `list` into a string.

For more variations and relative performance timings for this group, check out the [list and join][approach-list-and-join] approach.


## Approach: Make the Input Text a List & Use list.reverse() to Reverse in Place


```python
def reverse(text):
	output = list(text)
	output.reverse()
	
	return ''.join(output)
```

This approach turns the string into a list of codepoints and then uses the `list.reverse()` method to re-arrange the list _in place_.
After the reversal of the list, `str.join()` is used to create the reversed string.

For more details, see the [built in list.reverse()][approach-built-in-list-reverse] approach.


## Approach: Use the built-in reversed() Function & join() to Unpack


```python
def reverse(text):
  return (''.join(reversed(text)))
```

This approach calls the built-in `reversed()` function to return a [reverse iterator](https://docs.python.org/3/library/functions.html#reversed) that is then unpacked by `str.join()`.
This is equivalent to using a reverse slice, but incurs a bit of extra overhead due to the unpacking/iteration needed by `str.join()`.

For more details, see the [built-in reversed()][approach-built-in-reversed] approach.


```python
def reverse(text):
    output = ''
    for index in reversed(range(len(text))):
        output += text[index]
    return output
```

This version uses `reversed()` to reverse a `range()` object rather than feed a start/stop/step to `range()` itself.
It then uses the reverse range to iterate over the input string and concatenate each code point to a new 'output' string.
This has over-complicated `reversed()` a bit, as it can be called directly on the input string with almost no overhead.
This has also incurred the performance hit of repeated concatenation to the 'output' string.

## Other Interesting Approaches

These range from using recursion to converting text to bytes before processing.
Some even use `map()` and or a `lambda`

Take a look at the [additional approaches][approach-additional-approaches] 'approach' for more details and timings.


## Which Approach to Use?

The fastest and most canonical by far is the reverse slice.
Unless you are in an interview situation where you need to "show your work", or working with varied Unicode outside the ASCII range, a reverse slice is the easiest and most direct method of reversal.

A reverse slice will also work well for varied Unicode that has been pre-processed to ensure that multibyte characters and combined letters with diacritical and accent marks ('extended graphemes') remain grouped.


For other scenarios, converting the intput text to a `list`, swapping or iterating, and then using `join()` is recommended.

To compare performance of these approach groups, see the [Performance article][article-performance].

[approach-additional-approaches]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/additional-approaches
[approach-backward-iteration-with-range]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/backward-iteration-with-range
[approach-built-in-list-reverse]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/built-in-list-reverse
[approach-built-in-reversed]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/built-in-reversed
[approach-iteration-and-concatenation]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/iteration-and-concatenation
[approach-list-and-join]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/list-and-join
[approach-sequence-slicing]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/sequence-slicing
[article-performance]: https://exercism.org/tracks/python/exercises/reverse-string/articles/performance
[article-working-with-unicode-strings]: https://exercism.org/tracks/python/exercises/reverse-string/.articles/working-with-unicode-strings
[range]: https://docs.python.org/3/library/stdtypes.html#range
