import errno
import inspect
import io
import os


ZEN = b"""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""


class MockException(Exception):
    pass


class MockFile(io.BytesIO):
    def __init__(self, *args, chunk=None, exception=None, **kwargs):
        super(MockFile, self).__init__(*args, **kwargs)
        self.__chunk = chunk
        self.__exception = exception

    def __exit__(self, exc_type, exc_val, exc_tb):
        ret = super(MockFile, self).__exit__(exc_type, exc_val, exc_tb)
        if exc_type is not None and "suppress" in exc_val.args[0]:
            return True
        return ret

    def read(self, size=-1):
        if self.__exception is not None:
            raise self.__exception
        if self.__chunk is None:
            return super(MockFile, self).read(size)
        if size is None:
            return super(MockFile, self).read(self.__chunk)
        if size < 0:
            return super(MockFile, self).read(self.__chunk)
        return super(MockFile, self).read(min(self.__chunk, size))

    def write(self, data):
        if self.__chunk is None:
            return super(MockFile, self).write(data)
        return super(MockFile, self).write(data[: self.__chunk])


class MockSock:
    def __init__(self, *, chunk=None, exception=None):
        self._recver = io.BytesIO(ZEN)
        self._sender = io.BytesIO()
        self.__closed = False
        self.__chunk = chunk
        self.__exception = exception
        self.flags = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._recver.close()
        self._sender.close()
        self.__closed = True
        if exc_type is not None and "suppress" in exc_val.args[0]:
            return True
        return False

    def recv(self, bufsize, flags=0):
        if self.__closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if bufsize is None:
            raise TypeError("'NoneType' object cannot be interpreted as an integer")
        if not isinstance(flags, int):
            raise TypeError(
                "an integer is required (got type {})".format(type(flags).__name__)
            )
        self.flags = flags
        if self.__exception is not None:
            raise self.__exception
        if self.__chunk is None:
            return self._recver.read(bufsize)
        else:
            return self._recver.read(min(self.__chunk, bufsize))

    def send(self, data, flags=0):
        if self.__closed:
            raise OSError(errno.EBADF, os.strerror(errno.EBADF))
        if not isinstance(flags, int):
            raise TypeError(
                "an integer is required (got type {})".format(type(flags).__name__)
            )
        self.flags = flags
        if self.__chunk is None:
            return self._sender.write(data)
        return self._sender.write(data[: self.__chunk])


class SuperMock:
    """Mock for super().__init__ calls only, as mock.MagicMock cannot."""

    def __init__(self, *args, **kwargs):
        if self.initialized:
            self.init_called += 1
        else:
            self.initialized = True

    def __call__(self, *args, **kwargs):
        frame = inspect.currentframe()
        if frame is None:
            raise RuntimeError("Could not get current frame object")
        stack = inspect.getouterframes(frame)
        if any(frame[3] == "__init__" and "paasio" in frame[1] for frame in stack):
            return self
        else:
            return self.mock_object

    def __repr__(self):
        return "<SuperMock at {} with mock object: {!r}>".format(
            hex(id(self)), self.mock_object
        )

    mock_object = None
    init_called = 0
    initialized = False
