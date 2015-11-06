import unittest

from linked_list import Deque


class DequeTests(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()

    def test_push_pop(self):
        self.deque.push(10)
        self.deque.push(20)
        self.assertEqual(20, self.deque.pop())
        self.assertEqual(10, self.deque.pop())

    def test_push_shift(self):
        self.deque.push(10)
        self.deque.push(20)
        self.assertEqual(10, self.deque.shift())
        self.assertEqual(20, self.deque.shift())

    def test_unshift_shift(self):
        self.deque.unshift(10)
        self.deque.unshift(20)
        self.assertEqual(20, self.deque.shift())
        self.assertEqual(10, self.deque.shift())

    def test_unshift_pop(self):
        self.deque.unshift(10)
        self.deque.unshift(20)
        self.assertEqual(10, self.deque.pop())
        self.assertEqual(20, self.deque.pop())

    def test_all(self):
        self.deque.push(10)
        self.deque.push(20)
        self.assertEqual(20, self.deque.pop())
        self.deque.push(30)
        self.assertEqual(10, self.deque.shift())
        self.deque.unshift(40)
        self.deque.push(50)
        self.assertEqual(40, self.deque.shift())
        self.assertEqual(50, self.deque.pop())
        self.assertEqual(30, self.deque.shift())

if __name__ == '__main__':
    unittest.main()
