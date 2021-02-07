import errno
import os
import unittest
from unittest.mock import ANY, call, NonCallableMagicMock, patch

from test_utils import MockSock, MockFile, MockException, ZEN, SuperMock, LOGGER
from paasio import MeteredFile, MeteredSocket

class PaasioTest(unittest.TestCase):
    def test_meteredsocket_context_manager(self):
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

    def test_meteredsocket_context_manager_exception_raise(self):
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

    def test_meteredsocket_context_manager_exception_suppress(self):
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

    def test_meteredsocket_recv_once(self):
        mock = NonCallableMagicMock(wraps=MockSock(), autospec=True)
        with MeteredSocket(mock) as socket:
            actual_recv = socket.recv(4096)
        self.assertEqual(ZEN, actual_recv)
        self.assertEqual(1, socket.recv_ops)
        self.assertEqual(len(ZEN), socket.recv_bytes)
        self.assertEqual(1, mock.recv.call_count)

    def test_meteredsocket_recv_multiple(self):
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

    def test_meteredsocket_recv_multiple_chunk(self):
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

    def test_meteredsocket_recv_under_size(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            actual_recv = socket.recv(4096)
        self.assertEqual(ZEN[:257], actual_recv)
        self.assertEqual(1, socket.recv_ops)
        self.assertEqual(257, socket.recv_bytes)
        self.assertEqual(1, mock.recv.call_count)

    def test_meteredsocket_send_once(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            send_len = socket.send(ZEN)
            self.assertEqual(ZEN[:257], wrapped._sender.getbuffer())
        self.assertEqual(257, send_len)
        self.assertEqual(1, socket.send_ops)
        self.assertEqual(257, socket.send_bytes)
        self.assertEqual(1, mock.send.call_count)

    def test_meteredsocket_send_multiple(self):
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

    def test_meteredsocket_send_under_size(self):
        wrapped = MockSock(chunk=257)  # largish odd number
        mock = NonCallableMagicMock(wraps=wrapped, autospec=True)
        with MeteredSocket(mock) as socket:
            send_len = socket.send(ZEN[:123])
            self.assertEqual(ZEN[:123], wrapped._sender.getbuffer())
        self.assertEqual(123, send_len)
        self.assertEqual(1, socket.send_ops)
        self.assertEqual(123, socket.send_bytes)
        self.assertEqual(1, mock.send.call_count)

    def test_meteredsocket_bufsize_required(self):
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

    def test_meteredsocket_flags_support(self):
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

    def test_meteredsocket_stats_read_only(self):
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