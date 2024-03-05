# Introduction

The key to this exercise is to:

- Create a suitable collection object to hold the values.
- Keep track of size as elements are added and removed.

## General Guidance

Approaches to this exercise vary from easy but rather boring, to complex but educational.

It would be useful to think about what you want from completing the exercise, then choose an appropriate collection class that fits your aims.


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

Code for these error handling scenarios is always quite similar, so for brevity this aspect will be omitted from the various approaches to the exercise.


## Approach: Using built-in types

Python has an exceptionally flexible and widely-used `list` type.
Most submitted solutions to `Circular Buffer` are based on this data type.

Less versatile variants include [`bytearray`][bytearray] and [`array.array`][array.array].

`bytearray`s are similar to `list`s in many ways, but they are limited to holding only bytes (_represented as integers in the range `0 <= n < 256`_).

For details, see the [built-in types][approaches-built-in] approach.


Finally, [`memoryview`s][memoryview] allow for direct access to the binary data (_ without copying_) of Python objects that support the  [`Buffer Protocol`][buffer-protocol].
 `memoryview`s can be used to directly access the underlying memory of types such as `bytearray`, `array.array`, `queue`, `dequeue`, and `list` as well as working with [ctypes][ctypes] from outside libraries and C [structs][struct].

 For additional information on the `buffer protocol`, see [Emulating Buffer Types][emulating-buffer-types] in the Python documentation.
 As of Python `3.12`, the abstract class [collections.abc.Buffer][abc-Buffer] is also available for classes that provide the [`__buffer__()`][dunder-buffer] method and implement the `buffer protocol`.


## Approach: Using collection classes from the standard library

A circular buffer is a type of fixed-size queue, and Python provides various implementations of this very useful type of collection.

- The [`queue`][queue-module] module contains the [`Queue`][Queue-class] class, which can be initialized with a maximum capacity.
- The [`collections`][collections-module] module contains a [`deque`][deque-class] class (short for Double Ended QUEue), which can also be set to a maximum capacity.
- The [`array`][array.array] module contains an [`array`][array-array] class that is similar to Python's built-in `list`, but is limited to a single datatype (_available datatypes are mapped to C datatypes_).
This allows values to be stored in a more compact and efficient fashion.


For details, see the [standard library][approaches-standard-library] approach.


## Which Approach to Use?

Anyone just wanting to use a circular buffer to get other things done and is not super-focused on performance is likely to pick a `Queue` or `deque`, as either of these will handle much of the low-level bookkeeping.

For a more authentic learning experience, using a `list` will provide practice in keeping track of capacity, with  `bytearray` or `array.array` taking the capacity and read/write tracking a stage further.


For a really deep dive into low-level Python operations, you can explore using `memoryview`s into `bytearray`s or [`numpy` arrays][numpy-arrays], or customize your own `buffer protocol`-supporting Python object, `ctype` or `struct`.
Some 'jumping off' articles for this are [circular queue or ring buffer (Python and C)][circular-buffer], [memoryview Python Performance][memoryview-py-performance], and [Less Copies in Python with the buffer protocol and memoryviews][less-copies-in-Python].


In reality, anyone wanting to get a deeper understanding of how these collection structures work "from scratch" might do even better to try solving the exercise in a statically-typed system language such as C, Rust, or even try an assembly language like MIPS.

[Queue-class]: https://docs.python.org/3.11/library/queue.html#queue.Queue
[abc-Buffer]: https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer
[approaches-built-in]: https://exercism.org/tracks/python/exercises/circular-buffer/approaches/built-in-types
[approaches-standard-library]: https://exercism.org/tracks/python/exercises/circular-buffer/approaches/standard-library
[array-array]: https://docs.python.org/3.11/library/array.html#array.array
[array.array]: https://docs.python.org/3.11/library/array.html#module-array
[buffer-protocol]: https://docs.python.org/3/c-api/buffer.html
[bytearray]: https://docs.python.org/3/library/stdtypes.html#bytearray
[circular-buffer]: https://towardsdatascience.com/circular-queue-or-ring-buffer-92c7b0193326
[collections-module]: https://docs.python.org/3.11/library/collections.html
[ctypes]: https://docs.python.org/3/library/ctypes.html
[deque-class]: https://docs.python.org/3.11/library/collections.html#collections.deque
[dunder-buffer]: https://docs.python.org/3/reference/datamodel.html#object.__buffer__
[emulating-buffer-types]: https://docs.python.org/3/reference/datamodel.html#emulating-buffer-types
[less-copies-in-Python]: https://eli.thegreenplace.net/2011/11/28/less-copies-in-python-with-the-buffer-protocol-and-memoryviews
[memoryview-py-performance]: https://prrasad.medium.com/memory-view-python-performance-improvement-method-c241a79e9843
[memoryview]: https://docs.python.org/3/library/stdtypes.html#memoryview
[numpy-arrays]: https://numpy.org/doc/stable/reference/generated/numpy.array.html
[queue-module]: https://docs.python.org/3.11/library/queue.html
[struct]: https://docs.python.org/3/library/struct.html
