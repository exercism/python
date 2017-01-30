import unittest

from linked_list import LinkedList


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_push_pop(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(20, self.list.pop())
        self.assertEqual(10, self.list.pop())

    def test_push_shift(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(10, self.list.shift())
        self.assertEqual(20, self.list.shift())

    def test_unshift_shift(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(20, self.list.shift())
        self.assertEqual(10, self.list.shift())

    def test_unshift_pop(self):
        self.list.unshift(10)
        self.list.unshift(20)
        self.assertEqual(10, self.list.pop())
        self.assertEqual(20, self.list.pop())

    def test_all(self):
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(20, self.list.pop())
        self.list.push(30)
        self.assertEqual(10, self.list.shift())
        self.list.unshift(40)
        self.list.push(50)
        self.assertEqual(40, self.list.shift())
        self.assertEqual(50, self.list.pop())
        self.assertEqual(30, self.list.shift())

    @unittest.skip("advanced")
    def test_len(self):
        self.assertEqual(0, len(self.list))
        self.list.push(10)
        self.list.push(20)
        self.assertEqual(2, len(self.list))

    @unittest.skip("advanced")
    def test_iter(self):
        values = [10, 20, 30, 40]
        for value in values:
            self.list.push(value)

        for index, node in enumerate(self.list):
            self.assertEqual(values[index], node.value)

        iterator = iter(self.list)
        for value in values:
            self.assertEqual(value, next(iterator).value)

if __name__ == '__main__':
    unittest.main()
