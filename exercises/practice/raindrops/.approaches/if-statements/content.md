# `if` Statements

```python
def convert(num):
    sounds = ''
    
    if num % 3 == 0: sounds += 'Pling'
    if num % 5 == 0: sounds += 'Plang'
    if num % 7 == 0: sounds += 'Plong'
        
    return sounds or str(num)
```


This approach is the most straightforward or 'naive' - it replicates in code what the instructions say, using `if` statements to check the modulo for each factor.
If the number is evenly divisible by the factor (modulo == 0), the corresponding string is concatenated to  _sounds_ via the `+` operator.
Sounds is returned if it is not empty (_see [Truth Value Testing][truth-value-testing] for more info_).
Otherwise, a `str` version of the input number is returned.

This, of course incurs the 'penalty' of string concatenation.
But since there are only three factors to check and the strings are small, the concatenation is at a minimum.

In fact, this solution - and most others described in the approaches here - are `O(1)` time complexity.
There are a constant number of factors to iterate through, and the work that is done never increases, even as the input numbers get bigger.
This holds true for space complexity as well.

The compact form for the `if` statements might be harder to read for some people.
These can be re-written to be nested, and the return can be re-written to use a ternary expression:

```python
def convert(num):
    sounds = ''
    
    if num % 3 == 0: 
        sounds += 'Pling'
    if num % 5 == 0: 
        sounds += 'Plang'
    if num % 7 == 0: 
        sounds += 'Plong'
        
    return sounds if sounds else str(num)
```

While this solution is nicely readable and to-the-point, it will grow in length and get harder to read if many more factors are added or business logic changes.
Other solutions using data structures to hold factors might be a better option in 'high change' situations.

[truth-value-testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
