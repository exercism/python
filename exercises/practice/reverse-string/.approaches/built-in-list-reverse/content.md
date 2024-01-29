# Make the Input Text a List and Use list.reverse() to Reverse In-Place


```python
def reverse(text):
	output = list(text)
	output.reverse()
	
	return ''.join(output)
```

These approaches start with turning the text into a `list` of codepoints.
Rather than use a loop + append to then reverse the text, the [`list.reverse()`][list-reverse-method] method is used to perform an in-place reversal.
`join()` is then used to turn the list into a string.

This takes `O(n)` time complexity because `list.reverse()` & `join()` iterate through the entire `list`.
It uses `O(n)` space for the output `list`.

`list.reverse()` cannot be fed to `join()` here because it returns `None` as opposed to returning the `list`.
Because `list.reverse()` **mutates the list**, it is not advisable in situations where you want to preserve the original `list` of codepoints.


## Variation #1:  Keep a Copy of the Original Ordering of Codepoints


```python
def reverse(text):
    codepoints, output = list(text), list(text)
    output.reverse()
    return ''.join(output)
```

This variation is essentially the same as the solution above, but makes a codepoints list to keep the original codepoint ordering of the input text.
This does add some time and space overhead.


## Variation #2:  Iterate Through the String and Append to Create List Before Reversing


```python
def reverse(text):
    output = []
    
    for item in text:
        output.append(item)
        
   output.reverse()
    
    return ''.join(output)
```

This variation declares output as an empty literal, then loops through the codepoints of the input text and appends them to output.
`list.reverse()` is then called to reverse output in place.
 Finally, output is joined into a string via `str.join()`.
Using this method is the same as calling the `list` constructor directly on the input text (_`list(text)`_), which will iterate through it automatically.
 Calling the constructor is also quite  a bit faster than  using a "written out" `for-loop`.


## Timings vs Reverse Slice


As a (very) rough comparison, below is a timing table for these functions vs the canonical reverse slice:

As you can see, using `list.reverse()` after converting the input text to a list is much slower than using a reverse slice.
Iterating in a loop to create the output list also adds even more time.


| **string lengths >>>>** 	|     5    	|    11    	|    22    	|    52    	|    66    	|    86    	|    142   	|   1420   	|   14200  	|  142000  	|
|-------------------------	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
| reverse slice           	| 1.70e-07 	| 1.74e-07 	| 1.00e-07 	| 2.06e-07 	| 2.20e-07 	| 2.39e-07 	| 3.59e-07 	| 1.47e-06 	| 1.22e-05 	| 1.20e-04 	|
| reverse reverse method  	| 3.28e-07 	| 2.00e-07 	| 5.39e-07 	| 8.96e-07 	| 1.35e-06 	| 1.55e-06 	| 2.31e-06 	| 2.01e-05 	| 1.93e-04 	| 1.94e-03 	|
| reverse iterate list    	| 4.74e-07 	| 7.60e-07 	| 1.25e-06 	| 2.75e-06 	| 3.53e-06 	| 4.52e-06 	| 7.22e-06 	| 6.07e-05 	| 5.84e-04 	| 6.28e-03 	|


Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.


[list-reverse-method]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
