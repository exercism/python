# Standard Library


```python
from queue import Queue

class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = Queue(capacity)

    def read(self):
        if self.buffer.empty():
            raise BufferEmptyException("Circular buffer is empty")
        return self.buffer.get()

    def write(self, data):
        if self.buffer.full():
            raise BufferFullException("Circular buffer is full")
        self.buffer.put(data)

    def overwrite(self, data):
        if self.buffer.full():
            _ = self.buffer.get()
        self.buffer.put(data)

    def clear(self):
        while not self.buffer.empty():
            _ = self.buffer.get()
```

The above code uses a [`Queue` object][queue] to "implement" the buffer, a collection class which assumes entries will be added at the end and removed at the beginning.
This is a "queue" in British English, though Americans call it a "line".


Alternatively, the `collections` module provides a [`deque` object][deque], a double-ended queue class.
A `deque` allows adding and removing entries at both ends, which is not something we need for a circular buffer.
However, the syntax may be even more concise than for a `queue`:


```python
from collections import deque
from typing import Any

class CircularBuffer:
    def __init__(self, capacity: int):
        self.buffer = deque(maxlen=capacity)

    def read(self) -> Any:
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        return self.buffer.popleft()

    def write(self, data: Any) -> None:
        if len(self.buffer) == self.buffer.maxlen:
            raise BufferFullException("Circular buffer is full")
        self.buffer.append(data)

    def overwrite(self, data: Any) -> None:
        self.buffer.append(data)

    def clear(self) -> None:
        if len(self.buffer) > 0:
            self.buffer.popleft()
```

Both `Queue` and `deque` have the ability to limit the queues length by declaring a 'capacity' or 'maxlen' attribute.
This simplifies empty/full and read/write tracking.


Finally, the [`array`][array-array] class from the [`array`][array.array] module can be used to initialize a 'buffer' that works similarly to a built-in `list` or `bytearray`, but with efficiencies in storage and access:


```python
from array import array


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = array('u')
        self.capacity = capacity
        self.marker = 0

    def read(self):
        if not self.buffer: 
            raise BufferEmptyException('Circular buffer is empty')   

        else:
            data = self.buffer.pop(self.marker)
            if self.marker > len(self.buffer)-1: self.marker = 0
            
            return data
    
    def write(self, data):
        if len(self.buffer) < self.capacity:
            try:
                self.buffer.append(data)
            except TypeError:
                self.buffer.append(data)
        
        else: raise BufferFullException('Circular buffer is full')
    
    def overwrite(self, data):
        if len(self.buffer) < self.capacity: self.buffer.append(data)
        
        else:
            self.buffer[self.marker] = data

            if self.marker < self.capacity - 1: self.marker += 1  
            else: self.marker = 0
    
    def clear(self):
        self.marker = 0
        self.buffer = array('u')
```

[queue]: https://docs.python.org/3/library/queue.html
[deque]: https://docs.python.org/3/library/collections.html#deque-objects
[array-array]: https://docs.python.org/3.11/library/array.html#array.array
[array.array]: https://docs.python.org/3.11/library/array.html#module-array
