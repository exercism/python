import unittest

from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    def test_push_pop(self):
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(lst.pop(), 20)
        self.assertEqual(lst.pop(), 10)

    def test_push_shift(self):
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(lst.shift(), 10)
        self.assertEqual(lst.shift(), 20)

    def test_unshift_shift(self):
        lst = LinkedList()
        lst.unshift(10)
        lst.unshift(20)
        self.assertEqual(lst.shift(), 20)
        self.assertEqual(lst.shift(), 10)

    def test_unshift_pop(self):
        lst = LinkedList()
        lst.unshift(10)
        lst.unshift(20)
        self.assertEqual(lst.pop(), 10)
        self.assertEqual(lst.pop(), 20)

    def test_all(self):
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(lst.pop(), 20)
        lst.push(30)
        self.assertEqual(lst.shift(), 10)
        lst.unshift(40)
        lst.push(50)
        self.assertEqual(lst.shift(), 40)
        self.assertEqual(lst.pop(), 50)
        self.assertEqual(lst.shift(), 30)

    @unittest.skip("extra-credit")
    def test_length(self):
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        self.assertEqual(len(lst), 2)
        lst.shift()
        self.assertEqual(len(lst), 1)
        lst.pop()
        self.assertEqual(len(lst), 0)

    @unittest.skip("extra-credit")
    def test_iterator(self):
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        iterator = iter(lst)
        self.assertEqual(next(iterator), 10)
        self.assertEqual(next(iterator), 20)

    @unittest.skip("extra-credit")
    def test_iterator_independence(self):
        lst = LinkedList()
        lst.push(10)
        lst.push(20)
        iterator_a = iter(lst)
        iterator_b = iter(lst)
        self.assertEqual(next(iterator_a), 10)
        self.assertEqual(next(iterator_a), 20)
        self.assertEqual(next(iterator_b), 10)
        self.assertEqual(next(iterator_b), 20)


if __name__ == '__main__':
    unittest.main()
