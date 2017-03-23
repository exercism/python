import unittest

from linked_list import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_push_pop(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.pop(), 20)
        self.assertEqual(self.list.pop(), 10)

    def test_push_shift(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.shift(), 10)
        self.assertEqual(self.list.shift(), 20)

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(self.list.shift(), 20)
        self.assertEqual(self.list.shift(), 10)

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(self.list.pop(), 10)
        self.assertEqual(self.list.pop(), 20)

    def test_all(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(self.list.pop(), 20)
        self.list.push(30)
        self.assertEqual(self.list.shift(), 10)
        self.list.unshift(40)
        self.list.push(50)
        self.assertEqual(self.list.shift(), 40)
        self.assertEqual(self.list.pop(), 50)
        self.assertEqual(self.list.shift(), 30)

    @unittest.skip("extra-credit")
    def test_length(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(len(self.list), 2)
        self.list.shift()
        self.assertEqual(len(self.list), 1)
        self.list.pop()
        self.assertEqual(len(self.list), 0)

    @unittest.skip("extra-credit")
    def test_iterator(self):
        self.list.push(10)
        self.list.push(20)
        iterator = iter(self.list)
        self.assertEqual(next(iterator), 10)
        self.assertEqual(next(iterator), 20)


if __name__ == '__main__':
    unittest.main()
