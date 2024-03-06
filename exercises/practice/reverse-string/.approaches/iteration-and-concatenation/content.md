# Iteration and Concatenation


```python
def reverse(text):
    output = ''
    for codepoint in text:
        output = codepoint + output
    return output
```

The variations here all iterate over the string, concatenating each codepoint to a new string.
While this avoids all use of built-ins such as `range()`, `reversed()`, and `list.reverse()`, it incurs both a memory and speed penalty over using a reverse slice.

Strings are immutable in Python.
Using concatenation via `+` or `+=` forces the re-creation of the 'output' string for _every codepoint added from the input string._
That means the code has a minimum time complexity of `O(m + n)`, where `n` is the length of the text being iterated over, and `m` is the number of concatenations to the 'output' string.
For some more detail on `O(n + m)` vs `O(n)`, see this [Stack Overflow post][time-complexity-omn-vs-on].
The code also uses `O(n)` space to store 'output'.

As input strings grow longer, concatenation can become even more problematic, and performance can degrade to `O(n**2)`, as longer and longer shifts and reallocations occur in memory.
In fact, the "standard" way to describe the time complexity of this code is to say that is O(n**2), or quadratic.

Interestingly, CPython includes an optimization that attempts to avoid the worst of the shift and reallocation behavior by reusing memory when it detects that a string append is happening.
Because the code above _prepends_ the codepoint to the left-hand side of 'output', this optimization cannot be used.
Even in cases where strings are appended to, this optimization cannot be relied upon to be stable and is not transferable to other implementations of Python.

For some interesting reading on this topic, see these Stack Overflow posts:
-  [Time Complexity of String Concatenation in Python][time-complexity-of-string-concatenation-in-python],
-  [Time Complexity of Iterative String Append][time-complexity-of-iterative-string-append],
-  [Most efficient String Concatenation Method in Python][most-efficient-string-concatenation-method-in-Python],
-  [join() is faster than +, but what is wrong here?][join() is faster than +, but what is wrong here?], and
-  [Is += bad practice in Python?][is += bad practice in Python?]

To see the difference between reverse slicing and looping in terms of steps, check out [slicing verses iterating+concatenation][python-tutor] at the PythonTutor site.


## Variation #1: Using a While Loop and a Negative Index


```python
def reverse(text):
    output = '' 
    index = -1
   
    while index >= -len(text):
        output += text[index]
        index -= 1
    return output
```

This solution uses a while loop to "count down" the length of the string using a negative index.
Each number is used to index into the input string and concatenate the resulting codepoint to a new string.
Because each index is further from zero than the last, this has the effect of "iterating backward" over the input string.

This approach incurs additional overhead for length checking the input string repeatedly in the loop, and setting/decrementing the index variable, both of which can be avoided by using the built-in `range()` object.
Overall, this was the slowest of the three variations when timed.


## Variation #2: Using a While Loop with a Positive Index


```python
def reverse(text):
    result =''
    index = len(text)-1
    
    while index >= 0:
        result += text[index]
        index -= 1
    return result
```

This solution uses a while loop to "count down" the length of the string until it reaches zero using a positive index.
Each number is used to index into the input string and concatenate the resulting codepoint to a new string.
Because each index is closer to zero than the last, this has the effect of also "iterating backward" over the input string.
Algorithmically, this takes as much tine and space as the code samples above, since it uses an intermediate string for the reversal and must loop through every codepoint in the input.


## Timings vs Reverse Slice


As seen in the table below, all of these approaches are slower than using a reverse slice.
Interestingly, iteration + prepending to the string is fastest in this group for strings under length 1420.
But keep in mind that in general, string concatenation and prepending should be avoided for any 'industrial strength' use cases.


| **string length >>>>** 	| 5        	| 11       	| 22       	| 52       	| 66       	| 86       	| 142      	| 1420     	| 14200    	| 142000   	|
|------------------------	|----------	|----------	|----------	|----------	|----------	|----------	|----------	|----------	|----------	|----------	|
| reverse slice          	| 1.66e-07 	| 1.73e-07 	| 1.88e-07 	| 1.12e-07 	| 2.15e-07 	| 2.32e-07 	| 3.46e-07 	| 1.42e-06 	| 1.18e-05 	| 1.15e-04 	|
| reverse string prepend 	| 4.28e-07 	| 8.05e-07 	| 1.52e-06 	| 3.45e-06 	| 4.82e-06 	| 5.55e-06 	| 9.83e-06 	| 2.23e-04 	| 2.96e-03 	| 5.17e-01 	|
| reverse positive index 	| 4.65e-07 	| 8.85e-07 	| 1.73e-06 	| 3.70e-06 	| 4.83e-06 	| 6.55e-06 	| 1.01e-05 	| 1.54e-04 	| 1.60e-03 	| 2.61e-02 	|
| reverse negative index 	| 5.65e-07 	| 1.32e-06 	| 2.61e-06 	| 5.91e-06 	| 7.62e-06 	| 4.00e-06 	| 1.62e-05 	| 2.16e-04 	| 2.19e-03 	| 2.48e-02 	|


Measurements were taken on a  3.1 GHz Quad-Core Intel Core i7 Mac running MacOS Ventura.
Tests used `timeit.Timer.autorange()`, repeated 3 times.
Time is reported in seconds taken per string after calculating the 'best of' time.
The [`timeit`][timeit] module docs have more details, and [note.nkmk.me][note_nkmk_me] has a nice summary of methods.

[python-tutor]: https://pythontutor.com/render.html#code=def%20reverse_loop%28text%29%3A%0A%20%20%20%20output%20%3D%20''%0A%20%20%20%20for%20letter%20in%20text%3A%0A%20%20%20%20%20%20%20%20output%20%3D%20letter%20%2B%20output%0A%20%20%20%20return%20output%0A%20%20%20%20%0Adef%20reverse_slice%28text%29%3A%0A%20%20%20%20return%20text%5B%3A%3A-1%5D%0A%20%20%20%20%0A%0Aprint%28reverse_loop%28'Robot'%29%29%0Aprint%28reverse_slice%28'Robot'%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

[is += bad practice in Python?]: https://stackoverflow.com/questions/39675898/is-python-string-concatenation-bad-practice
[join() is faster than +, but what is wrong here?]: https://stackoverflow.com/a/1350289
[most-efficient-string-concatenation-method-in-Python]: https://stackoverflow.com/questions/1316887/what-is-the-most-efficient-string-concatenation-method-in-python
[note_nkmk_me]: https://note.nkmk.me/en/python-timeit-measure/
[time-complexity-of-iterative-string-append]: https://stackoverflow.com/questions/34008010/is-the-time-complexity-of-iterative-string-append-actually-on2-or-on
[time-complexity-of-string-concatenation-in-python]: https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python
[time-complexity-omn-vs-on]: https://cs.stackexchange.com/questions/139307/time-complexity-omn-vs-on
[timeit]: https://docs.python.org/3/library/timeit.html#python-interface
