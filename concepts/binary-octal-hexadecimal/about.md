# Binary, Octal, and Hexadecimal

Binary, octal, and hexadecimal (_also known as hex_) are different [numeral systems][numeral-systems] with different bases.
Binary is base 2, octal is base 8, and hexadecimal is base 16.
Normal integers are base 10 in python.
Binary, octal, and hexadecimal are all representations of integers.
Which means that they represent positive and negative numbers (_including zero_) without fractions or decimals, and support all the operations that we can do with integers.

## Binary

[Binary][binary] is a base 2 numeral system, using only the digits 0 and 1.
It commonly represents the 0 ("off") and 1 ("on") states of electrical flow through transistors and switches in computers, as well as the positive and negative charges in magnetic storage media.
Binary can represent all the integers that are used in base 10.

A snippet from the base 2 system looks like this, although it continues infinitely and doesn't stop at 128:

| 128      | 64       | 32       | 16       | 8        | 4        | 2        | 1        |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 2 \*\* 7 | 2 \*\* 6 | 2 \*\* 5 | 2 \*\* 4 | 2 \*\* 3 | 2 \*\* 2 | 2 \*\* 1 | 2 \*\* 0 |

So if we want to represent the number 6, it would in binary be: 110

| Place value   | 4   | 2   | 1   |
| ------------- | --- | --- | --- |
| Binary number | 1   | 1   | 0   |

And the operation would be: `4 + 2 + 0 = 6`

Another example: 19

| Place value   | 16  | 8   | 4   | 2   | 1   |
| ------------- | --- | --- | --- | --- | --- |
| Binary number | 1   | 0   | 0   | 1   | 1   |

The binary number would be: 10011
And the operation would be: `16 + 0 + 0 + 2 + 1 = 19`

## Binary in Python

In Python, we can represent binary literals using the `0b` prefix.
If we write `0b10011`, Python will interpret it as a binary number and convert it to base 10.

```python
# 0b10011
>>> 0b10011
19

>>> type(0b10011)
<class 'int'>
```

Binary in Python is just a different way of writing an integer and so the binary representation **is an integer** for all mathematical operations.

If you write a number with a `0b` prefix that is not in the binary system, it will raise a `SyntaxError`.

```python
Traceback (most recent call last):
  File "c:\binary.py", line 1, in <module>
    0b10211
SyntaxError: invalid digit '2' in binary literal
```

### Operations with Binary Numbers

Since binary numbers are integers, we can perform all operations on them that we can with integers.

```python
# addition
>>> 0b10011 + 0b10011
38

# multiplication
>>> 0b10011 * 0b10011
361
```

We can also perform operations between both binary and integer representations.
However, the usual mathematical operator rules apply:  dividing two binary numbers or integer numbers will return a `float`, even if the division does not result in a decimal portion.

```python
>>> 0b10011 + 19
38

>>> 0b10011/0b10011
1.0

>>> 0b10011/3
6.333333333333333

### Converting to and from Binary Representation

Python will automatically convert a binary literal into `int`.
 To convert an `int` into a binary representation, use the built-in [`bin()`][bin] function.
`bin()` will return a `str` of the binary equivalent with the prefix `0b` .

```python
>>> bin(19)
'0b10011'
```

To convert a binary literal to an integer, we can use the built-in `int()` function, and pass a string of the binary representation and a base argument:

```python
>>> int("0b10011", 2)
19
```

Giving the wrong base (_or an invalid binary representation_) will raise a `ValueError`:

```python
Traceback (most recent call last):
  File "c:\binary.py", line 4, in <module>
    int("0b10011", 3)
ValueError: invalid literal for int() with base 3: '0b10011'
```

### Binary Methods

There are also some special [methods][numeral-systems] that we can use on binary numbers.


[`<int>.bit_length()`][bit_length] will return the number of bits that are needed to represent the number:

```python
>>> 0b11011.bit_length()
5
```


[`<int>.bit_count()`][bit_count] will return the number of **ones** in the binary number.
For example, `bit_count()` on '0b11011' will return 4:

```python
>>> 0b11011.bit_count()
4
~~~~exercism/note
If you are working locally, `bit_count()` requires at least Python 3.10.
The Exercism online editor currently supports all features through Python 3.11.
~~~~ 


## Octal

[Octal][octal] is a base 8 numeral system.
It uses the digits 0, 1, 2, 3, 4, 5, 6, and 7.

In Python, we can represent octal numbers using the `0o` prefix.
As with binary, Python automatically converts an octal representation to an `int`.

```python
# 0o123
>>> 0o123
83
```

As with binary, octal numbers **are ints** and support all integer operations.
Prefixing a number with `0o` that is not in the octal system will raise a `SyntaxError`.

 ### Converting to and from Octal Representation
 

To convert an `int` into an octal representation, you can use the built-in [`oct()`][oct] function.
This acts similarly to the `bin()` function, returning a string:

```python
>>> oct(83)
'0o123'

To convert an octal number to an integer, we can use the `int()` function, passing an octal string representation and the base (8) as arguments:

```python
>>> int("0o123", 8)
83
```

As with binary, giving the wrong base will raise a `ValueError`.

### Hexadecimal

[Hexadecimal][hexadecimal] is a base 16 numeral system.
It uses the digits 0 - 9 and the letters A, B, C, D, E, and F.
A is 10, B is 11, C is 12, D is 13, E is 14, and F is 15.

We can represent hexadecimal numbers in Python using the `0x` prefix.
As with binary and octal, Python will automatically convert hexadecimal literals to `int`.

```python
# 0x123
>>> 0x123
291
```

As with binary and octal - hexidecimal literals **are ints**, and you can perform all integer operations.  
Prefixing a non-hexidecimal number with `0x` will raise a `SyntaxError`.


###  Converting to and from Hexadecimal Representation

To convert an `int` into a hexadecimal representation, you can use the built-in [`hex()`][hex] function.
This acts similarly to the `bin()` function, returning a string:

```python
>>> hex(291)
'0x123'

To convert a hexadecimal representation to an integer, we can use the `int()` function, passing a hexadecimal string with the base (16) as arguments:

```python
>>> int("0x123", 16)
291
```

As with binary and octal, giving the wrong base will raise a `ValueError`.


[binary]: https://en.wikipedia.org/wiki/Binary_number
[bit_count]:  https://docs.python.org/3/library/stdtypes.html#int.bit_count
[bit_length]: https://docs.python.org/3/library/stdtypes.html#int.bit_length
[bit_count]:  https://docs.python.org/3/library/stdtypes.html#int.bit_count
[bit_length]: https://docs.python.org/3/library/stdtypes.html#int.bit_length
[hexadecimal]: https://en.wikipedia.org/wiki/Hexadecimal
[methods-int]: https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types
[numeral-systems]: https://en.wikipedia.org/wiki/Numeral_system
[octal]: https://en.wikipedia.org/wiki/Octal
