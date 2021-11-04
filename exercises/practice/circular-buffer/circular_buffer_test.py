import unittest

from circular_buffer import (
    CircularBuffer,
    BufferEmptyException,
    BufferFullException,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class CircularBufferTest(unittest.TestCase):
    def test_reading_empty_buffer_should_fail(self):
        buf = CircularBuffer(1)
        with self.assertRaises(BufferError) as err:
            buf.read()

        self.assertEqual(type(err.exception), BufferEmptyException)
        self.assertEqual(err.exception.args[0], "Circular buffer is empty")

    def test_can_read_an_item_just_written(self):
        buf = CircularBuffer(1)
        buf.write("1")
        self.assertEqual(buf.read(), "1")

    def test_each_item_may_only_be_read_once(self):
        buf = CircularBuffer(1)
        buf.write("1")
        self.assertEqual(buf.read(), "1")
        with self.assertRaises(BufferError) as err:
            buf.read()

        self.assertEqual(type(err.exception), BufferEmptyException)
        self.assertEqual(err.exception.args[0], "Circular buffer is empty")

    def test_items_are_read_in_the_order_they_are_written(self):
        buf = CircularBuffer(2)
        buf.write("1")
        buf.write("2")
        self.assertEqual(buf.read(), "1")
        self.assertEqual(buf.read(), "2")

    def test_full_buffer_can_t_be_written_to(self):
        buf = CircularBuffer(1)
        buf.write("1")
        with self.assertRaises(BufferError) as err:
            buf.write("2")

        self.assertEqual(type(err.exception), BufferFullException)
        self.assertEqual(err.exception.args[0], "Circular buffer is full")

    def test_a_read_frees_up_capacity_for_another_write(self):
        buf = CircularBuffer(1)
        buf.write("1")
        self.assertEqual(buf.read(), "1")
        buf.write("2")
        self.assertEqual(buf.read(), "2")

    def test_read_position_is_maintained_even_across_multiple_writes(self):
        buf = CircularBuffer(3)
        buf.write("1")
        buf.write("2")
        self.assertEqual(buf.read(), "1")
        buf.write("3")
        self.assertEqual(buf.read(), "2")
        self.assertEqual(buf.read(), "3")

    def test_items_cleared_out_of_buffer_can_t_be_read(self):
        buf = CircularBuffer(1)
        buf.write("1")
        buf.clear()
        with self.assertRaises(BufferError) as err:
            buf.read()

        self.assertEqual(type(err.exception), BufferEmptyException)
        self.assertEqual(err.exception.args[0], "Circular buffer is empty")

    def test_clear_frees_up_capacity_for_another_write(self):
        buf = CircularBuffer(1)
        buf.write("1")
        buf.clear()
        buf.write("2")
        self.assertEqual(buf.read(), "2")

    def test_clear_does_nothing_on_empty_buffer(self):
        buf = CircularBuffer(1)
        buf.clear()
        buf.write("1")
        self.assertEqual(buf.read(), "1")

    def test_overwrite_acts_like_write_on_non_full_buffer(self):
        buf = CircularBuffer(2)
        buf.write("1")
        buf.overwrite("2")
        self.assertEqual(buf.read(), "1")
        self.assertEqual(buf.read(), "2")

    def test_overwrite_replaces_the_oldest_item_on_full_buffer(self):
        buf = CircularBuffer(2)
        buf.write("1")
        buf.write("2")
        buf.overwrite("3")
        self.assertEqual(buf.read(), "2")
        self.assertEqual(buf.read(), "3")

    def test_overwrite_replaces_the_oldest_item_remaining_in_buffer_following_a_read(
        self,
    ):
        buf = CircularBuffer(3)
        buf.write("1")
        buf.write("2")
        buf.write("3")
        self.assertEqual(buf.read(), "1")
        buf.write("4")
        buf.overwrite("5")
        self.assertEqual(buf.read(), "3")
        self.assertEqual(buf.read(), "4")
        self.assertEqual(buf.read(), "5")

    def test_initial_clear_does_not_affect_wrapping_around(self):
        buf = CircularBuffer(2)
        buf.clear()
        buf.write("1")
        buf.write("2")
        buf.overwrite("3")
        buf.overwrite("4")
        self.assertEqual(buf.read(), "3")
        self.assertEqual(buf.read(), "4")
        with self.assertRaises(BufferError) as err:
            buf.read()

        self.assertEqual(type(err.exception), BufferEmptyException)
        self.assertEqual(err.exception.args[0], "Circular buffer is empty")
