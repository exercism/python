# binary, octal, hexadecimal

Binary, octal, and hexadecimal (_also known as hex_) are different [numeral systems][numeral-systems] with different bases.
Binary is base 2, octal is base 8 and hexadecimal is base 16.
Normal integers are base 10 in python.
Binary, octal, and hexadecimal are all a subset of integers.
Which means that they can only represent whole numbers and support all the operations that we can do with integers.

## Binary

[Binary][binary] is a base 2 numeral system.
The most common numeral system is base 10.
In the base 10 numeral system so are the digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
Binary is base 2, so the digits are 0 and 1.
It is used to represent the on and off states of a computer.
Binary can create all the numbers that we use in base 10.

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

In Python, we can represent binary numbers using the `0b` prefix.
If we write `0b10011`, Python will interpret it as a binary number and convert it to base 10.

```python
# 0b10011
>>> 0b10011
19

>>> type(0b10011)
<class 'int'>
```

Binary in python is a subset of integers, therefore it will act like an integer.

If you have a number which is not in the binary system, it will raise a `SyntaxError`.

```python
Traceback (most recent call last):
  File "c:\binary.py", line 1, in <module>
    0b10211
SyntaxError: invalid digit '2' in binary literal
```

### Operations with binary numbers

Since binary is a subset of integers, we can do all the operations that we can do with integers.

```python
# addition
>>> 0b10011 + 0b10011
38

# multiplication
>>> 0b10011 * 0b10011
361
```

We can do also have operations with both integers and binary numbers.

```python
>>> 0b10011 + 19
38
```

### Representing binary numbers

Since python will automatically convert binary to `int`, do we have to use the `bin()` function.
If we want to represent a binary number.
`bin()` will return a `string` with the prefix `0b`.

```python
>>> bin(0b10011)
'0b10011'
```

To convert a binary number to an integer, we can use the `int()` function, and pass the string and the base as arguments.

```python
>>> int("0b10011", 2)
19
```

Giving the wrong base will raise a `ValueError`:

```python
Traceback (most recent call last):
  File "c:\Users\carlh\fwfa.py", line 4, in <module>
    int("0b10011", 3)
ValueError: invalid literal for int() with base 3: '0b10011'
```

### Converting int to binary

We can also convert an integer to binary using the `bin()` function.

```python
# 0b10011
>>> bin(19)
'0b10011'
```

### Binary methods

There are also [methods][numeral-systems] that we can use on binary numbers.

#### `<int>.bit_length()`

`<int>.bit_length()` will return the number of bits that are needed to represent the number.
So for example `0b10011` will return 5.

```python
>>> 0b11011.bit_length()
5
```

#### `<int>.count()`

```exercism/note
`<bin>.count()` requires Python 3.10+.
If you are using the online editor then you don't need to worry about this.
```

`<int>.bit_count()` will return the number of **ones** in the binary number.
So for example `bit_count` will return 3.

```python
>>> 0b11011.bit_count()
4
```

## Octal

[Octal][octal] is a base 8 numeral system.
Meaning that the digits are: 0, 1, 2, 3, 4, 5, 6, 7.

In python, we can represent octal numbers using the `0o` prefix.
As with binary, python will automatically convert octal to int.

```python
# 0o123
>>> 0o123
83
```

As with binary you can do all the operations that you can do with integers and giving a number which is not in the octal system will raise a `SyntaxError`.

### Representing octal numbers

To represent an octal number, we can use the `oct()` function.

```python
>>> oct(0o123)
'0o123'
```

To convert an octal number to an integer, we can use the `int()` function, and pass the string and the base as arguments.

```python
>>> int("0o123", 8)
83
```

As with binary, giving the wrong base will raise a `ValueError`.

### Converting int to octal

We can also convert an integer to binary using the `oct()` function.

```python
>>> oct(83)
'0o123'
```

### hexadecimal

[Hexadecimal][hexadecimal] is a base 16 numeral system.
Meaning that the digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
A is 10, B is 11, C is 12, D is 13, E is 14, F is 15.

In python, we can represent hexadecimal numbers using the `0x` prefix.
As with binary and octal, python will automatically convert hexadecimal to int.

```python
# 0o123
>>> 0x123
291
```

As with binary and octal you can do all the operations that you can do with integers and giving a number which is not in the hex system will raise a `SyntaxError`.

### Representing hexadecimal numbers

To represent an hexadecimal number, we can use the `hex()` function.

```python
>>> hex(0x123)
'0x123'
```

To convert an hexadecimal number to an integer, we can use the `int()` function, and pass the string and the base as arguments.

```python
>>> int("0x123", 16)
291
```

As with binary and octal, giving the wrong base will raise a `ValueError`.

### Converting int to hexadecimal

We can also convert an integer to binary using the `hex()` function.

```python
>>> hex(291)
'0x123'
```

[binary]: https://en.wikipedia.org/wiki/Binary_number
[octal]: https://en.wikipedia.org/wiki/Octal
[hexadecimal]: https://en.wikipedia.org/wiki/Hexadecimal
[numeral-systems]: https://en.wikipedia.org/wiki/Numeral_system
[methods-int]: https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types
