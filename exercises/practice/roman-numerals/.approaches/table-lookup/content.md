# Table Lookup

```python
def roman(number):
    # define lookup table (as a tuple of tuples, in this case)
    table = (
        ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
        ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
        ('C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
        ('M', 'MM', 'MMM'))

    # convert the input integer to a list of single digits
    digits = [int(digit) for digit in str(number)]
    
    # get the row in the lookup table for the most-significant decimal digit
    inverter = len(digits) - 1

    # translate decimal digits list to Roman numerals list
    roman_digits = [table[inverter - idx][digit - 1] for idx, digit in enumerate(digits) if digit != 0]

    # convert the list of Roman numerals to a single string
    return ''.join(roman_digits)
```

In this approach we loop over decimal digits (using a [list comprehension][list-comprehension]), not their Roman equivalents.

The key point is to have a 2-dimensional lookup table, with each row corresponding to a separate digit: ones, tens, hundreds, or thousands.
Each digit can then be converted to its Roman equivalent with a single lookup.

Note that we need to compensate for Python's zero-based indexing by (in effect) subtracting 1 from each row and column.

## Variation #1

In the code above, we used the `inverter` variable to work bottom-to-top through the lookup table.
This allows working left-to-right through the decimal digits.

Alternatively, we could reverse the `digits` list, go top-to-bottom through the lookup table, then reverse the `roman_digits` list before the final [`join()`][str-join].

```python
def roman(number):
    # define lookup table (as a tuple of tuples, in this case)
    table = (
        ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
        ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
        ('C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
        ('M', 'MM', 'MMM'))

    # convert the input integer to a list of single digits, in reverse order
    digits = [int(digit) for digit in str(number)][::-1]

    # translate decimal digits list to Roman numerals list
    roman_digits = [table[idx][digit - 1] for idx, digit in enumerate(digits) if digit != 0]

    # reverse the list of Roman numerals and convert to a single string
    return ''.join(roman_digits[::-1])
```

This eliminates one line of code, at the cost of adding two list reverses.

The `[::-1]` indexing is idiomatic Python, but less experienced programmers may not find it very readable.

## Credit

This approach was adapted from one created by @cmcaine on the Julia track.


[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[str-join]: https://docs.python.org/3/builtins/stdtypes.html#str.join
