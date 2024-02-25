# Built In Types

```python
class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.content = []

    def read(self) -> str:
        if not self.content:
            raise BufferEmptyException("Circular buffer is empty")
        return self.content.pop(0)

    def write(self, data: str) -> None:
        if len(self.content) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.content.append(data)

    def overwrite(self, data: str) -> None:
        if len(self.content) == self.capacity:
            self.content.pop(0)
        self.write(data)

    def clear(self) -> None:
        self.content = []
```

In Python, the `list` type is ubiquitous and exceptionally versatile.

Code similar to that shown above is a very common way to implement this exercise.

Though lists can do much more, here we just use `append()` to add an entry to the end of the list, and `pop(0)` to remove an entry from the beginning.

By design, lists have no built-in length limit and can grow arbitrarily, so the main task of the programmer here is to keep track of capacity.

A `list` is also designed to hold any mix of any Python objects, and this flexibility is emphasized over performance.

For more precise control, at the price of some increased programming complexity, it is possible to use a [`bytearray`][bytearray].

In this case, entries are of fixed type: integers in the range `0 <= n < 256`.

The tests are designed such that this is sufficient to solve the exercise, and byte handling may be quite a realistic view of how circular buffers are often used in practice.

The code below shows an implementation using this lower-level collection class:

```python
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = bytearray(capacity)
        self.read_start = 0
        self.write_start = 0

    def read(self):
        if not any(self.capacity):
            raise BufferEmptyException('Circular buffer is empty')
        
        data = chr(self.capacity[self.read_start])
        self.capacity[self.read_start] = 0
        self.read_start = (self.read_start + 1) % len(self.capacity)
        
        return data

    def write(self, data):
        if all(self.capacity):
            raise BufferFullException('Circular buffer is full')
        
        try:
            self.capacity[self.write_start] = data
        except TypeError:
            self.capacity[self.write_start] = ord(data)
        
        self.write_start = (self.write_start + 1) % len(self.capacity)

    def overwrite(self, data):
        try:
            self.capacity[self.write_start] = data
        except TypeError:
            self.capacity[self.write_start] = ord(data)
            
        if all(self.capacity) and self.write_start == self.read_start:
            self.read_start = (self.read_start + 1) % len(self.capacity)
            self.write_start = (self.write_start + 1) % len(self.capacity)

    def clear(self):
        self.capacity = bytearray(len(self.capacity))
```

[bytearray]: https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
