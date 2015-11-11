class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):

    def __init__(self, capacity):
        self.buffer = bytearray(capacity)
        self.read_point = 0
        self.write_point = 0

    def clear(self):
        self.buffer = bytearray(len(self.buffer))

    def write(self, data):
        if all(self.buffer):
            raise BufferFullException
        self.buffer[self.write_point] = data
        self.write_point = (self.write_point + 1) % len(self.buffer)

    def overwrite(self, data):
        self.buffer[self.write_point] = data
        if all(self.buffer) and self.write_point == self.read_point:
            self.read_point = (self.read_point + 1) % len(self.buffer)
        self.write_point = (self.write_point + 1) % len(self.buffer)

    def read(self):
        if not any(self.buffer):
            raise BufferEmptyException
        data = chr(self.buffer[self.read_point])
        self.buffer[self.read_point] = 0
        self.read_point = (self.read_point + 1) % len(self.buffer)
        return data
