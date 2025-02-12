import unittest
import pytest
from collections import OrderedDict
from dict_methods import (
    add_item,
    read_notes,
    update_recipes,
    sort_entries,
    send_to_store,
    update_store_inventory,
)

from dict_methods_test_data import (
    add_item_data,
    read_notes_data,
    update_recipes_data,
    sort_entries_data,
    send_to_store_data,
    update_store_inventory_data,
)

class MechaMunchManagementTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_add_item(self):
        for variant, (input_data, expected) in enumerate(add_item_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = add_item(input_data[0], input_data[1])
                error_msg= (f'Called add_item({input_data[0]}, {input_data[1]}). '
                            f'The function returned {actual_result}, but the tests '
                            f'expected: {expected} once the item was added.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_read_notes(self):
        for variant, (input_data, expected) in enumerate(read_notes_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = read_notes(input_data)
                error_msg = (f'Called read_notes({input_data}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} once the notes were read.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_update_recipes(self):
        for variant, (input_data, expected) in enumerate(update_recipes_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_recipes(input_data[0], input_data[1])
                error_msg = (f'Called update_recipes({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} once the recipes were updated.')

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def test_sort_entries(self):
        for variant, (input_data, expected) in enumerate(sort_entries_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expecred=expected):
                actual_result = sort_entries(input_data)
                error_msg = (f'Called sort_entries({input_data}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} for the sorted entries.')

                # Because we are asserting equal, we need to convert to an OrderedDict.
                # Regular dictionaries will compare equal even when they are ordered
                # differently from one another. See https://stackoverflow.com/a/58961124
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)

    @pytest.mark.task(taskno=5)
    def test_send_to_store(self):
        for variant, (input_data, expected) in enumerate(send_to_store_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = send_to_store(input_data[0], input_data[1])
                error_msg = (f'Called send_to_store({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} as the fulfillment cart.')

                # Because we are asserting equal, we need to convert to an OrderedDict.
                # Regular dictionaries will compare equal even when they are ordered
                # differently from one another. See https://stackoverflow.com/a/58961124
                self.assertEqual(OrderedDict(actual_result), OrderedDict(expected), msg=error_msg)

    @pytest.mark.task(taskno=6)
    def test_update_store_inventory(self):
        for variant, (input_data, expected) in enumerate(update_store_inventory_data, start=1):
            with self.subTest(f'variation #{variant}', input_data=input_data, expected=expected):
                actual_result = update_store_inventory(input_data[0], input_data[1])
                error_msg = (f'Called update_store_inventory({input_data[0]}, {input_data[1]}). '
                             f'The function returned {actual_result}, but the tests '
                             f'expected: {expected} as the store inventory.')

                self.assertEqual(actual_result, expected, msg=error_msg)
