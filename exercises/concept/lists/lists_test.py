import unittest
import random
from io import StringIO
import sys
from example import (
    to_list,
    list_twice,
    concatenate_lists,
    list_contains_object,
    first_and_last,
    interior_of_list,
    even_elements,
    odd_elements,
    unshuffle,
    print_list,
    multitype_list,
    swap_first_and_last,
)


class CaptureOutput(list):

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class TestToList(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            to_list('10H', 'JH', 'QH', 'KH', 'AH'),
            ['10H', 'JH', 'QH', 'KH', 'AH']
        )

    def test_5_random_ints(self):
        _list = [random.randint(0, 100) for i in range(5)]
        self.assertEqual(_list, to_list(*_list))

    def test_too_few_args(self):
        _list = [1, 2, 3, 4]
        with self.assertRaises(TypeError):
            to_list(*_list)

    def test_too_many_args(self):
        _list = [1, 2, 3, 4, 5, 6]
        with self.assertRaises(TypeError):
            to_list(*_list)


class TestListTwice(unittest.TestCase):

    def test_instructions_example(self):
        list1, list2 = list_twice(['AC', 'AD', 'AH', 'AS'])
        self.assertEqual(list1, list2)
        self.assertIsNot(list1, list2)

    def test_correct_values(self):
        for i in range(5):
            _list = [random.randint(0, 100) for _ in range(5)]
            list1, list2 = list_twice(_list)
            self.assertEqual(list1, list2)

    def test_distinct_objects(self):
        for i in range(5):
            _list = [random.randint(0, 100) for _ in range(5)]
            list1, list2 = list_twice(_list)
            self.assertIsNot(list1, list2)


class TestConcatenateLists(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            concatenate_lists(['2C', '2H', '2D'], ['KC', 'KD']),
            ['2C', '2H', '2D', 'KC', 'KD']
        )

    def test_empty_lists(self):
        _list = [random.randint(0, 100) for _ in range(5)]
        newlist = concatenate_lists(_list, [])
        self.assertEqual(_list, newlist)
        self.assertIsNot(_list, newlist)

    def test_lists_of_ints(self):
        list1 = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        list2 = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        newlist = list1 + list2
        self.assertEqual(newlist, concatenate_lists(list1, list2))


class TestListContainsObject(unittest.TestCase):

    def test_instructions_example_1(self):
        self.assertTrue(list_contains_object(['AC', 'AD', 'AH', 'AS'], 'AC'))

    def test_instructions_example_2(self):
        self.assertFalse(list_contains_object(['AC', 'AD', 'AH', 'AS'], '10C'))

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        element = random.randint(0, 200)
        _list_contains_object = (element in _list)
        self.assertTrue(
            list_contains_object(_list, element) == _list_contains_object
        )


class TestFirstAndLast(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            first_and_last(['2C', '2H', '2D', 'KC', 'KD']),
            ['2C', 'KD']
        )

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        self.assertEqual(first_and_last(_list), [_list[0], _list[-1]])


class InteriorOfList(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            interior_of_list(['2C', '2H', '2D', 'KC', 'KD']),
            ['2H', '2D', 'KC']
        )

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        self.assertEqual(interior_of_list(_list), _list[1:-1])


class TestEvenElements(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            even_elements(['2C', '2H', '2D', 'KC', 'KD']),
            ['2C', '2D', 'KD']
        )

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        self.assertEqual(even_elements(_list), _list[::2])


class OddElements(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            odd_elements(['2C', '2H', '2D', 'KC', 'KD']),
            ['2H', 'KC']
        )

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        self.assertEqual(odd_elements(_list), _list[1::2])


class Unshuffle(unittest.TestCase):

    def test_instructions_example(self):
        self.assertEqual(
            unshuffle(['2C', '2H', '2D', 'KC', 'KD']),
            ['2C', '2D', 'KD', '2H', 'KC']
        )

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        self.assertEqual(
            unshuffle(_list),
            _list[::2] + _list[1::2]
        )


class PrintList(unittest.TestCase):

    def test_instructions_example(self):
        with CaptureOutput() as output:
            print_list(['2C', '2H', '2D', 'KC', 'KD'])
        self.assertEqual(
            output,
            ["2C", "2H", "2D", "KC", "KD"]
        )

    def test_random_ints(self):
        _list = [
            random.randint(0, 100) for _ in range(1, random.randint(2, 100))
        ]
        with CaptureOutput() as output:
            print_list(_list)
        self.assertEqual([str(_) for _ in _list], output)


class MultitypeList(unittest.TestCase):

    def test_multitype_list(self):
        print(multitype_list())
        self.assertTrue(len(set([type(_) for _ in multitype_list()])) >= 3)


class SwapFirstAndLast(unittest.TestCase):

    def test_instructions_example(self):
        _list = ['2C', '2H', '2D', 'KC', 'KD']
        return_value = swap_first_and_last(_list)
        self.assertIsNone(return_value)
        self.assertEqual(_list, ['KD', '2H', '2D', 'KC', '2C'])
