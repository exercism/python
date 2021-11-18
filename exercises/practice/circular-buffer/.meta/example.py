class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:

    def __init__(self, capacity):
        self.buffer = bytearray(capacity)
        self.read_point = 0
        self.write_point = 0

    # (protected) helper method to support python 2/3
    def _update_buffer(self, data):
        try:
            self.buffer[self.write_point] = data
        except TypeError:
            self.buffer[self.write_point] = ord(data)

    def clear(self):
        self.buffer = bytearray(len(self.buffer))

    def write(self, data):
        if all(self.buffer):
            raise BufferFullException('Circular buffer is full')
        self._update_buffer(data)
        self.write_point = (self.write_point + 1) % len(self.buffer)

    def overwrite(self, data):
        self._update_buffer(data)
        if all(self.buffer) and self.write_point == self.read_point:
            self.read_point = (self.read_point + 1) % len(self.buffer)
        self.write_point = (self.write_point + 1) % len(self.buffer)

    def read(self):
        if not any(self.buffer):
            raise BufferEmptyException('Circular buffer is empty')
        data = chr(self.buffer[self.read_point])
        self.buffer[self.read_point] = 0
        self.read_point = (self.read_point + 1) % len(self.buffer)
        return data
