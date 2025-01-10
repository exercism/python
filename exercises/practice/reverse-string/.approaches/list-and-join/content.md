# Create a List and Use str.join() to Make A New String


To avoid performance issues with concatenating to a string, this group of approaches uses one or more `list`s to perform swaps or reversals before joining the codepoints back into a string.
This avoids the `O(n**2)` danger of repeated shifting/reallocation when concatenating long strings.
However, the use of `join()` and other techniques still make all of these solutions `O(n)` - `O(n+m)` in time complexity.


```python
def reverse(text):
    output = []
    
    for codepoint in text:
        output.insert(0,codepoint)
    return "".join(output)
```

The code above iterates over the codepoints in the input text and uses `list.insert()` to insert each one into the output list.
Note that `list.insert(0, codepoint)` _prepends_, which is very inefficient for `lists`, while appending takes place in (amortized) O(1) time.
So this code incurs a time penalty because it forces repeated shifts of every element in the list with every insertion.
A small re-write using `range()` to change the iteration direction will boost performance:


## Variation #1:  Use Range to Iterate Over the String Backward and list.append() to Output


```python
def reverse(text):
    output = []
    length = len(text)-1
    
    for index in range(length, -1, -1):
        output.append(text[index])
    return "".join(output)
```

This code iterates backward over the string using `range()`, and can therefore use `list.append()` to append to the output list in (amortized) constant time.
However, the use of `join()` to unpack the list and create a string still makes this `O(n)`.
This also takes `O(n)` space for the output `list`.


## Variation #2:  Convert Text to List and Use range() to Iterate over 1/2 the String, Swapping Values


```python
def reverse(text):
    output = list(text)
    length = len(text) // 2  #Cut the amount of iteration in half
    
    for index in range(length): 
        
        #Swap values at given indexes
        output[index], output[length - index - 1] = output[length - index - 1], output[index]
    return ''.join(output)
```


This variation calculates a median which is then used with `range()` in a `for loop` to iterate over _half_ the indexes in the 'output' list, swapping values into their reversed places.
`str.join()` is then used to create a new string.
This technique is quite speedy, and re-arranges the list of codepoints 'in place', avoiding expensive string concatenation.
It is still `O(n)` time complexity because `list()` and `join()` each force iteration over the entire length of the input string.


## Variation #3: Convert Text to List, Use Start and End Variables to Iterate and Swap Values


```python
def reverse(text):
    output = list(text)
    start = 0
    end = len(text) - 1
   
    while start < end:
        #Swap values in output until the indexes meet at the 'center'
        output[start], output[end] = output[end], output[start] 
        start += 1
        end -= 1
    return "".join(output)
```


This variation 'automatically' finds the midpoint by incrementing and decrementing 'start' and 'end' variables.
Otherwise, it is identical to variation 2.


## Variation #4:  Convert Text to Bytearray, Iterate and Swap


```python
def reverse(text):
    output = bytearray(text.encode("utf-8"))
    length = len(output)
    
    for index in range(length//2):
        output[index], output[length-1-index] = output[length-1-index], output[index]
    return output.decode("utf-8")
```


This variation is operationally the same as variations #2 & #3 above, except that it encodes the string to a `utf-8` [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray).
 It then iterates over the bytearray to perform the swaps.
Finally, the bytearray is decoded into a `utf-8` string to return the reversed word.
This incurs overhead when encoding/decoding to and from the `bytearray`.
This also throws an ` UnicodeDecodeError: invalid start byte` when working with any multi-byte codepoints because no check was conducted to keep multibyte codepoints grouped together during the reversal.

Because of this issue, no timings are available for this variation.
For code that keeps bytes together correctly, see the bytearray variation in the [additional approaches][approach-additional-approaches] approach.


## Variation #5:  Use Generator Expression with Join to Iterate Backwards Over Codepoints List

```python
def reverse(text):
    codepoints = list(text)
    length = len(text) - 1
    return "".join(codepoints[index] for index in range(length, -1, -1)) 
```

This variation puts the for/while loop used in other strategies directly into `join()` using a generator expression.
The text is first converted to a list and the generator-expression "swaps" the codepoints over the whole `list`, using `range()` for the indexes.
Interestingly, because of the work to create and manage the generator, this variation is actually _slower_ than using an auxiliary `list` and `loop` to manage codepoints and then calling `join()` separately.


## Timings vs Reverse Slice


As a (very) rough comparison, below is a timing table for these functions vs the canonical reverse slice:


| **string lengths >>>>** 	|     5    	|    11    	|    22    	|    52    	|    66    	|    86    	|    142   	|   1420   	|   14200  	|  142000  	|
|-------------------------	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
| reverse slice           	| 1.67e-07 	| 1.76e-07 	| 1.85e-07 	| 2.03e-07 	| 2.12e-07 	| 2.32e-07 	| 3.52e-07 	| 1.47e-06 	| 1.20e-05 	| 1.17e-04 	|
| reverse auto half swap  	| 4.59e-07 	| 7.53e-07 	| 1.16e-06 	| 2.25e-06 	| 3.08e-06 	| 3.80e-06 	| 5.97e-06 	| 7.08e-05 	| 7.21e-04 	| 7.18e-03 	|
| reverse half swap       	| 6.34e-07 	| 9.24e-07 	| 1.51e-06 	| 2.91e-06 	| 3.71e-06 	| 4.53e-06 	| 7.52e-06 	| 2.52e-04 	| 1.01e-03 	| 1.05e-02 	|
| reverse append          	| 6.44e-07 	| 1.00e-06 	| 1.56e-06 	| 3.28e-06 	| 4.48e-06 	| 5.54e-06 	| 8.89e-06 	| 2.20e-04 	| 8.73e-04 	| 9.10e-03 	|
| reverse generator join  	| 1.02e-06 	| 1.39e-06 	| 2.16e-06 	| 4.13e-06 	| 5.31e-06 	| 6.79e-06 	| 1.11e-05 	| 1.07e-04 	| 1.07e-03 	| 1.05e-02 	|
| reverse insert          	| 5.29e-07 	| 9.10e-07 	| 1.64e-06 	| 3.77e-06 	| 4.90e-06 	| 6.86e-06 	| 1.14e-05 	| 2.70e-04 	| 2.35e-02 	| 2.74e+00 	|



Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
[approach-additional-approaches]: https://exercism.org/tracks/python/exercises/reverse-string/.approaches/additional-approaches
