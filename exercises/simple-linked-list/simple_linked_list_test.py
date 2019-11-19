import unittest

from simple_linked_list import LinkedList, EmptyListException


# No canonical data available for this exercise

class SimpleLinkedListTest(unittest.TestCase):
    def test_empty_list_has_len_zero(self):
        sut = LinkedList()
        self.assertEqual(len(sut), 0)

    def test_singleton_list_has_len_one(self):
        sut = LinkedList([1])
        self.assertEqual(len(sut), 1)

    def test_non_empty_list_has_correct_len(self):
        sut = LinkedList([1, 2, 3])
        self.assertEqual(len(sut), 3)

    def test_error_on_empty_list_head(self):
        sut = LinkedList()
        with self.assertRaisesWithMessage(EmptyListException):
            sut.head()

    def test_singleton_list_has_head(self):
        sut = LinkedList([1])
        self.assertEqual(sut.head().value(), 1)

    def test_non_empty_list_has_correct_head(self):
        sut = LinkedList([1, 2])
        self.assertEqual(sut.head().value(), 2)

    def test_can_push_to_non_empty_list(self):
        sut = LinkedList([1, 2, 3])
        sut.push(4)
        self.assertEqual(len(sut), 4)

    def test_pushing_to_empty_list_changes_head(self):
        sut = LinkedList()
        sut.push(5)
        self.assertEqual(len(sut), 1)
        self.assertEqual(sut.head().value(), 5)

    def test_can_pop_from_non_empty_list(self):
        sut = LinkedList([3, 4, 5])
        self.assertEqual(sut.pop(), 5)
        self.assertEqual(len(sut), 2)
        self.assertEqual(sut.head().value(), 4)

    def test_pop_from_singleton_list_removes_head(self):
        sut = LinkedList([1])
        self.assertEqual(sut.pop(), 1)
        with self.assertRaisesWithMessage(EmptyListException):
            sut.head()

    def test_error_on_empty_list_pop(self):
        sut = LinkedList()
        with self.assertRaisesWithMessage(EmptyListException):
            sut.pop()

    def test_push_and_pop(self):
        sut = LinkedList([1, 2])
        sut.push(3)
        self.assertEqual(len(sut), 3)
        self.assertEqual(sut.pop(), 3)
        self.assertEqual(sut.pop(), 2)
        self.assertEqual(sut.pop(), 1)
        self.assertEqual(len(sut), 0)
        sut.push(4)
        self.assertEqual(len(sut), 1)
        self.assertEqual(sut.head().value(), 4)

    def test_singleton_list_head_has_no_next(self):
        sut = LinkedList([1])
        self.assertIsNone(sut.head().next())

    def test_non_empty_list_traverse(self):
        sut = LinkedList(range(10))
        current = sut.head()
        for i in range(10):
            self.assertEqual(current.value(), 9 - i)
            current = current.next()
        self.assertIsNone(current)

    def test_empty_linked_list_to_list_is_empty(self):
        sut = LinkedList()
        self.assertEqual(list(sut), [])

    def test_singleton_linked_list_to_list_list_with_singular_element(self):
        sut = LinkedList([1])
        self.assertEqual(list(sut), [1])

    def test_non_empty_linked_list_to_list_is_list_with_all_elements(self):
        sut = LinkedList([1, 2, 3])
        self.assertEqual(list(sut), [3, 2, 1])

    def test_reversed_empty_list_is_empty_list(self):
        sut = LinkedList([])
        self.assertEqual(list(sut.reversed()), [])

    def test_reversed_singleton_list_is_same_list(self):
        sut = LinkedList([1])
        self.assertEqual(list(sut.reversed()), [1])

    def test_reverse_non_empty_list(self):
        sut = LinkedList([1, 2, 3])
        self.assertEqual(list(sut.reversed()), [1, 2, 3])

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
