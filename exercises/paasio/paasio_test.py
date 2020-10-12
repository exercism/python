import errno
import inspect
import io
import logging
import os
import unittest
from unittest.mock import ANY, call, NonCallableMagicMock, patch

from paasio import MeteredFile, MeteredSocket


LOGGER = logging.getLogger(__name__)

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


# Implementation tests begin on line 456
# Code below this line consists of mocks and tests for mocks compliance


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
            raise TypeError(
                "'NoneType' object cannot be interpreted as an integer"
            )
        if not isinstance(flags, int):
            raise TypeError(
                "an integer is required (got type {})".format(
                    type(flags).__name__
                )
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
                "an integer is required (got type {})".format(
                    type(flags).__name__
                )
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
        if any(
            frame[3] == "__init__" and "paasio" in frame[1] for frame in stack
        ):
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


class MockTestCase(unittest.TestCase):
    def setUp(self):
        self.test_passed = False

    def tearDown(self):
        if not self.test_passed:
            LOGGER.critical(
                "\nError in mocks, please report to Exercism: %s", self.id()
            )

    def test_fixture_exception(self):
        self.assertEqual(False, self.test_passed)
        with self.assertLogs(__name__, level="CRITICAL") as logs:
            self.tearDown()
        self.assertEqual(1, len(logs.output))
        self.assertRegex(logs.output[0], ":\nError in mocks")
        self.assertRegex(logs.output[0], "{}$".format(self.id()))
        self.test_passed = True


class SuperMockTest(MockTestCase):
    def test_super_mock_repr(self):
        mock = SuperMock()
        expected = "<SuperMock at {} with mock object: {}>".format(
            hex(id(mock)), repr(None)
        )
        self.assertEqual(expected, repr(mock))
        file = MockFile()
        mock.mock_object = file
        expected = "<SuperMock at {} with mock object: {}>".format(
            hex(id(mock)), repr(file)
        )
        self.assertEqual(expected, repr(mock))
        self.test_passed = True

    def test_super_mock_init(self):
        self.assertIs(False, SuperMock.initialized)
        mock = SuperMock()
        self.assertIs(True, mock.initialized)
        for calls in range(5):
            self.assertEqual(calls, mock.init_called)
            mock.__init__()
        self.test_passed = True

    def test_super_mock_call(self):
        def call2(obj):
            return obj()

        def __init__(obj):
            ret = call2(obj)
            self.assertEqual(obj(), ret)
            return ret

        mock = SuperMock()
        self.assertIs(None, mock.mock_object)
        wrapped = object()
        mock.mock_object = wrapped
        self.assertIs(wrapped, mock())
        self.assertIs(mock, __init__(mock))
        self.test_passed = True

    @patch("inspect.currentframe", return_value=None)
    def test_super_mock_frame_error(self, inspect_mock):
        with self.assertRaisesRegex(
            RuntimeError, "^Could not get current frame object$"
        ):
            SuperMock()()
        self.test_passed = True


class MockSockTest(MockTestCase):
    def test_context_manager(self):
        with MockSock() as socket:
            socket.recv(30)
            socket.send(b"data")
        with self.assertRaisesRegex(OSError, os.strerror(errno.EBADF)):
            socket.recv(30)
        with self.assertRaisesRegex(OSError, os.strerror(errno.EBADF)):
            socket.send(b"")
        self.test_passed = True

    def test_context_manager_exception_raise(self):
        exception = MockException("Should raise")
        with self.assertRaisesRegex(MockException, "Should raise") as err:
            with MockSock(exception=exception) as socket:
                socket.recv(4096)
        self.assertEqual(exception, err.exception)
        self.test_passed = True

    def test_context_manager_exception_suppress(self):
        exception = MockException("Should suppress")
        with MockSock(exception=exception) as socket:
            socket.recv(4096)
        self.test_passed = True

    def test_recv_once(self):
        with MockSock() as socket:
            actual_recv = socket.recv(4096)
        self.assertEqual(ZEN, actual_recv)
        self.test_passed = True

    def test_recv_multiple(self):
        actual_recv = b""
        with MockSock() as socket:
            for _ in range(5):
                actual_recv += socket.recv(30)
        self.assertEqual(ZEN[:150], actual_recv)
        self.test_passed = True

    def test_recv_multiple_chunk(self):
        actual_recv = b""
        with MockSock(chunk=20) as socket:
            for _ in range(5):
                actual_recv += socket.recv(4096)
            actual_recv += socket.recv(10)
        self.assertEqual(ZEN[:110], actual_recv)
        self.test_passed = True

    def test_recv_under_size(self):
        with MockSock(chunk=257) as socket:
            actual_recv = socket.recv(4096)
        self.assertEqual(ZEN[:257], actual_recv)
        self.test_passed = True

    def test_send_once(self):
        with MockSock(chunk=257) as socket:
            send_len = socket.send(ZEN)
            self.assertEqual(ZEN[:257], socket._sender.getbuffer())
        self.assertEqual(257, send_len)
        self.test_passed = True

    def test_send_multiple(self):
        send_len = 0
        expected = b"Tomorrow's victory is today's practice."
        with MockSock() as socket:
            send_len += socket.send(b"Tomorro")
            send_len += socket.send(b"w's victo")
            send_len += socket.send(b"ry is today")
            send_len += socket.send(b"'s practice.")
            self.assertEqual(expected, socket._sender.getbuffer())
        self.assertEqual(39, send_len)
        self.test_passed = True

    def test_send_under_size(self):
        with MockSock(chunk=257) as socket:
            send_len = socket.send(ZEN[:123])
            self.assertEqual(ZEN[:123], socket._sender.getbuffer())
        self.assertEqual(123, send_len)
        self.test_passed = True

    def test_bufsize_required(self):
        with self.assertRaisesRegex(TypeError, "argument"):
            with MockSock() as socket:
                socket.recv()

        with self.assertRaisesRegex(TypeError, "'NoneType'.+integer"):
            with MockSock() as socket:
                socket.recv(None)
        self.test_passed = True

    def test_flags_support(self):
        with MockSock() as socket:
            self.assertEqual(len(ZEN), socket.send(ZEN, 42))
            self.assertEqual(ZEN, socket.recv(4096, 24))
        with MockSock() as mock_sock:
            self.assertIs(None, mock_sock.flags)
            mock_sock.recv(50)
            self.assertEqual(0, mock_sock.flags)
            mock_sock.send(b"no flags")
            self.assertEqual(0, mock_sock.flags)
            mock_sock.recv(30, 30)
            self.assertEqual(30, mock_sock.flags)
            mock_sock.send(b"flags", 1024)
            self.assertEqual(
                1024, mock_sock.flags,
            )
            with self.assertRaisesRegex(
                TypeError, r"^an integer is.+NoneType\)$"
            ):
                mock_sock.send(b"data", None)
            with self.assertRaisesRegex(
                TypeError, r"^an integer is.+bytes\)$"
            ):
                mock_sock.send(b"data", b"flags")
            with self.assertRaisesRegex(
                TypeError, r"^an integer is.+NoneType\)$"
            ):
                mock_sock.recv(b"data", None)
            with self.assertRaisesRegex(
                TypeError, r"^an integer is.+bytes\)$"
            ):
                mock_sock.recv(b"data", b"flags")
        self.test_passed = True


class MockFileTest(MockTestCase):
    def test_context_manager(self):
        with MockFile(ZEN) as file:
            file.read()
        with self.assertRaisesRegex(
            ValueError, "I/O operation on closed file."
        ):
            file.read()
        with self.assertRaisesRegex(
            ValueError, "I/O operation on closed file."
        ):
            file.write(b"data")
        self.test_passed = True

    def test_context_manager_exception_raise(self):
        exception = MockException("Should raise")
        mock = MockFile(ZEN, exception=exception)
        with self.assertRaisesRegex(MockException, "Should raise") as err:
            with mock as file:
                file.read()
        self.assertEqual(exception, err.exception)
        self.test_passed = True

    def test_context_manager_exception_suppress(self):
        exception = MockException("Should suppress")
        mock = MockFile(ZEN, exception=exception)
        with mock as file:
            file.read()
        self.test_passed = True

    def test_read_once(self):
        with MockFile(ZEN) as file:
            actual_read = file.read()
        self.assertEqual(ZEN, actual_read)

        with MockFile(ZEN) as file:
            actual_read = file.read(None)
        self.assertEqual(ZEN, actual_read)

        with MockFile(ZEN) as file:
            actual_read = file.read(-1)
        self.assertEqual(ZEN, actual_read)
        self.test_passed = True

    def test_read_multiple(self):
        actual_read = b""
        with MockFile(ZEN) as file:
            for _ in range(5):
                actual_read += file.read(30)
        self.assertEqual(ZEN[:150], actual_read)
        self.test_passed = True

    def test_read_multiple_chunk(self):
        actual_read = b""
        with MockFile(ZEN, chunk=20) as file:
            for _ in range(5):
                actual_read += file.read()
            actual_read += file.read(10)
        self.assertEqual(ZEN[:110], actual_read)

        actual_read = b""
        with MockFile(ZEN, chunk=20) as file:
            for size in [None, -2, -1, 0, 1, 2]:
                actual_read += file.read(size)
            actual_read += file.read(10)
        self.assertEqual(ZEN[:73], actual_read)
        self.test_passed = True

    def test_read_under_size(self):
        with MockFile(ZEN, chunk=257) as file:
            actual_read = file.read()
        self.assertEqual(ZEN[:257], actual_read)
        self.test_passed = True

    def test_write_once(self):
        with MockFile(chunk=257) as file:
            write_len = file.write(ZEN)
            self.assertEqual(ZEN[:257], file.getbuffer())
            self.assertEqual(257, write_len)
        self.test_passed = True

    def test_write_multiple(self):
        write_len = 0
        expected = b"Tomorrow's victory is today's practice."
        with MockFile() as file:
            write_len += file.write(b"Tomorro")
            write_len += file.write(b"w's victo")
            write_len += file.write(b"ry is today")
            write_len += file.write(b"'s practice.")
            self.assertEqual(expected, file.getbuffer())
            self.assertEqual(len(expected), write_len)
        self.test_passed = True

    def test_write_under_size(self):
        with MockFile(chunk=257) as file:
            write_len = file.write(ZEN[:123])
            self.assertEqual(ZEN[:123], file.getbuffer())
            self.assertEqual(123, write_len)
        self.test_passed = True


# Tests for paasio.py begin here


class MeteredSocketTest(unittest.TestCase):
    def test_context_manager(self):
        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        with MeteredSocket(mock) as socket:
            self.assertFalse(mock.__enter__.called)
            socket.recv(30)
        self.assertFalse(mock.__enter__.called)
        mock.__exit__.assert_called_once_with(None, None, None)
        self.assertEqual(2, len(mock.mock_calls))
        with self.assertRaisesRegex(OSError, os.strerror(errno.EBADF)):
            socket.recv(30)
        with self.assertRaisesRegex(OSError, os.strerror(errno.EBADF)):
            socket.send(b"")

    def test_context_manager_exception_raise(self):
        exception = MockException("Should raise")
        wrapped = MockSock(exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        with self.assertRaisesRegex(MockException, "Should raise") as err:
            with MeteredSocket(mock) as socket:
                self.assertFalse(mock.__enter__.called)
                socket.recv(4096)
        self.assertFalse(mock.__enter__.called)
        mock.__exit__.assert_called_once_with(
            MockException, err.exception, ANY,
        )
        self.assertEqual(exception, err.exception)

    def test_context_manager_exception_suppress(self):
        exception = MockException("Should suppress")
        wrapped = MockSock(exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        with MeteredSocket(mock) as socket:
            self.assertFalse(mock.__enter__.called)
            socket.recv(4096)
        self.assertFalse(mock.__enter__.called)
        mock.__exit__.assert_called_once_with(
            MockException, exception, ANY,
        )

    def test_recv_once(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with MeteredSocket(mock) as socket:
            actual_recv = socket.recv(4096)
        self.assertEqual(ZEN, actual_recv)
        self.assertEqual(1, socket.recv_ops)
        self.assertEqual(len(ZEN), socket.recv_bytes)
        self.assertEqual(1, mock.recv.call_count)

    def test_recv_multiple(self):
        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        actual_recv = b""
        with MeteredSocket(mock) as socket:
            for _ in range(5):
                actual_recv += socket.recv(30)
        self.assertEqual(ZEN[:150], actual_recv)
        self.assertEqual(5, socket.recv_ops)
        self.assertEqual(150, socket.recv_bytes)
        self.assertEqual(5, mock.recv.call_count)

    def test_recv_multiple_chunk(self):
        wrapped = MockSock(chunk=20)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        actual_recv = b""
        with MeteredSocket(mock) as socket:
            for _ in range(5):
                actual_recv += socket.recv(4096)
            actual_recv += socket.recv(10)
        self.assertEqual(ZEN[:110], actual_recv)
        self.assertEqual(6, socket.recv_ops)
        self.assertEqual(110, socket.recv_bytes)
        self.assertEqual(6, mock.recv.call_count)

    def test_recv_under_size(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            actual_recv = socket.recv(4096)
        self.assertEqual(ZEN[:257], actual_recv)
        self.assertEqual(1, socket.recv_ops)
        self.assertEqual(257, socket.recv_bytes)
        self.assertEqual(1, mock.recv.call_count)

    def test_send_once(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            send_len = socket.send(ZEN)
            self.assertEqual(ZEN[:257], wrapped._sender.getbuffer())
        self.assertEqual(257, send_len)
        self.assertEqual(1, socket.send_ops)
        self.assertEqual(257, socket.send_bytes)
        self.assertEqual(1, mock.send.call_count)

    def test_send_multiple(self):
        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        send_len = 0
        expected = b"Tomorrow's victory is today's practice."
        with MeteredSocket(mock) as socket:
            send_len += socket.send(b"Tomorro")
            send_len += socket.send(b"w's victo")
            send_len += socket.send(b"ry is today")
            send_len += socket.send(b"'s practice.")
            self.assertEqual(expected, wrapped._sender.getbuffer())
        self.assertEqual(39, send_len)
        self.assertEqual(4, socket.send_ops)
        self.assertEqual(39, socket.send_bytes)
        self.assertEqual(4, mock.send.call_count)

    def test_send_under_size(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            send_len = socket.send(ZEN[:123])
            self.assertEqual(ZEN[:123], wrapped._sender.getbuffer())
        self.assertEqual(123, send_len)
        self.assertEqual(1, socket.send_ops)
        self.assertEqual(123, socket.send_bytes)
        self.assertEqual(1, mock.send.call_count)

    def test_bufsize_required(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with self.assertRaisesRegex(TypeError, "argument"):
            with MeteredSocket(mock) as socket:
                socket.recv()
        self.assertFalse(mock.recv.called)

        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with self.assertRaisesRegex(TypeError, "^'NoneType'.+integer$"):
            with MeteredSocket(mock) as socket:
                socket.recv(None)
        self.assertTrue(
            call(None) in mock.recv.mock_calls
            or call(None, ANY) in mock.recv.mock_calls
        )

    def test_flags_support(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with MeteredSocket(mock) as socket:
            self.assertEqual(len(ZEN), socket.send(ZEN, 42))
            self.assertEqual(ZEN, socket.recv(4096, 24))
        mock.send.assert_called_once_with(ZEN, 42)
        mock.recv.assert_called_once_with(4096, 24)

        wrapped = MockSock()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            socket.recv(50)
            self.assertEqual(0, wrapped.flags)
            socket.send(b"no flags")
            self.assertEqual(0, wrapped.flags)
            socket.recv(30, 30)
            self.assertEqual(30, wrapped.flags)
            socket.send(b"flags", 1024)
            self.assertEqual(1024, wrapped.flags)
            with self.assertRaisesRegex(TypeError, "integer is required"):
                socket.send(b"data", None)
            with self.assertRaisesRegex(TypeError, "integer is required"):
                socket.send(b"data", b"flags")
            with self.assertRaisesRegex(TypeError, "integer is required"):
                socket.recv(b"data", None)
            with self.assertRaisesRegex(TypeError, "integer is required"):
                socket.recv(b"data", b"flags")

    def test_stats_read_only(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with MeteredSocket(mock) as socket:
            self.assertEqual(0, socket.send_ops)
            self.assertEqual(0, socket.send_bytes)
            self.assertEqual(0, socket.recv_ops)
            self.assertEqual(0, socket.recv_bytes)
            for _ in range(277):
                socket.send(b"b")
            socket.send(b"bytes")
            for _ in range(257):
                socket.recv(1)
            socket.recv(2)
            self.assertEqual(278, socket.send_ops)
            self.assertEqual(282, socket.send_bytes)
            self.assertEqual(258, socket.recv_ops)
            self.assertEqual(259, socket.recv_bytes)
            with self.assertRaisesRegex(AttributeError, "can't set"):
                socket.send_ops = 0
            with self.assertRaisesRegex(AttributeError, "can't set"):
                socket.send_bytes = 0
            with self.assertRaisesRegex(AttributeError, "can't set"):
                socket.recv_ops = 0
            with self.assertRaisesRegex(AttributeError, "can't set"):
                socket.recv_bytes = 0
            self.assertEqual(278, socket.send_ops)
            self.assertEqual(282, socket.send_bytes)
            self.assertEqual(258, socket.recv_ops)
            self.assertEqual(259, socket.recv_bytes)


@patch("paasio.super", create=True, new_callable=SuperMock)
class MeteredFileTest(unittest.TestCase):
    def test_context_manager(self, super_mock):
        wrapped = MockFile(ZEN)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
        with MeteredFile() as file:
            self.assertEqual(1, super_mock.init_called)
            self.assertFalse(mock.__enter__.called)
            file.read()
        self.assertFalse(mock.__enter__.called)
        mock.__exit__.assert_called_once_with(None, None, None)
        self.assertEqual(2, len(mock.mock_calls))
        with self.assertRaisesRegex(
            ValueError, "I/O operation on closed file."
        ):
            file.read()
        with self.assertRaisesRegex(
            ValueError, "I/O operation on closed file."
        ):
            file.write(b"data")

    def test_context_manager_exception_raise(self, super_mock):
        exception = MockException("Should raise")
        wrapped = MockFile(ZEN, exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
        with self.assertRaisesRegex(MockException, "Should raise") as err:
            with MeteredFile() as file:
                self.assertFalse(mock.__enter__.called)
                file.read()
        self.assertFalse(mock.__enter__.called)
        mock.__exit__.assert_called_once_with(
            MockException, err.exception, ANY,
        )
        self.assertEqual(exception, err.exception)

    def test_context_manager_exception_suppress(self, super_mock):
        exception = MockException("Should suppress")
        wrapped = MockFile(ZEN, exception=exception)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        mock.__exit__.side_effect = wrapped.__exit__
        super_mock.mock_object = mock
        with MeteredFile() as file:
            self.assertFalse(mock.__enter__.called)
            file.read()
        self.assertFalse(mock.__enter__.called)
        mock.__exit__.assert_called_once_with(
            MockException, exception, ANY,
        )

    def test_iteration(self, super_mock):
        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
        actual_reads = b""
        file = MeteredFile()
        for line in file:
            actual_reads += line
            self.assertLess(
                0, mock.readline.call_count, "File's readline not called"
            )
            self.assertGreater(
                50, mock.readline.call_count, "Possible infinte loop detected"
            )
            self.assertEqual(file.read_ops, mock.readline.call_count)
        self.assertFalse(mock.__iter__.called)
        self.assertEqual(len(ZEN), file.read_bytes)
        self.assertEqual(ZEN, actual_reads)

    def test_read_once(self, super_mock):
        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            actual_read = file.read()
        self.assertEqual(ZEN, actual_read)
        self.assertEqual((len(ZEN)), file.read_bytes)
        self.assertEqual(1, file.read_ops)
        self.assertEqual(mock.read.call_count, file.read_ops)

        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            actual_read = file.read(None)
        self.assertEqual(ZEN, actual_read)
        self.assertEqual((len(ZEN)), file.read_bytes)
        self.assertEqual(1, file.read_ops)
        self.assertEqual(mock.read.call_count, file.read_ops)

        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            actual_read = file.read(-1)
        self.assertEqual(ZEN, actual_read)
        self.assertEqual((len(ZEN)), file.read_bytes)
        self.assertEqual(1, file.read_ops)
        self.assertEqual(mock.read.call_count, file.read_ops)

    def test_read_multiple(self, super_mock):
        wrapped = MockFile(ZEN)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        actual_read = b""
        with MeteredFile() as file:
            for _ in range(5):
                actual_read += file.read(30)
        self.assertEqual(ZEN[:150], actual_read)
        self.assertEqual(5, file.read_ops)
        self.assertEqual(150, file.read_bytes)
        self.assertEqual(5, mock.read.call_count)

    def test_read_multiple_chunk(self, super_mock):
        wrapped = MockFile(ZEN, chunk=20)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        actual_read = b""
        with MeteredFile() as file:
            for _ in range(5):
                actual_read += file.read()
            actual_read += file.read(10)
        self.assertEqual(ZEN[:110], actual_read)
        self.assertEqual(6, file.read_ops)
        self.assertEqual(110, file.read_bytes)
        self.assertEqual(6, mock.read.call_count)

        wrapped = MockFile(ZEN, chunk=20)
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        actual_read = b""
        with MeteredFile() as file:
            for size in [None, -2, -1, 0, 1, 2]:
                actual_read += file.read(size)
            actual_read += file.read(10)
        self.assertEqual(ZEN[:73], actual_read)
        self.assertEqual(7, file.read_ops)
        self.assertEqual(73, file.read_bytes)
        self.assertEqual(7, mock.read.call_count)

    def test_read_under_size(self, super_mock):
        wrapped = MockFile(ZEN, chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            actual_read = file.read()
        self.assertEqual(ZEN[:257], actual_read)
        self.assertEqual(1, file.read_ops)
        self.assertEqual(257, file.read_bytes)
        self.assertEqual(1, mock.read.call_count)

    def test_write_once(self, super_mock):
        wrapped = MockFile(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            write_len = file.write(ZEN)
            self.assertEqual(ZEN[:257], wrapped.getbuffer())
        self.assertEqual(257, write_len)
        self.assertEqual(1, file.write_ops)
        self.assertEqual(257, file.write_bytes)
        self.assertEqual(1, mock.write.call_count)

    def test_write_multiple(self, super_mock):
        wrapped = MockFile()
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        write_len = 0
        expected = b"Tomorrow's victory is today's practice."
        with MeteredFile() as file:
            write_len += file.write(b"Tomorro")
            write_len += file.write(b"w's victo")
            write_len += file.write(b"ry is today")
            write_len += file.write(b"'s practice.")
            self.assertEqual(expected, wrapped.getbuffer())
        self.assertEqual(39, write_len)
        self.assertEqual(4, file.write_ops)
        self.assertEqual(39, file.write_bytes)
        self.assertEqual(4, mock.write.call_count)

    def test_write_under_size(self, super_mock):
        wrapped = MockFile(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            write_len = file.write(ZEN[:123])
            self.assertEqual(ZEN[:123], wrapped.getbuffer())
        self.assertEqual(123, write_len)
        self.assertEqual(1, file.write_ops)
        self.assertEqual(123, file.write_bytes)
        self.assertEqual(1, mock.write.call_count)

    def test_stats_read_only(self, super_mock):
        mock = NonCallableMagicMock(wraps=MockFile(ZEN), autospec=True)
        super_mock.mock_object = mock
        with MeteredFile() as file:
            self.assertEqual(0, file.read_ops)
            self.assertEqual(0, file.read_bytes)
            for _ in range(57):
                file.read(1)
            file.read(2)
            self.assertEqual(58, file.read_ops)
            self.assertEqual(59, file.read_bytes)
            self.assertEqual(0, file.write_ops)
            self.assertEqual(0, file.write_bytes)
            for _ in range(77):
                file.write(b"b")
            file.write(b"bytes")
            self.assertEqual(78, file.write_ops)
            self.assertEqual(82, file.write_bytes)
            with self.assertRaisesRegex(AttributeError, "can't set"):
                file.write_ops = 0
            with self.assertRaisesRegex(AttributeError, "can't set"):
                file.write_bytes = 0
            with self.assertRaisesRegex(AttributeError, "can't set"):
                file.read_ops = 0
            with self.assertRaisesRegex(AttributeError, "can't set"):
                file.read_bytes = 0
            self.assertEqual(78, file.write_ops)
            self.assertEqual(82, file.write_bytes)
            self.assertEqual(58, file.read_ops)
            self.assertEqual(59, file.read_bytes)


if __name__ == "__main__":
    unittest.main()
