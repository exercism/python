## Backward Iteration with Range


```python
def reverse(text):
    output = ""
    for index in range(len(text) - 1, -1, -1): #For 'Robot', this is 4 (start) 0 (stop), iterating (4,3,2,1,0)
        output += text[index]
    return output
```


These variations all use the built-in [`range()`][range] object to iterate over the input text from right --> left, adding each codepoint to the output string.
This is the same as iterating over the text backward using one or more `index` variables, but incurs slightly less overhead by substituting `range()` for them.
Note that the code above also avoids _prepending_ to the output string.

For very long strings, this code will still degrade to `O(n**2)` performance, due to the use of string concatenation.
Using `''.join()` here can avoid heavy concatenation penalty as strings grow longer and the CPython string append optimization mentioned in the [iteration and concatenation][approach-iteration-and-concatenation] approach breaks down.


##  Variation #1: Forward Iteration in Range, Negative Index


```python
def reverse(text):
    output = ''

    for index in range(1, len(text) + 1):
        output += text[-index]
    return output  
```


This version iterates left --> right using a positive `range()` and then _prepends to the string_ by using a negative index for the codepoint.
This has the same faults as variation #1, with the added cost of prepending via concatenation.


## Variation #2:  Feed Range and the Index into Join()

```python
def reverse(text):
    return "".join(text[index] for index in range(len(text)-1, -1, -1)) 
 ```

 This version omits the intermediary output string, and uses `"".join()` directly in the return.
 Within the `join()` call, `range()` is used with a negative step to iterate over the input text backward.

 This strategy avoids the penalties of string concatenation with an intermediary string.
 It is still `O(n)` in time complexity, and is slower than reverse indexing due to the calls to `join()`, `len()` and `range()`, and the creation of the generator expression.

 Because of the aforementioned string append optimization in CPython, this approach will benchmark slower for strings under length 1000, but becomes more and more efficient as the length of the string grows.
 Since the CPython optimization is not stable nor transferable to other versions of Python, using `join()` by default is recommended in any situation where the string concatenation is not strictly repetition and length constrained.


## Timings vs Reverse Slice


 As a (very) rough comparison, below is a timing table for these functions vs the canonical reverse slice:



| **string length >>>>** 	|     5    	|    11    	|    22    	|    52    	|    66    	|    86    	|    142   	|   1420   	|   14200  	|  142000  	|
|------------------------	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
| reverse slice          	| 1.68e-07 	| 1.74e-07 	| 1.83e-07 	| 2.07e-07 	| 2.14e-07 	| 2.29e-07 	| 3.51e-07 	| 1.50e-06 	| 1.19e-05 	| 1.17e-04 	|
| reverse negative range 	| 5.89e-07 	| 9.93e-07 	| 1.78e-06 	| 3.69e-06 	| 4.71e-06 	| 5.83e-06 	| 9.61e-06 	| 1.39e-04 	| 1.46e-03 	| 1.81e-02 	|
| reverse positive range 	| 6.20e-07 	| 1.14e-06 	| 2.23e-06 	| 4.54e-06 	| 5.74e-06 	| 7.38e-06 	| 1.20e-05 	| 1.70e-04 	| 1.75e-03 	| 2.07e-02 	|
| reverse range and join 	| 8.90e-07 	| 1.31e-06 	| 2.14e-06 	| 4.15e-06 	| 5.22e-06 	| 6.57e-06 	| 1.06e-05 	| 1.05e-04 	| 1.04e-03 	| 1.07e-02 	|


Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[approach-iteration-and-concatenation]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/iteration-and-concatenation
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[range]: https://docs.python.org/3/library/stdtypes.html#range
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
