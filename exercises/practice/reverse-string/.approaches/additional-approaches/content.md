# Additional Approaches that are Further Afield

Below are some interesting strategies that are distinct from the canonical approaches that have already been discussed.
While they do not offer particular performance boosts over the canonical approaches (_and some offer very large penalties_), they do explore interesting corners of Python.


## Convert the Input to a UTF-8 bytearray and use a Sliding Window to Reverse


```python
def reverse(text):

    # Create bytearrays for input and output.
    given, output = bytearray(text.encode("utf-8")), bytearray(len(text))
    index = 0
    LENGTH_MASK = 0xE0  # this is 0b11110000 (binary) or 224 (decimal)
    
    # Loop through the input bytearray.
    while index < len(given):
    
        #Either the len is 1 or it is calculated by counting the bits after masking.
        seq_len = (not(given[index] >> 7) or
                  (given[index] & LENGTH_MASK).bit_count())
        
        #Calculate the index start.
        location = index + seq_len +1

        #Prepend the byte segment to the output bytearray
        output[-location:-index or None] = given[index:index + seq_len]

        #Increment the index count or slide the 'window'.
        index += seq_len
    
    #Decode output to UTF-8 string and return.    
    return output.decode("utf-8")
  
```

This strategy encodes the string into a UTF-8 [`bytearray`][bytearray].
It then uses a `while` loop to iterate through the text, calculating the length of a sequence (or 'window') to slice from 'given' and prepend to 'output'.
 The 'index' counter is then incremented by the length of the 'window'.
 Once the 'index' is greater than the length of 'given', the 'output' bytearray is decoded into a UTF-8 string and returned.
 This is (_almost_) the same set of operations as described in the code below, but operating on bytes in a bytearray, as opposed to text/codepoints in a `list` - although this strategy does not use `list.pop()` (_bytearray objects do not have a pop method_).

 This uses `O(n)` space for the output array.
It incurs additional runtime overhead by _prepending_ to the output array, which is an expensive operation that forces many repeated shifts.
Encoding to bytes and decoding to codepoints further slow this approach.


## Convert the Input to a list and use a While Loop to Pop and Append to a Second List


```python
def reverse(text):
    codepoints, stniopedoc = list(text), []
    
    while codepoints:
        stniopedoc.append(codepoints.pop())
        
    return ''.join(stniopedoc)
```

This strategy uses two lists.
One `list` for the codepoints in the text, and one to hold the codepoints in reverse order.
First, the input text is turned into a the 'codepoints' `list`, and iterated over.
Each codepoint is `pop()`ped from 'codepoints' and appended to the 'stniopedoc' `list`.
Finally, 'stniopedoc' is joined via `str.join()` to create the reversed string.

While this is a straightforward and readable approach, it creates both memory and performance overhead, due to the creation of the lists and the use of `join()`.
This is much faster than the bytearray strategy or using string concatenation, but is still almost  slower than the slicing strategy.
It also takes up `O(n)` auxiliary space with the stniopedoc list.



## Using Recursion Instead of a Loop


```python
def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]
```

This strategy uses a slice to copy all but the leftmost part of the string, concatenating the codepoint at the first index to the end.
The function then calls itself with the (now shorter) text slice.
This slice + concatenation process continues until the `len()` is 0, and the reversed text is returned up the call stack.
This is the same as iterating over the string backward in a `loop`, appending each codepoint to a new string, and has identical time complexity.
It also uses O(n) space, with the space being successive calls on the call stack.

Because each recursive call is placed on the stack and Python limits recursive calls to a max of 1000, this code produces a `maximum recursion depth exceeded` error for any string longer than ~999 characters.


## Using `map()` and `lambbda` with `Join()` Instead of a Loop

```python
def reverse(text):
    return "".join(list(map(lambda x: text[(-x-1)], range(len(text)))))
```

This variation uses the built-in `map()` and a `lambda` to iterate over the string backward, constructing a `list`.
The `list` is then fed to `str.join()`, which unpacks it and turns it into a string.
This is a very non-performant way to walk the string backwards, and also incurs extra overhead due to the unneeded construction of an intermediary `list`.

`map()` can instead be directly fed to `join()`, which improves performance to `O(n)`:

```python
def reverse(text):
    return "".join(map(lambda x: text[(-x-1)], range(len(text))))
```


## Using a `lambda` that returns a Reverse Sequence Slice


```python
reverse = lambda text: text[::-1]
```


This strategy assigns the name "reverse" to a `lambda` that produces a reverse slice of the string.
This looks quite clever and is shorter than a "traditional" function, but it is far from obvious that this line defines a callable named "reverse" that returns a reversed string.
While this code compiles to the same function definition as the first approach article, it is not clear to many programmers who might read through this code that they could call `reverse('some_string')` the way they could call other functions.


This has the added disadvantage of creating troubleshooting issues since any errors will be attributed to `lambda` in the stack trace and not associated with an explicit function named `reverse`.
Help calls and `__repr__` calls are similarly affected.
This is not the intended use of `lambdas` (_which are for unnamed or anonymous functions_), nor does it confer any sort of performance boost over other methods, but _does_ create readability issues with anyone unfamiliar with `lambda` syntax and compilation.


## Timings vs Reverse Slice


As a (very) rough comparison, below is a timing table for these functions vs the canonical reverse slice:


| **string lengths >>>>** 	| Str Len: 5 	| Str Len: 11 	| Str Len: 22 	| Str Len: 52 	| Str Len: 68 	| Str Len: 86 	| Str Len: 142 	| Str Len: 1420 	| Str Len: 14200 	| Str Len: 142000 	|
|-------------------------	|------------	|-------------	|-------------	|-------------	|-------------	|-------------	|--------------	|---------------	|----------------	|-----------------	|
| reverse slice           	| 1.66e-07   	| 1.75e-07    	| 1.79e-07    	| 2.03e-07    	| 2.22e-07    	| 2.38e-07    	| 3.63e-07     	| 1.44e-06      	| 1.17e-05       	| 1.16e-04        	|
| reverse lambda          	| 1.68e-07   	| 1.72e-07    	| 1.85e-07    	| 2.03e-07    	| 2.44e-07    	| 2.35e-07    	| 3.65e-07     	| 1.47e-06      	| 1.25e-05       	| 1.18e-04        	|
| reverse dual lists      	| 9.17e-07   	| 1.56e-06    	| 2.70e-06    	| 5.69e-06    	| 8.30e-06    	| 1.07e-05    	| 1.80e-05     	| 1.48e-04      	| 1.50e-03       	| 1.53e-02        	|
| reverse recursive       	| 8.74e-07   	| 1.90e-06    	| 4.02e-06    	| 8.97e-06    	| 1.24e-05    	| 1.47e-05    	| 3.34e-05     	| ---           	| ---            	| ---             	|
| reverse bytes           	| 1.92e-06   	| 3.82e-06    	| 7.36e-06    	| 1.65e-05    	| 2.17e-05    	| 2.71e-05    	| 4.47e-05     	| 5.17e-04      	| 6.10e-03       	| 2.16e-01        	|


As you can see, the reverse using two lists and the reverse using a bytearray are orders of magnitude slower than using a reverse slice.
For the largest inputs measured, the dual list solution was almost 55x slower, and the bytearray solution was almost 1800x slower.
Timings for strings over 142 characters could not be run for the recursive strategy, due to Python's 1000 call recursion limit.


Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[bytearray]: https://docs.python.org/3/library/stdtypes.html#bytearray
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
