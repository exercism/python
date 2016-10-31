import unittest

from simple_linked_list import LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.slist = LinkedList()

    def test_size(self):
        self.slist.push(0)
        self.assertEqual(1, self.slist.size)
        # notice if size is increased
        self.slist.push(1)
        self.assertEqual(2, self.slist.size)
        self.slist.push(2)
        self.assertEqual(3, self.slist.size)

    def test_pop(self):
        # with cero element
        self.assertIsNone(self.slist.pop())
        # with multiple elements
        self.slist.push(1)
        self.slist.push(2)
        self.slist.push(3)
        self.assertEqual(3, self.slist.pop())
        self.assertEqual(2, self.slist.pop())
        self.assertEqual(1, self.slist.pop())
        self.assertIsNone(self.slist.pop())

    def test_reverse(self):
        # empty reversed LinkedList
        empty_reversed = self.slist.reverse()
        self.assertEqual(0, empty_reversed.size)
        self.assertIsNone(empty_reversed.head)
        # push_elements
        self.slist.push(1)
        self.slist.push(2)
        self.slist.push(3)
        self.slist.push(4)
        reversed_list = self.slist.reverse()
        self.assertEqual(4, reversed_list.head.value)
        self.assertEqual(1, reversed_list.get_peek())

    def test_to_array(self):
        # in : empty list out : empty array
        self.assertListEqual([], self.slist.to_array())
        # push_elements
        self.slist.push(1)
        self.slist.push(2)
        self.slist.push(3)
        self.slist.push(4)
        self.assertListEqual([1, 2, 3, 4], self.slist.to_array())

    def test_from_array(self):
        # in : empty array out : empty list
        self.assertIsNone(self.slist.from_array([]).head)
        # push_elements
        new_arr = [1, 2, 3, 4]
        self.assertEqual(1, self.slist.from_array(new_arr).head.value)
        self.assertEqual(4, self.slist.from_array(new_arr).get_peek())


if __name__ == '__main__':
    unittest.main()
