# About

Down at the hardware level, transistors can only be on or off: two states that we traditionaly represent with `1` and `0`. 
These are `binary digits`, abbreviated as `bits`.

This is particularly important for systems pprogrammers working in low-level languages.
However, for most of the history of computing the priority has been to find increasing sophisticated ways to hide the binary reality from most users.
Hence we work with `int`, `float`, `string` and many other types, up to audio and video formats.

Nevertheless, bitwise operations can sometimes have significant advantages in speed and memory efficiency, even in a high-level scripting language like Python.

## Entering and displaying binary numbers

Unsurprisingly, Python interacts with the user using decimal numbers by default, but the programmer can override this.

Binary numbers are just entered with a `0b` prefix, just as `0x` can be used for hexadecimal (hex numbers are a concise way to represent groups of 4 bits).
Note that these are all really an `int`, just displayed differently.

There are multiple ways to convert integers to binary strings, varying in whether they include the `0b` prefix and whether they support left-padding with zeros.

```python
>>> 0b10111  # binary entry
23

>>> bin(23)  # int to binary string, with prefix
'0b10111'

>>> n = 23
>>> format(n, '08b')  # no prefix, padded to 8 digits
'00010111'
>>> f"{n} in decimal is {n:08b} in binary and {n:x} in hex" # same, but using an f-string
'23 in decimal is 00010111 in binary and 17 in hex'
```

## [`Shift operators`][bitwise-operators]

The left-shift operator `x << y` simply moves all the bits in `x` by `y` places to the left, filling the new gaps with zeros.
Note that this is arithmetically identical to multiplying by `2**y`.

The right-shift operator `x >> y` does the opposite (for non-negative numbers, see below for how negative numbers work).
This is arithmetically identical to integer division `x // 2**y`.

```python
>>> x = 8
>>> format(x, '08b')
'00001000'

>>> x << 2  # left shift 
32
>>> format(x << 2, '08b')
'00100000'
>>> format(x >> 2, '08b')  # right shift
'00000010'
```

## [`Bitwise logic`][bitwise-operators]

In a previous concept, we saw the logical operators `and`, `or` and `not` which operate on `True` and `False` values.

In the bitwise equivalent, the operators are applied to each bit in the number, treating `1` as `True` and `0` as `False.`
An example with bitwise `&` (and) might make this clearer:

```python
>>> x = 0b01100110
>>> y = 0b00101010
>>> format(x & y, '08b')
'00100010'
```

Only positions with a `1` in _both_ the input strings are set to `1` in the output.

Bitwise `&` is commonly used as a way to isolate single bits in a compacted set of `True`/`False` flags, for example user-configurable settings in an app.
This lets the value of individual bits control program logic.

```python
>>> n = 0b0110
>>> n & 0b0001 > 0
False
>>> n & 0b0010 > 0
True
```

For a bitwise `|` (or), a `1` is set in the output if there is a `1` in _either_ of the inputs:

```python
>>> format(x | y, '08b')
'01101110'
```

There is also a `^` operator for bitwise exclusive or (xor).
In this case, a `1` is set if it appears in either of the inputs _but not both_.

If xor `^` seems strange, be aware that this is by far the most common operation in cryptography.

```python
>>> format(x ^ y, '08b')
'01001100'
```

Finally, there is the `~` operator (the tilde character), which is a bitwise `not` that takes a single input and inverts all the bits.
Each `1` changes to `0` and vice versa.

`Bitwise ~` may give an answer you were not expecting.
See the next section for details.

## Negative numbers

In decimal representation, we distinguish positive and negative numbers by putting a `+` or `-` sign in front.

Doing this at binary level proved inefficient for digital computing.
Not least, it raised the problem that `+0` is not the same as `-0`.

Instead, all modern computers use a `twos-complement` representation for negative numbers, right down to the silicon chip level.

This means that all bits are inverted, and a number is interpreted as negative if the left-most bit is `1`.

As an added complication, recent versions of Python no longer use finite-integer concepts like `int32` internally.
Instead, an `int` can now be of unlimited size, and a negative or bit-inverted number has a (theoretically) infinite number of `1`'s to the left, just as a positive number has `0`'s.

This makes it hard to give a useful example of bitwise not:

```python
>>> format(x, '08b')
'01100110'
>>> format(~x, '08b')
'-1100111'  # negative binary (not twos-complement display)

>>> x
102  # decimal
>>> ~x
-103
```

This is _not_ the `0b10011001` we would see in languages with fixed-size integers.

The `~` operator works as expected with `unsigned` byte or integer types.
These are supported in third-party packages such as `NumPy`, but not in core Python.

In practice, Python programmers quite often use shift operators and `& | ^` with positive numbers.
Bitwise operations with negative numbers are much less common.



[bitwise-operators]: https://wiki.python.org/moin/BitwiseOperators