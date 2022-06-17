# Introduction

Python has two looping constructs.
`while` loops for _indefinite_ (uncounted) iteration and `for` loops for  _definite_, (counted) iteration.
The keywords `break`, `continue`, and `else` help customize loop behavior.
The `range(<length of sequence>)` and `enumerate(<iterable>)` functions help with loop counting and indexing.


`while` loops do not have a number of loops to execute specified, and will continue as long as the `loop` expression or "test" evaluates to `True`.
The loop will terminate when the loop expression evaluates to `False`.

```python
while expression:
    set_of_statements
```

`for` loops cycle through the values of any sequence, terminating when there are no more values returned.
The `range(<length of sequence>)` function provides a `loop` counter or sequence when there is no data structure or other iterable to loop over.

```python
# Python will keep track of the loop count internally.
for item in sequence:
    set_of_statements
    
# `range()` is used as an explicit loop counter.  
# This will loop 12 times, from index 0 to index 11.
for item in range(12):
    set_of_statements
```


