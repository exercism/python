# Introduction

The key to this exercise is to:

- Create a suitable collection object to hold the values.
- Keep track of size as elements are added and removed.

## General Guidance



## Exception classes

All the approaches rely on being able to raise two custom exceptions, with suitable error messages.

```python
class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full."""
    
    def __init__(self, message):
        self.message = message

class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty."""
    
    def __init__(self, message):
        self.message = message
```

Code for these is always quite similar, so for brevity this aspect will be omitted from the various approaches.

## Approach: Using built-in types

Python has an exceptionally flexible and widely-used `list` type.
Most submitted solutions are based on this.

A less versatile variant is the `bytearray`.

This  is similar to a list in many ways, but is limited to holding integers in the range `0 <= n < 256`

For details, see the [built-in types][approaches-built-in] approach.

## Approach: Using collection classes from the standard library

A circular buffer is a type of fixed-size queue, and Python provides various implementations of this very useful type of collection.

The `queue` module contains the `Queue` class, which can be initialized with a maximum capacity.

Similarly, the `collections` module contains a `deque` class (short for Double Ended QUEue).

For details, see the [standard library][approaches-standard-library] approach.

## Which Approach to Use?

Anyone just wanting to use a circular buffer to get other things done is likely to pick a `Queue` or `deque`, as either of these will handle much of the low-level bookkeeping.

For a more authentic learning experience, using a `list` will provide practice in keeping track of capacity, and a `bytearray` takes this a stage further into low-level operations.

In reality, anyone wanting to get a deeper understanding of these collection structures might do even better to try solving the exercise in a statically-typed system language such as C, or even an assembly language like MIPS.

Python perhaps makes this exercise too easy?

[approaches-built-in]: https://exercism.org/tracks/python/exercises/circular-buffer/approaches/built-in-types
[approaches-standard-library]: https://exercism.org/tracks/python/exercises/circular-buffer/approaches/standard-library
