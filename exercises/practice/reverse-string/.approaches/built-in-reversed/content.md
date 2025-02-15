# Use the built-in reversed() and Unpack with join()


```python
def reverse(text):
  return (''.join(reversed(text)))
```

This approach calls the built-in `reversed()` function to return a [reverse iterator](https://docs.python.org/3/library/functions.html#reversed) that is then unpacked by `str.join()`.
This is equivalent to using a reverse slice, but incurs a bit of extra overhead due to the unpacking/iteration needed by `str.join()`.
This takes `O(n)` time and `O(n)` space for the reversed copy.


```python
def reverse(text):
    output = ''
    for index in reversed(range(len(text))):
        output += text[index]
    return output
```

This version uses `reversed()` to reverse a `range()` object rather than feed a start/stop/step to `range()` itself.
It then uses the reverse range to iterate over the input string and concatenate each code point to a new 'output' string.
This has over-complicated `reversed()`, as it can be called directly on the input string with almost no overhead.
This has also incurs the performance hit of repeated concatenation to the 'output' string.

While this approach _looks_ as if it would be similar to the first, it is actually `O(n**2)` in time complexity due to string concatenation.
It was also the slowest in benchmarks.


## Timings vs Reverse Slice


As a (very) rough comparison, below is a timing table for these functions vs the canonical reverse slice:

While `reversed()` is very fast, the call to `join()` to unpack slows things down compared to using a reverse slice.
For long strings, this slight overhead starts to become significant.
Using `reversed()` but concatenating to a string is non-performant in this context.


| **string length >>>>** 	|     5    	|    11    	|    22    	|    52    	|    66    	|    86    	|   S142   	|   1420   	|   14200  	|  142000  	|
|------------------------	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
| reverse slice          	| 1.70e-07 	| 1.78e-07 	| 1.89e-07 	| 2.10e-07 	| 2.25e-07 	| 2.40e-07 	| 3.56e-07 	| 1.52e-06 	| 1.22e-05 	| 1.20e-04 	|
| reverse reversed       	| 3.71e-07 	| 4.77e-07 	| 6.78e-07 	| 1.20e-06 	| 1.63e-06 	| 1.01e-06 	| 2.78e-06 	| 2.47e-05 	| 2.44e-04 	| 2.40e-03 	|
| reverse reversed range 	| 6.34e-07 	| 1.05e-06 	| 1.85e-06 	| 3.85e-06 	| 4.73e-06 	| 6.10e-06 	| 9.77e-06 	| 1.44e-04 	| 1.53e-03 	| 1.89e-02 	|


Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
