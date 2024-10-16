# Sequence Slice with Negative Step


```python
def reverse(text):
  return text[::-1]
```

This approach uses Python's negative indexes and _[sequence slices][sequence slicing]_ to iterate over the string in reverse order, returning a reversed copy.


<table>
<tr>
  <td style="vertical-align: top"> index from left ⟹<br><br><br><br><br><br><br></td><td style="vertical-align: middle">

|  0<br>👇🏾 	|  1<br>👇🏾 	|  2<br>👇🏾 	|  3<br>👇🏾 	|  4<br>👇🏾 	|  5<br>👇🏾 	|
|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|:--------:	|
|     P    	|     y    	|     t    	|     h    	|     o    	|     n    	|
| 👆🏾<br>-6 	| 👆🏾<br>-5 	| 👆🏾<br>-4 	| 👆🏾<br>-3 	| 👆🏾<br>-2 	| 👆🏾<br>-1 	|
</td><td style="vertical-align: bottom"><br><br><br><br><br>⟸ index from right</td>
</tr>
</table>

Slices use **`[<start> : <stop> : <step>]`** syntax.
The space before the first `:` indicates which index to start iterating from (_inclusive_), the space before the second `:` indicates which index to stop before (_exclusive_), and the final space after the second `:` indicates the direction of iteration and size of the 'step'.
  A positive step moves left --> right and a negative step moves right --> left.
   If start/stop indexes are omitted, Python assumes 'start of string' and 'end of string'.
Omitting the step defaults to a step of +1, but any size step can be used.
Slices return a _copy_ of the original object.
This same syntax works on `strings`, `bytearray`, `lists`, `tuples`, and `ranges`, which are all sequence types.


Reverse slicing has `O(n)` time complexity - the amount of time/work scales directly with the length of the string being iterated through and reversed.
And since slicing returns copy, the space for the copy also scales with the size of the input.

Using a slice on a string is roughly equivalent to looping over the string from the right-hand side, appending each codepoint to a new string.
However, the code below takes `O(n + n)` best case and `O(n**2)` worst case due to the operations needed for string concatenation.


```python
def reverse(text):
  output = ''
  for index in range(-1, -(len(text)+1), -1):
    output += text[index] 
  return output
```

[sequence slicing]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
